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

   \left( \varepsilon_{c,\bm{k+Q}} * \varepsilon_{v,\bm{k}} \right) A^Q_{vc}(\bm{k}) +
   \sum_{v',c',\bm{k}'} K_{vc,v'c'}(\bm{k}, \bm{k}', Q) A^Q_{v'c'}(\bm{k}') = E_X A^Q_{vc}(\bm{k})

where:

* :math:`\varepsilon_{n,\mathbf{k}}` are the HF (or DFT/GW) quasiparticle energies
* :math:`A^{Q}_{vc}(\mathbf{k})` are the exciton amplitudes
* $ K = -(D - X) $ is the interaction kernel with:

  * $ D $ : direct interaction between electron and hole
  * $ X $ : exchange interaction (optional)

This is the **Tamm-Dancoff approximation (TDA)** form of the BSE.


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

