==============
Screening file
==============

|scr|

The screening file sets up the microscopic RPA dielectric screening of a 2D material (see
:doc:`../methods/screening`). It is passed with ``-z``, always **together with an exciton file**, whose
``# label`` names the output files:

.. code-block:: bash

   xatu -d 50 -z screening.txt system.outp exciton.txt

It uses the common syntax of :doc:`../input_files`, one line per block.

Example:

.. code-block:: text

   # function
   exciton
   # valence.bands
   4
   # conduction.bands
   8
   # ncell_aux
   17
   # spin
   false
   # gcutoff
   5.0

Required blocks
===============

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Keyword
     - Content
   * - ``# function``
     - What to compute: ``dielectric``, ``polarizability``, ``inversedielectric`` or ``exciton`` (see
       below).
   * - ``# valence.bands``
     - Number of valence bands included in the polarizability.
   * - ``# conduction.bands``
     - Number of conduction bands included in the polarizability.
   * - ``# ncell_aux``
     - Number of k-points per direction of the auxiliary mesh used to compute the polarizability.
       Default 17.
   * - ``# spin``
     - ``true`` if spin is part of the orbital basis; ``false`` applies a spin-degeneracy factor of 2.
   * - ``# gcutoff``
     - Cutoff on :math:`|\bm{G}|` for the reciprocal-lattice vectors of the dielectric matrix. Default
       10. It may be larger than the ``gcutoff`` of the exciton file.

Optional blocks
===============

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Keyword
     - Content
   * - ``# momentum``
     - Momentum :math:`\bm{q}` (``qx qy qz``) for the single-momentum functions. Default ``0.2 0 0``.
   * - ``# vectors``
     - Pair of :math:`\bm{G}`-vector indices ``i j`` selecting the element :math:`\chi_{\bm{G}\bm{G}'}` or
       :math:`\epsilon_{\bm{G}\bm{G}'}` for ``dielectric`` and ``polarizability``. Default ``0 0``.
   * - ``# isotropic``
     - ``true`` or ``false`` *(default)*: whether the material is in-plane isotropic.
   * - ``# thickness``
     - Thickness :math:`d_\perp` of the material (Å). If non-zero, the quasi-2D (Q2D) dielectric
       function is computed instead of the strictly 2D one. Default 0.

The four functions
==================

.. list-table::
   :header-rows: 1
   :widths: 22 42 36

   * - ``# function``
     - Computes
     - Writes
   * - ``dielectric``
     - One element :math:`\epsilon_{\bm{G}\bm{G}'}(\bm{q})` at ``# momentum``, for ``# vectors``. Also
       tracks the convergence of the polarizability with the number of bands. Then stops.
     - ``polarizability_convergence.dat``: ``[# val. bands] [# cond. bands] [Re χ] [Im χ]`` per line.
   * - ``polarizability``
     - :math:`\chi_{\bm{G}\bm{G}'}` for ``# vectors`` over the whole BZ mesh. Then stops.
     - ``polarizability_mesh.dat``: ``[kx] [ky] [kz] [Re χ] [Im χ]`` per line (``kz = 0``).
   * - ``inversedielectric``
     - The full matrix :math:`\epsilon^{-1}(\bm{q})` at ``# momentum``. Then stops. The order of the
       :math:`\bm{G}` vectors is printed to the terminal.
     - ``<label>_invepsilon.dat`` (see :doc:`../outputs/invpesilon`).
   * - ``exciton``
     - :math:`\epsilon^{-1}(\bm{q})` on the whole BZ mesh, then **continues with the exciton
       calculation** using the ``rpa`` potential.
     - ``kgrid_<ncells>.dat`` and ``<label>_invepsilon.dat``, plus the usual exciton outputs.
