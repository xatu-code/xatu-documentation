====================
Optical conductivity
====================

With ``-a``, Xatu computes the linear optical conductivity from the Kubo formula. It does so twice: in
the **independent-particle approximation (IPA)**, from interband transitions, and with **excitons
(BSE)**, from transitions between the ground state and each exciton.

Excitonic conductivity
======================

The absorptive part of the conductivity tensor is

.. math::

   \sigma^{ab}(\omega) = \frac{\pi}{V N_{\bm{k}}} \sum_{X}
   \frac{(V^a_X)^*\,V^b_X}{E_X}\; \delta(\hbar\omega - E_X)
   \qquad (\text{atomic units}),

where

* :math:`V` is the unit-cell volume (area in 2D) and :math:`N_{\bm{k}}` the number of k-points;
* :math:`E_X` is the energy of exciton :math:`X`, and the sum runs over **all** excitons of the BSE;
* :math:`V^a_X = \langle GS|\hat v^a|X\rangle` is the velocity matrix element between the ground state
  and the exciton, written to :doc:`../outputs/oscillator_strengths`;
* the :math:`\delta` function is replaced by a Lorentzian, Gaussian or exponential of width
  :math:`\eta`, set in :doc:`../input_files/absorption`.

The exciton velocity matrix elements follow from the exciton coefficients and the single-particle
velocity matrix elements:

.. math::

   V^a_X = \sum_{vc\bm{k}} A^X_{vc}(\bm{k})\; v^a_{vc}(\bm{k}),
   \qquad
   v^a_{vc}(\bm{k}) = \frac{i}{\hbar}\langle v\bm{k}|[H_0, \hat r^a]|c\bm{k}\rangle .

Independent-particle conductivity
=================================

The IPA spectrum is the same formula, with excitons replaced by single electron–hole pairs
:math:`(v, c, \bm{k})` of energy :math:`\varepsilon_{c\bm{k}} - \varepsilon_{v\bm{k}}`. It always uses a
Lorentzian of width :math:`\eta`. Comparing the two spectra shows the effect of the electron–hole
interaction directly: the continuum is redistributed into exciton peaks below the gap.

Output
======

Both spectra, their imaginary parts and the oscillator strengths are written as described in
:doc:`../outputs/conductivity`. The conductivity is given in atomic units, i.e. :math:`e^2/\hbar` for
2D materials.

Reference
=========

A. J. Uría-Álvarez *et al.*, `Efficient computation of optical excitations in two-dimensional
materials with the Xatu code, Comput. Phys. Commun. 295, 109001 (2024)
<https://doi.org/10.1016/j.cpc.2023.109001>`_.
