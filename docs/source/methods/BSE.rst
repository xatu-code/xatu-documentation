====================================
Bethe-Salpeter Equation in Xatu
====================================

The Bethe-Salpeter Equation (BSE) governs the formation of excitons in semiconductors and insulators. Xatu solves the BSE using localized orbitals and static screened interactions.

.. contents::
   :local:
   :depth: 2

BSE Formalism
==============

Starting from the full interacting Hamiltonian projected onto electron-hole pairs:

.. math::

   \sum_{v',c',\bm{k}'} H_{vc,v'c'}(\bm{k},\bm{k}',Q) A^Q_{v'c'}(\bm{k}') = E_X A^Q_{vc}(\bm{k})

we define the interaction kernel and simplify the problem by transforming into the **Hartree-Fock (HF) band basis**. This incorporates self-energy corrections into the quasiparticle energies.

The resulting **working form of the BSE** solved in Xatu is:

.. math::

   \left( \varepsilon_{c,\bm{k+Q}} - \varepsilon_{v,\bm{k}} \right) A^Q_{vc}(\bm{k}) +
   \sum_{v',c',\bm{k}'} K_{vc,v'c'}(\bm{k}, \bm{k}', Q) A^Q_{v'c'}(\bm{k}') = E_X A^Q_{vc}(\bm{k})

where:

* :math:`\varepsilon_{n,\mathbf{k}}` are the HF (or DFT/GW) quasiparticle energies
* :math:`A^{Q}_{vc}(\mathbf{k})` are the exciton amplitudes
* $ K = -(D - X) $ is the interaction kernel with:

  * $ D $ : direct interaction between electron and hole
  * $ X $ : exchange interaction (optional)

This is the **Tamm-Dancoff approximation (TDA)** form of the BSE.

Screened RPA Coulomb potential
==============================

If the user chose the `rpa` option for the interaction potential, then in the strict 2D approximation the screened Coulomb potential is also a matrix at each point in the Brillouin zone, whose elements are given by

.. math::
   W_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{v_c(\bm{q}+\bm{G})}\, \epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q}) \sqrt{v_c(\bm{q}+\bm{G}')} \,,

where :math:`\epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})` is the inverse RPA dielectric function computed within the strictly 2D approach. If the user provides the thickness :math:`d_{\perp}` of the 2D material in the screening input file, then the quasi-2D mode (Q2D) is enabled, and the screened potential is given by

.. math::
   \bar{W}_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{\bar{v}_c(\bm{q}+\bm{G})} \,\bar{\epsilon}^{-1}_{\bm{G}\bm{G}'}(\bm{q}) \sqrt{\bar{v}_c(\bm{q}+\bm{G}')} \,,

where :math:`\bar{\epsilon}^{-1}_{\bm{G}\bm{G}'}(\bm{q})` is the inverse RPA dielectric function computed within the Q2D approach, and :math:`\bar{v}_c` is given by

.. math::
   \bar{v}_c(\bm{q}) = \int_{-d_{\perp}/2}^{d_{\perp}/2}  \int_{-d_{\perp}/2}^{d_{\perp}/2}  v_c(\bm{q}, z-z') \, \mathrm{d} z \, \mathrm{d} z'\,,

where :math:`v_c(\bm{q},z-z')` is the Coulomb potential in the mixed :math:`(\bm{q},z)`-representation. Formally, it is given by the in-plane Fourier transform of the unscreened real-space-resolved Coulomb potential :math:`V(\bm{r}-\bm{r}')`, while keeping the $z,z'$ variables intact.

.. Interaction Matrix Elements
.. =============================

.. The matrix elements are computed assuming point-like localized orbitals. For example, the direct term reads:

.. .. math::

   .. D_{vc,v'c'}(\mathbf{k}, \mathbf{k}', \mathbf{Q}) = 
   .. \sum_{ij,\alpha\beta} 
   .. C^{i\alpha*}_{c,\mathbf{k} + \mathbf{Q}}^{} C^{*}_{v',\mathbf{k}'}^{j\beta}
   .. C_{c',\mathbf{k}'+\mathbf{Q}}^{i\alpha} C_{v,\mathbf{k}}^{j\beta}\, V_{ij}(\mathbf{k}' * \mathbf{k})

.. Here, :math:`C_{n,\mathbf{k}}^{i\alpha}` are the tight-binding coefficients and $V_{ij}$ is the lattice-transformed interaction.

.. The exchange term is analogous and typically vanishes at $Q = 0$ .

Solution Methods
=================

The BSE matrix is constructed and diagonalized using Armadillo linear algebra routines. For large systems, the following methods are available:

* **diag**: full diagonalization (default)
* **davidson**: iterative solver for low-lying states
* **sparse**: Lanczos-based sparse diagonalization

Output includes exciton energies, wavefunctions, real* and reciprocal-space densities, and optical matrix elements.

