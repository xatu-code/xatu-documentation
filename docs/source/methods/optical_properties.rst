===============================================
Optical Conductivity from Excitonic States
===============================================

Xatu can compute the linear optical conductivity using the excitonic states obtained from the BSE. The calculation is performed in the **independent-particle approximation (IPA)** or the **Bethe-Salpeter equation (BSE)** formalism, based on the eigenstates previously computed.

.. contents::
   :local:
   :depth: 2
   
General Expression
===================

The optical conductivity tensor is computed from the excitonic eigenstates and their coupling to the electromagnetic field, following the Kubo-Greenwood formalism.

The real part of the conductivity tensor $ \sigma_{ab}(\omega) $ is given by:

.. math::

   \sigma_{ab}(\omega) = \frac{\pi e^2 \hbar}{V} \sum_{\mathbf{k}}^{N_X} \frac{1}{E_{\mathbf{k}}}
   \left[ V_{\mathbf{k}}^a (V_{\mathbf{k}}^b)^* \right] \delta(\hbar\omega - E_{\mathbf{k}})

where:

- $ V $ is the system volume
- $ E_{\mathbf{k}} $ is the exciton energy at momentum $ \mathbf{k} $
- $ V_{\mathbf{k}}^a $ is the oscillator strength (current matrix element) in direction $ a $
- $ N_X $ is the number of computed exciton states
- The delta function is broadened numerically using a specified kernel

This expression is implemented directly in Xatu when the linear response spectrum is requested using the `-a` flag and a valid `kubo_w.in` file is provided.



Dipole Matrix Elements
========================

The key quantity is the matrix element of the current operator between the ground state and an exciton:

.. math::

   \langle 0 | j_\alpha | M \rangle = \sum_{v,c,\bm{k}} A^{M}_{vc}(\bm{k}) 
   \langle v,\bm{k} | j_\alpha | c,\bm{k} \rangle

Here, $A^{M}_{vc}(\bm{k})$ are the excitonic wavefunction coefficients in the electron-hole basis, and $\langle v | j | c \rangle$ are velocity matrix elements computed from the system Hamiltonian.


Excitonic Absorption Spectrum
===============================

The absorption spectrum is computed by convoluting the excitonic delta functions with a chosen broadening. The user can specify:

- Broadening type: `lorentzian`, `gaussian`, or `exponential`
- Broadening width (in eV)
- Frequency range and resolution

This is controlled by the `kubo_w.in` input file. The computed spectra include:

- **Independent-particle spectrum** (IPA)
- **Excitonic spectrum** (BSE)

Each output is saved to separate `.dat` files for plotting, with names defined in the exciton configuration file.

Reference
=========

For details, see:

`Efficient computation of optical excitations in two-dimensional materials with the Xatu code, Computer Physics Communications, 2024` <https://doi.org/10.1016/j.cpc.2023.109001>
