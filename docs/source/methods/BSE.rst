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

Self-energy correction
----------------------

With ``# selfenergy true``, the band energies entering the BSE are corrected by a self-energy computed
from the same model interaction (``# selfenergy.potential``):

.. math::

   \varepsilon_{n,\bm{k}} \;\to\; \varepsilon_{n,\bm{k}} + \Sigma_n(\bm{k}) .

:math:`\Sigma_n(\bm{k})` is a Hartree–Fock-type term: a direct (Hartree) contribution minus an
exchange contribution, summed over the valence bands of the window and the k-mesh. It follows Eqs.
(2.10)–(2.12) of `arXiv:2510.25009 <https://arxiv.org/abs/2510.25009>`_. It is available for the
real-space method, and can be written to :doc:`../outputs/selfenergy` with ``-i``.

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
   The potential is summed over reciprocal-lattice vectors :math:`\bm{G}` with
   :math:`|\bm{G}|` below ``# gcutoff``, which enables this method (see
   :doc:`../input_files/exciton`).

Screened RPA potential
----------------------

With ``# potential rpa``, the direct term uses the numerical RPA screening (see :doc:`screening`). In the
``2d`` mode the screened Coulomb potential is a matrix at each :math:`\bm{q}` of the Brillouin zone:

.. math::

   W_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{v_c(\bm{q}+\bm{G})}\;
   \epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})\;
   \sqrt{v_c(\bm{q}+\bm{G}')} .

In the ``q2d_legacy`` mode the same form holds with the slab-averaged Coulomb potential
:math:`\bar{v}_c` and dielectric matrix :math:`\bar{\epsilon}^{-1}`:

.. math::

   \bar{W}_{\bm{G}\bm{G}'}(\bm{q}) = \sqrt{\bar{v}_c(\bm{q}+\bm{G})}\;
   \bar{\epsilon}^{-1}_{\bm{G}\bm{G}'}(\bm{q})\;
   \sqrt{\bar{v}_c(\bm{q}+\bm{G}')} .

In the ``q2d_atomic`` mode the screened interaction :math:`W_{\bm{G}a,\bm{G}'b}(\bm{q})` couples atomic
planes :math:`a, b`. The direct term contracts it with transition densities resolved by plane: for each
:math:`\bm{G}`, the density of the electron–hole pair is summed over the orbitals of each plane, keeping
their in-plane phases:

.. math::

   D = \frac{1}{N_{\bm{k}}} \sum_{\bm{G}a,\bm{G}'b} \rho^{c\,*}_{\bm{G}a}\,
   W_{\bm{G}a,\bm{G}'b}(\bm{q})\, \rho^{v}_{\bm{G}'b} .

The interaction between charges on different planes is thus screened and weakened by their separation.
In the ``q2d_averaged`` mode the BSE uses the doubly averaged :math:`\bar{W}_{\bm{G}\bm{G}'}(\bm{q})`
directly, in place of the square-root form.

Regularization of the :math:`\bm{q} = 0` term
---------------------------------------------

In reciprocal space the :math:`\bm{G} = \bm{G}' = 0` element of the interaction diverges at
:math:`\bm{q} = 0`. Its contribution to the Brillouin-zone sum is replaced by the average of the screened
potential over a small disk :math:`|\bm{q}| < q_0` around :math:`\Gamma`, with :math:`q_0 = \varsigma k_0`
set by ``# percentage``. Near :math:`\Gamma` the screened potential of a 2D material takes the
Rytova–Keldysh form :math:`W(q) = v_c(q)/(1 + r_0 q)`, for which the disk average is analytic:

.. math::

   W_{00}(0) = 2\, v_c(q_0)\, \frac{\ln(1 + x)}{x} , \qquad x = \epsilon(q_0) - 1 ,

where :math:`\epsilon(q_0) = 1 + r_0 q_0` is the ratio of the bare to the screened interaction at
:math:`q_0`. To first order in :math:`x` this is :math:`(2 - x)\, v_c(q_0)`, the expression of Ninhos
*et al.* (arXiv:2603.10966, Supporting Information, Eq. S.21). The exact form stays accurate when
:math:`x` is not small, as for strongly screening or thick materials on coarse meshes. Every potential
and screening mode uses this rule, and they differ only in how :math:`\epsilon(q_0)` is obtained:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Potential or mode
     - :math:`\epsilon(q_0)`
   * - ``coulomb``
     - 1, so :math:`W_{00}(0) = 2 v_c(q_0)`
   * - ``keldysh``
     - :math:`1 + r_0 q_0`
   * - ``rpa``, ``2d`` and ``q2d_legacy``
     - :math:`1/\epsilon^{-1}_{00}(q_0)`, averaged over :math:`\bm{q}_0` and the perpendicular direction
       for anisotropic systems
   * - ``rpa``, ``q2d_atomic``
     - bare over screened interaction at :math:`q_0`, summed over all pairs of atomic planes in the
       :math:`\bm{G} = 0` block
   * - ``rpa``, ``q2d_averaged``
     - doubly averaged bare over screened interaction at :math:`q_0`

The values of :math:`q_0`, :math:`v_c(q_0)`, :math:`\epsilon(q_0)`, :math:`x` and :math:`W_{00}(0)`
are printed at run time.

Because the density factors reduce to overlaps at :math:`\bm{q} = 0`, this term adds
:math:`-W_{00}(0)/N_{\bm{k}}` times the identity to the BSE Hamiltonian. It shifts every exciton energy by
the same amount and leaves splittings, wavefunctions and oscillator strengths unchanged. The shift
vanishes as the mesh is refined, but including it makes the exciton energies converge much faster with
the number of k-points.

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
