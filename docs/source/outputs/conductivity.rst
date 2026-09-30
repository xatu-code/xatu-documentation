====================================
Optical conductivity (``-a``)
====================================

With ``-a``, Xatu computes the linear optical conductivity :math:`\sigma^{ab}(\omega)` in the
independent-particle approximation (IPA) and with excitons (BSE), following
:doc:`../methods/optical_properties`. The frequency grid, broadening and file names come from
:doc:`../input_files/absorption`.

Files
=====

For output names ``hBN_sp.dat`` and ``hBN_ex.dat`` in ``kubo_w.in``:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File
     - Content
   * - ``hBN_sp.dat``
     - :math:`\mathrm{Re}\,\sigma^{ab}(\omega)`, independent particles.
   * - ``hBN_ex.dat``
     - :math:`\mathrm{Re}\,\sigma^{ab}(\omega)`, with excitons.
   * - ``hBN_sp_imag.dat``, ``hBN_ex_imag.dat``
     - The corresponding imaginary parts (same layout).
   * - ``hBN_ex_osc.dat``
     - Exciton energies and velocity matrix elements, see :doc:`oscillator_strengths`.

Format
======

One row per frequency, ten columns:

.. code-block:: text

   omega   xx   xy   xz   yx   yy   yz   zx   zy   zz

* ``omega``: photon energy :math:`\hbar\omega` (eV).
* ``ab``: component :math:`\sigma^{ab}`, in atomic units. For a 2D material this is the sheet
  conductivity in units of :math:`e^2/\hbar` (:math:`\approx 2.43\times10^{-4}` S).

What the real and imaginary files contain
-----------------------------------------

The two spectra are not built the same way:

.. list-table::
   :header-rows: 1
   :widths: 18 41 41

   * -
     - ``*_sp.dat`` (IPA)
     - ``*_ex.dat`` (BSE)
   * - Broadening
     - **Always Lorentzian** of width :math:`\eta`, whatever ``kubo_w.in`` says.
     - The type chosen in ``kubo_w.in``.
   * - Real file
     - Absorptive part, :math:`\mathrm{Re}\,\sigma^{ab}`.
     - Absorptive part, :math:`\mathrm{Re}\,\sigma^{ab}`.
   * - ``_imag`` file
     - Imaginary part of the transition strengths :math:`v^a_{cv}v^b_{vc}` times the (real) line shape.
       Zero on the diagonal; non-zero off-diagonal only when time-reversal symmetry is broken.
     - With ``lorentzian``: the dispersive part of the resonant terms,
       :math:`\propto (\hbar\omega - E_X)/[(\hbar\omega-E_X)^2+\eta^2]`. With ``gaussian`` or
       ``exponential``: zero.

.. warning::

   Neither ``_imag`` file is a full Kramers–Kronig partner of the real part: anti-resonant terms and
   transitions outside the band window are missing. To compare IPA and BSE spectra line by line, use
   ``lorentzian`` so both share the same line shape.

Absorbance
==========

For a freestanding 2D layer at normal incidence, the absorbance for light polarized along :math:`a` is,
to lowest order,

.. math::

   A(\omega) = \frac{4\pi}{c}\,\mathrm{Re}\,\sigma^{aa}(\omega) \qquad (c \approx 137.036 \text{ in atomic units}).

.. code-block:: python

   import numpy as np
   ex = np.loadtxt("hBN_ex.dat")
   absorbance_x = 4 * np.pi / 137.035999 * ex[:, 1]

See the :doc:`../quickstart` for a full example, and ``plot/conductivity.py`` in the repository for a
plotting script.
