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

* :math:`\varepsilon_{n,\bm{k}}` are the HF (or DFT/GW) quasiparticle energies
* :math:`A^{Q}_{vc}(\bm{k})` are the exciton amplitudes
* $ K = -(D - X) $ is the interaction kernel with:

  * $ D $ : direct interaction between electron and hole
  * $ X $ : exchange interaction (optional)

This is the **Tamm-Dancoff approximation (TDA)** form of the BSE.

Screened RPA Coulomb potential
==============================

If the user chose the `rpa` option for the interaction potential, then in the strict 2D approximation the screened Coulomb potential is also a matrix at each point in the Brillouin zone, whose elements are given by

.. math::
   W_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{v_c(\bm{q}+\bm{G})}\, \epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q}) \sqrt{v_c(\bm{q}+\bm{G}')} \,,

where :math:`\epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})` is the inverse RPA dielectric function computed within the strictly 2D approach (see :doc:`screening`). In the `q2d_legacy` mode, with the thickness :math:`d_{\perp}` of the material given in the screening input file, the screened potential is

.. math::
   \bar{W}_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{\bar{v}_c(\bm{q}+\bm{G})} \,\bar{\epsilon}^{-1}_{\bm{G}\bm{G}'}(\bm{q}) \sqrt{\bar{v}_c(\bm{q}+\bm{G}')} \,,

where :math:`\bar{\epsilon}^{-1}_{\bm{G}\bm{G}'}(\bm{q})` is the inverse RPA dielectric function computed within the quasi-2D approach, and :math:`\bar{v}_c` is given by

.. math::
   \bar{v}_c(\bm{q}) = \frac{1}{d_\perp^2} \int_{-d_{\perp}/2}^{d_{\perp}/2}  \int_{-d_{\perp}/2}^{d_{\perp}/2}  v_c(\bm{q}, z-z') \, \mathrm{d} z \, \mathrm{d} z'\,,

where :math:`v_c(\bm{q},z-z')` is the Coulomb potential in the mixed :math:`(\bm{q},z)`-representation. Formally, it is given by the in-plane Fourier transform of the unscreened real-space-resolved Coulomb potential :math:`V(\bm{r}-\bm{r}')`, while keeping the $z,z'$ variables intact.

In the `q2d_atomic` mode the screened interaction :math:`W_{\bm{G}a,\bm{G}'b}(\bm{q})` couples atomic planes :math:`a, b` (see :doc:`screening`). The direct term then contracts it with transition densities resolved by plane: for each :math:`\bm{G}`, the density of the electron-hole pair is summed over the orbitals of each plane, keeping their in-plane phases, and the kernel is

.. math::
   D = \frac{1}{N_k} \sum_{\bm{G}a,\bm{G}'b} \rho^{c\,*}_{\bm{G}a}\, W_{\bm{G}a,\bm{G}'b}(\bm{q})\, \rho^{v}_{\bm{G}'b}\,,

so that the interaction between charges on different planes is screened and weakened by their separation. In the `q2d_averaged` mode the BSE uses the doubly averaged :math:`\bar{W}_{\bm{G}\bm{G}'}(\bm{q})` directly, in place of the square-root form above.

Regularization of the :math:`\bm{q} = 0` term
=============================================

In reciprocal space the :math:`\bm{G} = \bm{G}' = 0` element of the interaction diverges at :math:`\bm{q} = 0`. Its contribution to the Brillouin-zone sum is replaced by the average of the screened potential over a small disk :math:`|\bm{q}| < q_0` around :math:`\Gamma`, with :math:`q_0 = \varsigma k_0` set by **# Percentage** in the exciton file. Near :math:`\Gamma` the screened potential of a 2D material takes the Rytova–Keldysh form :math:`W(q) = v_c(q)/(1 + r_0 q)`, for which the disk average is analytic:

.. math::
   W_{00}(0) = 2\, v_c(q_0)\, \frac{\ln(1 + x)}{x}\,, \qquad x = \epsilon(q_0) - 1\,,

where :math:`\epsilon(q_0) = 1 + r_0 q_0` is the ratio of the bare to the screened interaction at :math:`q_0`. To first order in :math:`x` this is :math:`(2 - x)\, v_c(q_0)`, the expression of Ref. [Ninhos2026]_; the exact form remains accurate when :math:`x` is not small, as happens for strongly screening or thick materials on coarse meshes. Every potential and screening mode uses this rule and differs only in how :math:`\epsilon(q_0)` is obtained:

.. list-table::
   :header-rows: 1

   * - Potential or mode
     - :math:`\epsilon(q_0)`
   * - `coulomb`
     - 1, so :math:`W_{00}(0) = 2 v_c(q_0)`
   * - `keldysh`
     - :math:`1 + r_0 q_0`
   * - `rpa`, `2d` and `q2d_legacy`
     - :math:`1/\epsilon^{-1}_{00}(q_0)`, averaged over :math:`\bm{q}_0` and the perpendicular direction for anisotropic systems
   * - `rpa`, `q2d_atomic`
     - bare over screened interaction at :math:`q_0`, summed over all pairs of atomic planes in the :math:`\bm{G} = 0` block
   * - `rpa`, `q2d_averaged`
     - doubly averaged bare over screened interaction at :math:`q_0`

The values of :math:`q_0`, :math:`v_c(q_0)`, :math:`\epsilon(q_0)`, :math:`x` and :math:`W_{00}(0)` are printed at run time.

Because the density factors reduce to overlaps at :math:`\bm{q} = 0`, this term adds :math:`-W_{00}(0)/N_k` times the identity to the BSE Hamiltonian: it shifts every exciton energy by the same amount and leaves splittings, wavefunctions and oscillator strengths unchanged. The shift vanishes as the mesh is refined, but including it makes the exciton energies converge much faster with the number of k points.

.. [Ninhos2026] P. Ninhos, A. J. Uría-Álvarez, C. Tserkezis, N. A. Mortensen and J. J. Palacios, *Microscopic screening theory for excitons in two-dimensional materials: A bridge between effective models and ab initio descriptions*, arXiv:2603.10966 (2026), Supporting Information, Eq. (S.21).


.. Interaction Matrix Elements
.. =============================

.. The matrix elements are computed assuming point-like localized orbitals. For example, the direct term reads:

.. .. math::

   .. D_{vc,v'c'}(\bm{k}, \bm{k}', \bm{Q}) = 
   .. \sum_{ij,\alpha\beta} 
   .. C^{i\alpha*}_{c,\bm{k} + \bm{Q}}^{} C^{*}_{v',\bm{k}'}^{j\beta}
   .. C_{c',\bm{k}'+\bm{Q}}^{i\alpha} C_{v,\bm{k}}^{j\beta}\, V_{ij}(\bm{k}' * \bm{k})

.. Here, :math:`C_{n,\bm{k}}^{i\alpha}` are the tight-binding coefficients and $V_{ij}$ is the lattice-transformed interaction.

.. The exchange term is analogous and typically vanishes at $Q = 0$ .

Solution Methods
=================

The BSE matrix is constructed and diagonalized using Armadillo linear algebra routines. For large systems, the following methods are available:

* **diag**: full diagonalization (default)
* **davidson**: iterative solver for low-lying states
* **sparse**: Lanczos-based sparse diagonalization

Output includes exciton energies, wavefunctions, real* and reciprocal-space densities, and optical matrix elements.

