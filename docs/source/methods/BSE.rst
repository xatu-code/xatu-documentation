=============================
The Bethe–Salpeter equation
=============================

The Bethe–Salpeter equation (BSE) describes excitons, the bound electron–hole pairs of semiconductors
and insulators. Xatu solves it in a basis of localized orbitals, with a static screened interaction.

Excitons as electron–hole pairs
===============================

An exciton of centre-of-mass momentum :math:`\bm{Q}` is written as a superposition of electron–hole
pairs, with an electron in conduction band :math:`c` at :math:`\bm{k}+\bm{Q}` and a hole in valence
band :math:`v` at :math:`\bm{k}`:

.. math::

   |X\rangle = \sum_{v,c,\bm{k}} A^{\bm{Q}}_{vc}(\bm{k})\;
   c^\dagger_{c,\bm{k}+\bm{Q}}\, c_{v,\bm{k}}\, |GS\rangle .

Projecting the interacting Hamiltonian onto these pairs gives an eigenvalue problem for the coefficients
:math:`A^{\bm{Q}}_{vc}(\bm{k})`:

.. math::

   \sum_{v',c',\bm{k}'} H_{vc,v'c'}(\bm{k},\bm{k}',\bm{Q})\, A^{\bm{Q}}_{v'c'}(\bm{k}') = E_X\, A^{\bm{Q}}_{vc}(\bm{k}) .

Working in the band basis of a mean-field Hamiltonian (Hartree–Fock, DFT or tight-binding) absorbs the
self-energy corrections into the quasiparticle energies. The equation Xatu solves is then

.. math::

   \left( \varepsilon_{c,\bm{k}+\bm{Q}} - \varepsilon_{v,\bm{k}} \right) A^{\bm{Q}}_{vc}(\bm{k})
   + \sum_{v',c',\bm{k}'} K_{vc,v'c'}(\bm{k}, \bm{k}', \bm{Q})\, A^{\bm{Q}}_{v'c'}(\bm{k}')
   = E_X\, A^{\bm{Q}}_{vc}(\bm{k}),

where

* :math:`\varepsilon_{n,\bm{k}}` are the quasiparticle band energies (plus the optional
  ``# scissor``);
* :math:`A^{\bm{Q}}_{vc}(\bm{k})` are the exciton coefficients, written to :doc:`../outputs/states`;
* :math:`K = -(D - X)` is the interaction kernel, with the **direct** term :math:`D` (screened
  electron–hole attraction) and the optional **exchange** term :math:`X` (``# exchange``).

This is the **Tamm–Dancoff approximation**: coupling between resonant and anti-resonant pairs is
neglected.

The size of the problem, the **BSE dimension**, is
:math:`N_v \times N_c \times N_{\bm{k}}`: bands from ``# bands``/``# bandlist``, and k-points
:math:`N_{\bm{k}} =` ``ncells``:math:`^d`.

Interaction matrix elements
===========================

The kernel is built from the electron–hole interaction potential chosen with ``# potential`` (see
:doc:`screening`). The matrix elements can be computed in two ways:

Real space *(default)*
   The potential is evaluated between orbitals of the lattice, treated as point-like charges at their
   centres. The divergence at :math:`r=0` is removed with ``# regularization``.

Reciprocal space
   The potential is summed over reciprocal-lattice vectors :math:`\bm{G}`. Enabled with
   ``# reciprocal`` |w90| or ``# gcutoff`` |scr| (see :doc:`../input_files/exciton`).

Screened RPA potential
----------------------

|scr|

With ``# potential rpa``, the direct term uses the numerical RPA screening. In the strictly 2D
approach, the screened Coulomb potential is a matrix at each :math:`\bm{q}` of the Brillouin zone:

.. math::

   W_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{v_c(\bm{q}+\bm{G})}\;
   \epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})\;
   \sqrt{v_c(\bm{q}+\bm{G}')} ,

where :math:`\epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})` is the inverse RPA dielectric matrix of
:doc:`screening`.

If a thickness :math:`d_\perp` is given in the screening file, the quasi-2D (Q2D) mode is used
instead:

.. math::

   \bar{W}_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{\bar{v}_c(\bm{q}+\bm{G})}\;
   \bar{\epsilon}^{-1}_{\bm{G}\bm{G}'}(\bm{q})\;
   \sqrt{\bar{v}_c(\bm{q}+\bm{G}')} ,

with the Coulomb potential averaged over the thickness of the layer,

.. math::

   \bar{v}_c(\bm{q}) = \int_{-d_{\perp}/2}^{d_{\perp}/2} \int_{-d_{\perp}/2}^{d_{\perp}/2}
   v_c(\bm{q}, z-z')\, \mathrm{d}z\, \mathrm{d}z' .

Here :math:`v_c(\bm{q}, z-z')` is the Coulomb potential in the mixed :math:`(\bm{q}, z)`
representation: the in-plane Fourier transform of :math:`V(\bm{r}-\bm{r}')`, keeping :math:`z` and
:math:`z'`.

Solving the BSE
===============

The BSE matrix is Hermitian. It is built and diagonalized with Armadillo; the solver is chosen with
``-m``:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``-m``
     - Method
   * - ``diag``
     - Full diagonalization *(default)*. All states; memory and time grow fast with the BSE dimension.
   * - ``davidson``
     - Iterative Davidson solver for the lowest ``-n`` states.
   * - ``sparse``
     - Lanczos-based sparse diagonalization (ARPACK) for the lowest ``-n`` states.

From the solution, Xatu derives the energies, wavefunctions in real and reciprocal space, spin, and
optical matrix elements (see :doc:`../outputs/overview`).
