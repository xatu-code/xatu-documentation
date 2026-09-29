============================================
Inverse dielectric matrix (``_invepsilon``)
============================================

|scr|

With ``-z`` and ``# function`` set to ``inversedielectric`` or ``exciton`` in the
:doc:`screening file <../input_files/screening>`, Xatu writes the inverse RPA dielectric matrix
:math:`\epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})` (see :doc:`../methods/screening`):

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - File
     - Function
     - Content
   * - ``<label>_invepsilon.dat``
     - both
     - :math:`\epsilon^{-1}(\bm{q})` at one :math:`\bm{q}` (``inversedielectric``) or on the whole BZ
       mesh (``exciton``).
   * - ``kgrid_<ncells>.dat``
     - ``exciton``
     - The :math:`\bm{q}`-points of the mesh, in the order used in ``_invepsilon.dat``.

``<label>_invepsilon.dat``
==========================

Each :math:`\epsilon^{-1}(\bm{q})` is an :math:`N_G\times N_G` complex matrix, written as :math:`N_G`
rows of :math:`2N_G` numbers, with real and imaginary parts side by side:

.. code-block:: text

   Re(G0,G0)  Im(G0,G0)  Re(G0,G1)  Im(G0,G1)  ...  Re(G0,Gn)  Im(G0,Gn)
   Re(G1,G0)  Im(G1,G0)  ...
   ...
   Re(Gn,G0)  Im(Gn,G0)  ...                        Re(Gn,Gn)  Im(Gn,Gn)

* **inversedielectric**: a single matrix, at the ``# momentum`` of the screening file.
* **exciton**: one matrix per :math:`\bm{q}`-point, stacked one after another (:math:`N_G` rows each),
  in the order of ``kgrid_<ncells>.dat``.

The :math:`\bm{G}` vectors (all with :math:`|\bm{G}|` below the screening ``gcutoff``, including
:math:`\bm{G}=0`) appear in the order printed to the terminal during the run.

The macroscopic dielectric function is :math:`\epsilon_M(\bm{q}) = 1/\epsilon^{-1}_{00}(\bm{q})`, the
inverse of the first element of each matrix.

.. code-block:: python

   import numpy as np
   raw = np.loadtxt("hBN_invepsilon.dat")
   NG = raw.shape[1] // 2
   inv_eps = (raw[:, 0::2] + 1j * raw[:, 1::2]).reshape(-1, NG, NG)   # [q, G, G']
   eps_M = 1 / inv_eps[:, 0, 0].real
   q = np.loadtxt("kgrid_20.dat")

``kgrid_<ncells>.dat``
======================

One :math:`\bm{q}`-point per line, in the same units as the k-mesh of the calculation:

.. code-block:: text

   qx0 qy0 qz0
   qx1 qy1 qz1
   ...

Reusing a computed matrix
=========================

The screening is the expensive part of an ``rpa`` calculation. Through the Xatu library it can be
reused:

* ``ExcitonTB::readInverseDielectricMatrix(filename)`` loads a matrix written in this format. That lets
  you repeat the exciton calculation with other parameters (solver, regularization, …) without
  recomputing the screening. ``main/read_screening.cpp`` in the repository shows how.
* ``ExcitonTB::augment_2D_DielectricMatrix(Gcutoff)``, called after a successful
  ``readInverseDielectricMatrix``, extends a loaded matrix to a larger ``Gcutoff``. Only the missing
  elements are computed.
* To go to a *smaller* ``Gcutoff``, read the matrix, invert it back to :math:`\epsilon`, drop the extra
  :math:`\bm{G}` vectors, and invert again. This can be done in any language.
