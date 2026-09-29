=================
Output files
=================

Xatu always prints the exciton spectrum to the terminal. Files are only written when requested with a
flag. Every file goes to the working directory, and most are named after the ``# label`` of the
exciton file.

.. list-table::
   :header-rows: 1
   :widths: 30 14 56

   * - File
     - Flag
     - Content
   * - :doc:`<label>.eigval <eigval>`
     - ``-e``
     - Exciton energies (eV).
   * - :doc:`<label>.states <states>`
     - ``-c``
     - Electron–hole basis and exciton coefficients :math:`A_{vc}(\bm{k})`.
   * - :doc:`<label>.kwf <kwf>`
     - ``-k``
     - k-space probability density of each exciton.
   * - :doc:`<label>.rswf <rswf>`
     - ``-r``
     - Real-space probability density, with the hole fixed.
   * - :doc:`<label>.spin <spin>`
     - ``-s``
     - Total, electron and hole spin :math:`S_z` of each exciton.
   * - :doc:`*_sp.dat, *_ex.dat (+ _imag) <conductivity>`
     - ``-a``
     - Optical conductivity without and with excitons. Names set in ``kubo_w.in``.
   * - :doc:`*_ex_osc.dat <oscillator_strengths>`
     - ``-a``
     - Energies and velocity matrix elements of all excitons.
   * - :doc:`_invepsilon.dat and kgrid_*.dat <invpesilon>` |scr|
     - ``-z``
     - Inverse dielectric matrix and the k-mesh it is given on.
   * - ``<kpointsfile>.bands``
     - ``-b``
     - Band energies (eV) at each k-point of the input list, one row per k-point.

How many excitons are written
=============================

``-n`` (default 8) sets how many excitons appear in the terminal and in ``.eigval``, ``.states``,
``.kwf``, ``.rswf`` and ``.spin``. With ``-t <E>`` |w90|, the terminal, ``.eigval``, ``.states`` and
``.spin`` instead keep every exciton up to energy ``E``. The absorption spectrum and the oscillator
strengths always use **all** excitons of the BSE.

Units at a glance
=================

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Quantity
     - Unit
   * - Energies (exciton, photon)
     - eV
   * - k-points
     - Å⁻¹ (for model and Wannier90 input)
   * - Positions
     - Å
   * - Optical conductivity
     - :math:`e^2/\hbar` for 2D systems (atomic units)
   * - Spin
     - :math:`\hbar`

Plotting
========

The ``plot/`` folder of the Xatu repository contains Python scripts for the most common files:
``conductivity.py``, ``kwf.py`` and ``rswf.py``.
