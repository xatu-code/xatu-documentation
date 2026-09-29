=====================================
Absorption file (``kubo_w.in``)
=====================================

The optical conductivity (``-a``) is controlled by a file that **must be called** ``kubo_w.in`` and sit
in the directory where Xatu runs.

.. code-block:: text

   #initial frequency (eV)
   4
   #frequency range (eV)
   4
   #number of frequency points (integer)
   400
   #broadening parameter (eV)
   0.05
   #type of broadening (available: 'lorentzian', 'exponential', 'gaussian')
   lorentzian
   #output kubo name files
   hBN_sp.dat
   hBN_ex.dat

Unlike the other input files, this one is read **by position**. Each value must follow its comment line,
in exactly this order. The comment text itself does not matter.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Entry
     - Meaning
   * - initial frequency
     - First photon energy :math:`\omega_0` (eV).
   * - frequency range
     - Width :math:`\Delta` of the energy window (eV).
   * - number of frequency points
     - :math:`n_\omega`. The grid is :math:`\omega_i = \omega_0 + (i-1)\,\Delta/n_\omega`, so it ends
       one step before :math:`\omega_0+\Delta`.
   * - broadening parameter
     - Width :math:`\eta` of the broadening function (eV).
   * - type of broadening
     - ``lorentzian``, ``gaussian`` or ``exponential``. Applies to the excitonic spectrum only: the
       independent-particle spectrum always uses a Lorentzian.
   * - output file names
     - Two lines: the independent-particle and the excitonic spectrum files.

From the two file names, Xatu derives three more by inserting ``_imag`` or ``_osc`` before the
extension. For the example above it writes ``hBN_sp.dat``, ``hBN_ex.dat``, ``hBN_sp_imag.dat``,
``hBN_ex_imag.dat`` and ``hBN_ex_osc.dat`` (see :doc:`../outputs/conductivity`).

.. note::

   |w90| If ``kubo_w.in`` is missing, the w90 version prints a warning, skips the spectra, and still
   writes the oscillator strengths to ``kubo_ex_osc.dat``. Other versions stop with an error.
