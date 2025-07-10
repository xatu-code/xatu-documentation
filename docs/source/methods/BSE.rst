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

   \sum_{v',c',\mathbf{k}'} H_{vc,v'c'}(\mathbf{k},\mathbf{k}',Q) A^Q_{v'c'}(\mathbf{k}') = E_X A^Q_{vc}(\mathbf{k})

we define the interaction kernel and simplify the problem by transforming into the **Hartree-Fock (HF) band basis**. This incorporates self-energy corrections into the quasiparticle energies.

The resulting **working form of the BSE** solved in Xatu is:

.. math::

   \left( \varepsilon_{c,\mathbf{k+Q}} - \varepsilon_{v,\mathbf{k}} \right) A^Q_{vc}(\mathbf{k}) +
   \sum_{v',c',\mathbf{k}'} K_{vc,v'c'}(\mathbf{k}, \mathbf{k}', Q) A^Q_{v'c'}(\mathbf{k}') = E_X A^Q_{vc}(\mathbf{k})

where:

- \( \varepsilon_{n,\mathbf{k}} \) are the HF (or DFT/GW) quasiparticle energies
- \( A^Q_{vc}(\mathbf{k}) \) are the exciton amplitudes
- \( K = -(D - X) \) is the interaction kernel with:
  - \( D \): direct interaction between electron and hole
  - \( X \): exchange interaction (optional)

This is the **Tamm-Dancoff approximation (TDA)** form of the BSE.


Interaction Matrix Elements
=============================

The matrix elements are computed assuming point-like localized orbitals. For example, the direct term reads:

.. math::

   D_{vc,v'c'}(\mathbf{k}, \mathbf{k}', Q) =
   \sum_{ij,\alpha\beta} 
   C^{*}_{c,\mathbf{k+Q}}^{i\alpha} C^{*}_{v',\mathbf{k}'}^{j\beta}
   C_{c',\mathbf{k'+Q}}^{i\alpha} C_{v,\mathbf{k}}^{j\beta}
   \, V_{ij}(\mathbf{k}' - \mathbf{k})

Here, \( C_{n,\mathbf{k}}^{i\alpha} \) are the tight-binding coefficients and \( V_{ij} \) is the lattice-transformed interaction.

The exchange term is analogous and typically vanishes at \( Q = 0 \).

Solution Methods
=================

The BSE matrix is constructed and diagonalized using Armadillo linear algebra routines. For large systems, the following methods are available:

- **diag**: full diagonalization (default)
- **davidson**: iterative solver for low-lying states
- **sparse**: Lanczos-based sparse diagonalization

Output includes exciton energies, wavefunctions, real- and reciprocal-space densities, and optical matrix elements.

