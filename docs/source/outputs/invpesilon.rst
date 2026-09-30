=================
Screening outputs
=================

With ``-z``, Xatu writes the screening it computes (see :doc:`../input_files/screening` for which
function writes what, in each mode):

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - File
     - Content
   * - ``<label>_invepsilon.dat``
     - Inverse dielectric matrix :math:`\epsilon^{-1}(\bm{q})` at one :math:`\bm{q}` or on the BZ mesh
       (projected response :math:`M` in ``q2d_averaged``).
   * - ``<label>_epsilon.dat``
     - Dielectric matrix :math:`\epsilon(\bm{q})` at one :math:`\bm{q}`.
   * - ``kgrid_<ncells>.dat``
     - The :math:`\bm{q}`-points of the mesh, for ``# function exciton``.
   * - ``polarizability_mesh.dat``, ``<label>_polarizability.dat``
     - Polarizability.
   * - ``<label>_q2d_atomic.dat``
     - Full atomic-plane screening (``q2d_atomic``).
   * - ``<label>_zdecomposition.dat``
     - Plane-pair decomposition of the direct interaction (``q2d_atomic``).

``<label>_invepsilon.dat`` and ``<label>_epsilon.dat``
======================================================

Each matrix is :math:`N_G\times N_G` complex, written as :math:`N_G` rows of :math:`2N_G` numbers,
with real and imaginary parts side by side:

.. code-block:: text

   Re(G0,G0)  Im(G0,G0)  Re(G0,G1)  Im(G0,G1)  ...  Re(G0,Gn)  Im(G0,Gn)
   Re(G1,G0)  Im(G1,G0)  ...
   ...
   Re(Gn,G0)  Im(Gn,G0)  ...                        Re(Gn,Gn)  Im(Gn,Gn)

* At a single momentum (``dielectric``, ``inversedielectric``): one matrix, at ``# momentum``.
* With ``exciton``: one matrix per :math:`\bm{q}`-point, stacked (:math:`N_G` rows each), in the order
  of ``kgrid_<ncells>.dat``.

The :math:`\bm{G}` vectors (all with :math:`|\bm{G}|` below the screening ``gcutoff``, including
:math:`\bm{G}=0`) appear in the order printed to the terminal. The macroscopic dielectric function is
:math:`\epsilon_M(\bm{q}) = 1/\epsilon^{-1}_{00}(\bm{q})`.

In ``q2d_averaged`` mode the files have the same layout, written with 17 significant digits.
``_invepsilon.dat`` then holds the projected response :math:`M(\bm{q})` of
:doc:`../methods/screening`, so :math:`\epsilon_M(\bm{q}) = 1/M_{00}(\bm{q})`.

.. code-block:: python

   import numpy as np
   raw = np.loadtxt("hBN_invepsilon.dat")
   NG = raw.shape[1] // 2
   inv_eps = (raw[:, 0::2] + 1j * raw[:, 1::2]).reshape(-1, NG, NG)   # [q, G, G']
   eps_M = 1 / inv_eps[:, 0, 0].real
   q = np.loadtxt("kgrid_20.dat")

``kgrid_<ncells>.dat``
======================

One :math:`\bm{q}`-point per line (``qx qy qz``), in the same units as the k-mesh of the calculation.

Polarizability files
====================

``polarizability_mesh.dat`` (``2d`` mode)
   One line per k-point of the BZ mesh: ``kx ky kz Re(chi) Im(chi)``, for the element
   :math:`\chi_{\bm{G}\bm{G}'}` selected by ``# vectors``.

``<label>_polarizability.dat`` (``q2d_legacy`` mode)
   The polarizability matrix at ``# momentum``, in the matrix layout above.

``<label>_q2d_atomic.dat``
==========================

The complete atomic-plane screening at ``# momentum``, written with 17 significant digits. The file
starts with comment lines (``#``) describing the conventions, then:

.. code-block:: text

   planes <Nplanes>
   <z of each plane, one per line>                       (Angstrom)
   G <NG>
   <Gx Gy Gz, one per line>                              (1/Angstrom)
   q <index> <qx> <qy> <qz>
   P <n>            then n*n lines "Re Im", row by row
   B <n>            ...
   R <n>
   W <n>
   epsilon_at <n>
   inverse_epsilon_at <n>

The matrices are those of :doc:`../methods/screening`: the susceptibility :math:`P`, the bare
interaction :math:`B`, the screened response :math:`R = (I-PB)^{-1}P`, the screened interaction
:math:`W = B + BRB`, and :math:`I - BP` and :math:`I + BR`. They are indexed by
``G*Nplanes + plane``, with :math:`W` in eV and :math:`P`, :math:`R` in eV\ :sup:`-1`. The scalar
:math:`\bm{q}=0` correction used in the BSE is not included.

``<label>_zdecomposition.dat``
==============================

Written with ``# zdecomposition.states`` in ``q2d_atomic`` mode. For each requested exciton
:math:`\lambda`, it splits the direct-interaction energy into ordered plane pairs :math:`(a, b)`:

.. math::

   E_{ab}(\lambda) = \langle A^\lambda | K^d_{ab} | A^\lambda\rangle, \qquad
   \sum_{ab} E_{ab} = E_\text{direct},

for the screened interaction (:math:`W`) and for the bare one (:math:`V`), on the same exciton state.
The difference :math:`E_{ab}[W] - E_{ab}[V]` isolates the screening. A header of ``#`` lines explains
every field. The data follow:

.. code-block:: text

   planes <Nplanes>
   states <Nstates>
   z <a> <z_a>                                          (one line per plane, Angstrom)
   state <lambda> energy <E> E_direct_W_re <> E_direct_W_im <> E_sum_W_re <> E_sum_W_im <>
         E_sum_V_re <> E_sum_V_im <> residual_abs <> residual_rel <>
   a  b  z_a  z_b  Re(E_ab_W)  Im(E_ab_W)  Re(E_ab_V)  Im(E_ab_V)     (Nplanes^2 lines)
   ...                                                  (next state)

Energies are in eV and state indices are 1-based, as in the terminal output. ``E_sum_V`` is the bare
operator's expectation value on the screened exciton, not a second BSE solution.

Reusing a computed matrix
=========================

The screening is the expensive part of an ``rpa`` calculation. Through the Xatu library it can be
reused:

* ``ExcitonTB::readInverseDielectricMatrix(filename)`` loads a matrix written in the
  ``_invepsilon.dat`` format. That lets you repeat the exciton calculation with other parameters
  (solver, regularization, ...) without recomputing the screening. ``main/read_screening.cpp`` in the
  repository shows how.
* ``ExcitonTB::augment_2D_DielectricMatrix(Gcutoff)``, called after a successful
  ``readInverseDielectricMatrix``, extends a loaded matrix to a larger ``Gcutoff``. Only the missing
  elements are computed. It fills the dielectric matrix, so call ``ExcitonTB::invertDielectricMatrix()``
  afterwards. The new :math:`\bm{G}` vectors are appended after those of the file, so the order can
  differ from a calculation done directly at the larger cutoff. Available for the ``2d`` and
  ``q2d_legacy`` modes.
* To go to a *smaller* ``Gcutoff``, read the matrix, invert it back to :math:`\epsilon`, drop the extra
  :math:`\bm{G}` vectors, and invert again. This can be done in any language.
