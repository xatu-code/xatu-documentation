============
Exciton file
============

The exciton file sets up the Bethe–Salpeter equation: the k-mesh, the bands, and the electron–hole
interaction. It uses the common syntax of :doc:`../input_files`, and every block holds a single line.

Minimal example:

.. code-block:: text

   # label
   hBN_N30
   # ncells
   30
   # bands
   1
   # dielectric
   1 1 10

Required blocks
===============

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Keyword
     - Content
   * - ``# label``
     - Name used for all output files (``<label>.eigval``, ``<label>.states``, …). Not strictly
       enforced, but without it the output files have no name.
   * - ``# ncells``
     - Number of k-points along each reciprocal lattice vector. The mesh has :math:`N^d` points in
       :math:`d` dimensions. This is the main convergence parameter.
   * - ``# bands``
     - Number of valence **and** of conduction bands closest to the gap: ``1`` uses the top valence and
       bottom conduction band. Either this or ``# bandlist`` is required.
   * - ``# bandlist``
     - Explicit list of bands, relative to the Fermi level: ``0`` is the highest valence band, ``-1``
       the one below; ``1`` is the lowest conduction band, ``2`` the next. E.g. ``-1 0 1 2``.
       Overrides ``# bands``.
   * - ``# dielectric``
     - Parameters of the Rytova–Keldysh potential: ``eps_s eps_m r0 [r0y [r0z]]``. These are the
       substrate and medium permittivities and the screening length :math:`r_0` in Å. Give up to
       three lengths for anisotropic screening; if only one is given,
       :math:`r_0^x = r_0^y = r_0^z`. Required even when another potential is used.

Interaction
===========

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Keyword
     - Content
   * - ``# potential``
     - Potential in the direct term of the kernel: ``keldysh`` *(default)*, ``coulomb``, or ``rpa``
       |scr|. ``rpa`` uses the numerical screened potential, and needs the reciprocal-space method and
       a screening file (``-z``).
   * - ``# exchange``
     - Include the exchange term: ``true`` or ``false`` *(default)*.
   * - ``# exchange.potential``
     - Potential used in the exchange term: ``keldysh`` *(default)* or ``coulomb``.
   * - ``# scissor``
     - Energy (eV) added to every electron–hole transition, i.e. a rigid band-gap correction. Default 0.
   * - ``# regularization``
     - Real-space method only. Distance :math:`a` used to remove the divergence at :math:`r=0` by
       setting :math:`V(0) = V(a)`. Defaults to the lattice parameter; only change it for supercells.

Real space or reciprocal space
------------------------------

By default the interaction matrix elements are computed in **real space**. Adding one of the keywords
below switches to the **reciprocal-space** method. The keyword differs between versions:

.. tab-set::

   .. tab-item:: w90 version

      ``# reciprocal``
         Integer ``nG``: the number of reciprocal-lattice cells summed over.

         .. code-block:: text

            # reciprocal
            3

   .. tab-item:: screening version

      ``# gcutoff``
         Real number: cutoff on :math:`|\bm{G}|` for the reciprocal-lattice vectors summed over. With
         ``rpa`` it can be smaller than the ``gcutoff`` of the screening file.

      ``# percentage``
         Regularization of the divergent :math:`\bm{q}=0` term. It is replaced by an average over a
         disk of radius :math:`q_0 = \varsigma k_0`, where :math:`\varsigma` is this value and
         :math:`k_0` the smallest wavevector of the mesh. Default ``0.5``; ``0`` drops the term.

         .. code-block:: text

            # gcutoff
            3.0
            # percentage
            0.5

k-mesh
======

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Keyword
     - Content
   * - ``# submesh``
     - Integer :math:`m`: mesh only a fraction :math:`1/m` of the Brillouin zone along each axis, with
       ``ncells`` points. It gives a finer mesh around a valley at the same cost. Memory grows as
       :math:`\mathcal{O}(m^d)`.
   * - ``# shift``
     - Centre of the (sub)mesh, ``kx ky kz`` (Å⁻¹). Use it with ``# submesh`` to centre on a valley.
   * - ``# totalmomentum``
     - Exciton centre-of-mass momentum :math:`\bm{Q}`, ``qx qy qz``. Default ``0 0 0`` (optical
       excitons).

.. note::

   ``# cutoff`` (real-space interaction cutoff) is read but not applied by the ``xatu`` binary, which
   always uses ``ncells/2.5``. Set it through the library with ``Exciton::setCutoff``.

Examples
========

Keldysh potential in real space, with exchange and a scissor correction:

.. code-block:: text

   # label
   MoS2
   # ncells
   60
   # bandlist
   -1 0 1 2
   # dielectric
   1 1 40
   # exchange
   true
   # scissor
   0.5

Reciprocal-space method with the RPA-screened potential |scr| (run with ``-z screening.txt``):

.. code-block:: text

   # label
   hBN_rpa
   # ncells
   20
   # bands
   1
   # dielectric
   1 1 10
   # potential
   rpa
   # gcutoff
   3.0
