===============================================
Optical Conductivity from Excitonic States
===============================================

Xatu can compute the linear optical conductivity using the excitonic states obtained from the BSE. The calculation is performed in the **independent-particle approximation (IPA)** or the **Bethe-Salpeter equation (BSE)** formalism, based on the eigenstates previously computed.

.. contents::
   :local:
   :depth: 2

General Expression
===================

The linear conductivity tensor is evaluated using the Kubo formula, in the dipole approximation. The general expression for the real part of the frequency-dependent conductivity reads:

.. math::

   \mathrm{Re}\,\sigma_{\alpha\beta}(\omega) = \frac{2\pi e^2}{\Omega} \sum_M \frac{f_M}{\omega_M} 
   \langle 0 | j_\alpha | M \rangle \langle M | j_\beta | 0 \rangle \delta(\omega - \omega_M)

where:

- \( \Omega \) is the system area
- \( \omega_M = E_M - E_0 \) is the excitation energy
- \( f_M \) is the oscillator strength of exciton \( M \)
- \( j_\alpha \) is the current operator in direction \( \alpha \)
- \( |0\rangle \) is the ground state
- \( |M\rangle \) is an exciton eigenstate

Dipole Matrix Elements
========================

The key quantity is the matrix element of the current operator between the ground state and an exciton:

.. math::

   \langle 0 | j_\alpha | M \rangle = \sum_{v,c,\mathbf{k}} A^{M}_{vc}(\mathbf{k}) 
   \langle v,\mathbf{k} | j_\alpha | c,\mathbf{k} \rangle

Here, \( A^{M}_{vc}(\mathbf{k}) \) are the excitonic wavefunction coefficients in the electron-hole basis, and \( \langle v | j | c \rangle \) are velocity matrix elements computed from the system Hamiltonian.


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

[Efficient computation of optical excitations in two-dimensional materials with the Xatu code, `Computer Physics Communications`, 2024](https://doi.org/10.1016/j.cpc.2023.109001)
