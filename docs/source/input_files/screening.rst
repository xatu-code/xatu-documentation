==============
Screening file
==============

The screening file sets up the microscopic RPA dielectric screening of a 2D material (see
:doc:`../methods/screening`). It is passed with ``-z``, always **together with an exciton file**, whose
``# label`` names the output files:

.. code-block:: bash

   xatu -d 50 -z screening.txt system.outp exciton.txt

It uses the common syntax of :doc:`../input_files`, one line per block.

Example (atomic-plane screening, then the exciton):

.. code-block:: text

   # function
   exciton
   # screening.mode
   q2d_atomic
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
       :ref:`below <screening-functions>`).
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

Screening model
===============

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Keyword
     - Content
   * - ``# screening.mode``
     - The screening model (see :doc:`../methods/screening`). Default ``2d``.

       * ``2d``: strictly two-dimensional RPA dielectric matrix.
       * ``q2d_legacy``: quasi-2D RPA, averaged over a slab of thickness ``# thickness``.
       * ``q2d_atomic``: quasi-2D RPA resolved on the atomic planes of the structure, solved
         analytically in :math:`z`.
       * ``q2d_averaged``: the ``q2d_atomic`` response, averaged uniformly in :math:`z` after the
         inversion.
   * - ``# thickness``
     - Slab thickness :math:`d_\perp` (Angstrom) for ``q2d_legacy``. Required and positive in that
       mode; ignored by the others.
   * - ``# isotropic``
     - ``true`` or ``false`` *(default)*. If ``false``, the :math:`\bm{q}=0` regularization of the ``2d``
       and ``q2d_legacy`` modes averages the dielectric function along :math:`\bm{q}_0` and the
       perpendicular direction.

Single-momentum options
=======================

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Keyword
     - Content
   * - ``# momentum``
     - Momentum :math:`\bm{q}` (``qx qy qz``) at which ``dielectric``, ``polarizability`` and
       ``inversedielectric`` are computed. Not used by ``exciton``. Default ``0.2 0 0``.
   * - ``# vectors``
     - Pair of :math:`\bm{G}`-vector indices ``i j`` for the ``polarizability`` function in ``2d`` mode.
       Default ``0 0``.

Averaging interval (``q2d_averaged``)
=====================================

By default the response is averaged over the extent of the atomic planes,
:math:`[z_\mathrm{min}, z_\mathrm{max}]`. The result depends on this interval, and the interval used is
printed.

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Keyword
     - Content
   * - ``# zaverage.margin``
     - Widens the interval to :math:`[z_\mathrm{min} - m, z_\mathrm{max} + m]` (Angstrom). Default 0.
   * - ``# zaverage.zmin``, ``# zaverage.zmax``
     - Explicit bounds (Angstrom). Each replaces the bound on its side, including the margin. All atomic
       planes must lie inside the interval.

A structure whose atoms all sit at one height needs a margin or both bounds. The old ``cheb.*`` keywords
are no longer accepted.

Diagnostics (``q2d_atomic``)
============================

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Keyword
     - Content
   * - ``# zdecomposition.states``
     - With ``# function exciton``: list of 1-based exciton indices, e.g. ``1 2``. For each, the direct
       interaction term is split into contributions from each ordered pair of atomic planes, for the
       screened and the bare interaction, and written to ``<label>_zdecomposition.dat`` (see
       :doc:`../outputs/invpesilon`). Read-only: it changes no energy or state.

.. _screening-functions:

The four functions
==================

Except for ``exciton``, every function stops after writing its output. What each one writes depends on
the mode. All files are described in :doc:`../outputs/invpesilon`.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - ``# function``
     - Mode
     - Computes and writes
   * - ``dielectric``
     - ``2d``, ``q2d_legacy``, ``q2d_averaged``
     - :math:`\epsilon_{\bm{G}\bm{G}'}(\bm{q})` at ``# momentum``, written to ``<label>_epsilon.dat``. In
       ``q2d_averaged`` this is the inverse of the projected response :math:`M`, not an average of the
       microscopic dielectric function.
   * - ``polarizability``
     - ``2d``
     - :math:`\chi_{\bm{G}\bm{G}'}` for ``# vectors`` over the BZ mesh, written to
       ``polarizability_mesh.dat``.
   * -
     - ``q2d_legacy``
     - The polarizability matrix at ``# momentum``, written to ``<label>_polarizability.dat``.
   * -
     - ``q2d_averaged``
     - Not available.
   * - ``inversedielectric``
     - ``2d``, ``q2d_legacy``, ``q2d_averaged``
     - :math:`\epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})` at ``# momentum``, written to
       ``<label>_invepsilon.dat``. In ``q2d_averaged`` it holds the projected response :math:`M`, with
       :math:`\epsilon_M(\bm{q}) = 1/M_{00}(\bm{q})`.
   * - any of the three above
     - ``q2d_atomic``
     - The atomic-plane screening at ``# momentum``, written to ``<label>_q2d_atomic.dat``.
   * - ``exciton``
     - all
     - Screening on the whole BZ mesh, then the **exciton calculation** with the ``rpa`` potential.
       Writes ``kgrid_<ncells>.dat`` and, except in ``q2d_atomic``, ``<label>_invepsilon.dat`` on that
       mesh. In ``q2d_atomic`` the screened interaction is built internally and not written.
