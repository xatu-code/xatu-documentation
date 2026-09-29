===============================
Screening Potentials in Xatu
===============================

Xatu supports two real-space interaction potentials used in the Bethe-Salpeter Equation:

1. **Coulomb potential**
2. **Rytova–Keldysh potential**

These govern the electron–hole interaction and are used to build the interaction kernel.

Xatu also supports three interaction potentials in reciprocal space to compute the interaction matrix elements:

1. **Bare Coulomb potential**
2. **Rytova–Keldysh potential**
3. **Numerical RPA screened potential**

These potentials model the electron–hole interaction in momentum space through the 2D Fourier transform of the real-space potentials: Coulomb, Rytova–Keldysh and the screened potential with discrete translation symmetry. The numerical RPA potential can be computed in the strictly 2D limit or, for materials with a finite thickness, in one of three quasi-2D modes, selected with **# screening.mode** in the screening file (see :doc:`../input_files`).

.. contents::
   :local:
   :depth: 2

Coulomb Potential
===================

The standard Coulomb interaction in real space is defined as:

.. math::

   V(\bm{r}) = \frac{e^2}{4 \pi \varepsilon_0 |\bm{r}|}

In the implementation, this interaction is:

* Regularized at $r = 0$ using a small regularization parameter
* Truncated beyond a distance cutoff defined from the lattice parameter

This option is appropriate when long-range unscreened interactions are desired.

Rytova–Keldysh Potential
=========================

This model captures the effect of environmental screening in 2D materials. The potential reads:

.. math::

   V(r) = -\frac{e^2}{8 \varepsilon_0 \bar{\varepsilon} r_0} \left[ H_0\left(\frac{r}{r_0}\right) - Y_0\left(\frac{r}{r_0}\right) \right]

where:

* :math:`\bar{\varepsilon} = (\varepsilon_m + \varepsilon_s)/2` is the average surrounding dielectric between the medium :math:`\varepsilon_m` and substrate :math:`\varepsilon_s`
* $ r_0 $ is the effective screening length of the 2D material
* $ H_0 $ is the Struve function
* $ Y_0 $ is the Bessel function of the second kind

In practice:

* The interaction is regularized at $r = 0$
* A cutoff beyond which the interaction vanishes is applied
* The implementation may treat the screening radius **anisotropically**, i.e., using different $r_0$ values along different directions. This is an extension not typically found in the literature.

Anisotropic Screening
======================

Xatu supports anisotropic screening in the Rytova–Keldysh model by allowing directional dependence in the screening length. This is implemented by constructing an effective vector :math:`\bm{r}_0 = (r_{0}^{x}, r_{0}^{y}, r_{0}^{z})` , and rescaling the coordinates accordingly.

This allows the screening environment to be tuned independently along in-plane and out-of-plane directions -- a generalization that extends beyond conventional isotropic models.

Numerical RPA Screened Potential
=================================

Xatu can compute the microscopic RPA dielectric function

.. math::
   \epsilon_{\bm{G}\bm{G}'}(\bm{q}) = \delta_{\bm{G}\bm{G}'} - \sqrt{v_c(\bm{q}+\bm{G})} \chi^0_{\bm{G}\bm{G}'}(\bm{q}) \sqrt{v_c(\bm{q}+\bm{G}')}

in its symmetric form, where :math:`v_c(\bm{q})` is the 2D Fourier transform of the Coulomb potential given by

.. math::
   v_c(\bm{q}) = \frac{e}{2 \varepsilon_0 |\bm{q}|}\,,

and :math:`\chi^0` is the independent-particle polarizability (or the irreducible polarizability within RPA), which for gapped time-reversal symmetric systems is given by

.. math::
   \chi^0_{\bm{G}\bm{G}'}(\bm{q}) = \frac{2}{A}  \sum_{vc,\bm{k} \sigma} \frac{\langle c,\bm{k}| e^{-i(\bm{q}+\bm{G})\cdot\bm{r}}|v,\bm{k}+\bm{q}\rangle  \langle v,\bm{k}+\bm{q}| e^{i(\bm{q}+\bm{G}')\cdot\bm{r}}|c,\bm{k}\rangle^*}{\epsilon_{v,\bm{k} + \bm{q}} - \epsilon_{c,\bm{k}} }\,.

The matrix elements in the sum are computed for Bloch states written within the linear combination of atomic orbitals (LCAO) approximation and in the point-like orbital approximation. This is the `2d` screening mode.

Quasi-2D Screening
==================

A real 2D material has a finite thickness, and its atoms may sit at different heights :math:`z`. In the mixed :math:`(\bm{q}, z)` representation the bare Coulomb interaction is

.. math::
   v_c(\bm{q}, z - z') = v_c(\bm{q})\, e^{-|\bm{q}| |z - z'|}\,,

which reduces to :math:`v_c(\bm{q})` only when all charges lie in one plane. Xatu offers three ways of keeping this dependence.

Thickness-averaged screening (`q2d_legacy`)
-------------------------------------------

The material is treated as a slab of thickness :math:`d_\perp`, given in the screening file. The Coulomb interaction is averaged over both coordinates across the slab,

.. math::
   \bar{v}_c(\bm{q}) = \frac{1}{d_\perp^2} \int_{-d_\perp/2}^{d_\perp/2} \int_{-d_\perp/2}^{d_\perp/2} v_c(\bm{q}, z - z') \, \mathrm{d} z \, \mathrm{d} z'\,,

and the symmetric quasi-2D dielectric matrix :math:`\bar{\epsilon}_{\bm{G}\bm{G}'}(\bm{q})` is built from it. The result depends on the chosen :math:`d_\perp`.

Atomic-plane screening (`q2d_atomic`)
-------------------------------------

Within the point-like orbital approximation, the induced charge sits on the atoms. Grouping the atoms by height gives a set of atomic planes :math:`z_a`, and the response can be solved exactly on them, with no thickness parameter and no discretization in :math:`z`. Matrices are indexed by the pair :math:`(\bm{G}, a)` and are diagonal in :math:`\bm{G}` for the bare interaction:

.. math::
   B_{\bm{G}a,\bm{G}'b}(\bm{q}) = \delta_{\bm{G}\bm{G}'}\, v_c(\bm{q}+\bm{G})\, e^{-|\bm{q}+\bm{G}| |z_a - z_b|}\,.

The point-density susceptibility :math:`P_{\bm{G}a,\bm{G}'b}(\bm{q})` is the polarizability above with each transition density summed over the orbitals of plane :math:`a` (and :math:`b`), keeping their in-plane phases. The RPA Dyson equation is then solved on the planes,

.. math::
   R = (I - P B)^{-1} P\,, \qquad W = B + B R B\,,

where :math:`R` is the screened density response and :math:`W_{\bm{G}a,\bm{G}'b}(\bm{q})` the screened interaction between planes. :math:`W` is what the BSE contracts with the transition densities of each plane (see :doc:`BSE`). The screened interaction at any heights follows from :math:`R` as :math:`W(z, z') = v_c(z, z') + A(z) R A^T(z')`, with :math:`A(z)` the bare kernel from height :math:`z` to the planes. For a single atomic plane this mode reproduces the `2d` mode.

Averaged atomic-plane screening (`q2d_averaged`)
------------------------------------------------

This mode keeps the full `q2d_atomic` response through the inversion, and only then averages it uniformly in :math:`z` over an interval :math:`[z_\mathrm{lo}, z_\mathrm{hi}]`: by default the extent of the atomic planes, which **# zaverage.margin**, **# zaverage.zmin** and **# zaverage.zmax** can widen or replace. Averaging after the inversion is not the same as averaging the dielectric matrix and then inverting it.

With :math:`J_{\bm{G},\bm{G}'a} = \delta_{\bm{G}\bm{G}'} \frac{1}{z_\mathrm{hi} - z_\mathrm{lo}} \int_{z_\mathrm{lo}}^{z_\mathrm{hi}} B_{\bm{G}}(z, z_a)\, \mathrm{d}z` the bare kernel from a plane to the averaged coordinate, and :math:`T` the matrix that applies a :math:`z`-uniform potential to every plane, the response to a uniform external potential is

.. math::
   M(\bm{q}) = I + J R T\,, \qquad \epsilon_M(\bm{q}) = \frac{1}{M_{00}(\bm{q})}\,,

which is what the `inversedielectric` function writes. The BSE uses instead the screened interaction with both coordinates averaged,

.. math::
   \bar{W}(\bm{q}) = \bar{V}(\bm{q}) + J R J^\dagger\,,

where :math:`\bar{V}` is the doubly averaged bare interaction. The result depends on the averaging interval.

Example: macroscopic dielectric function of hBN
===============================================

To illustrate the new functionalities, we show below the macroscopic dielectric function of monolayer hBN computed with our implementation, and explain to the user how they can obtain it themselves.

.. note::

   📄 **Reference Paper:**   
   `Microscopic screening theory for excitons in two-dimensional materials: A bridge between effective models and ab initio descriptions, arxiv 2603.10966 <https://arxiv.org/abs/2603.10966>`_

.. image:: ../images/epsilon_vs_q_hBN.jpg
   :width: 75%
   :align: center

The continuous black curve above was obtained in Phys. Rev. B 92, 245123 (2015), while the dashed black one was obtained using the QEH package for Python from Nano Lett. 2015, 15, 7, 4616-462.

With the script called ``write_screening.cpp`` in the main folder and using the CRYSTAL model file `hBN_base_HSE06.outp` for monolayer hBN with the HSE06 functional, included among the models provided with Xatu, we obtain the red and blue curves with the new screening functionalities.
The script is compiled like any other in the main folder (``make write_screening``). To run it, execute the following command in the terminal:

.. code-block:: bash

   ./write_screening ../examples/material_models/DFT/hBN_base_HSE06.outp ../examples/excitonconfig/hBN_reciprocal.txt ../examples/screeningconfig/hBN_DFT_screening.txt <name_of_q_points_file>.dat

similarly to the command-line usage of the `xatu` binary (but without any flags), and providing the name of the input file containing the list of q-points at the end of the command. Such a file is already provided in the data folder, `hBN_DFT_HSE06_Gamma_K_q_points.dat`. The exciton file must contain the **# Gcutoff** block, which selects the reciprocal-space method.

The method which reads the input file containing the list of q-points and computes the dielectric matrix accordingly is called ``ExcitonTB::compute_2D_DielectricMatrix(file_name)``, which can be identified in the script.
The screening file selects the model: with the default `2d` mode the strictly 2D dielectric matrix is computed, and with **# screening.mode** set to `q2d_legacy` and a finite **# thickness** the quasi-2D one. With **# function** set to `dielectric` the script writes the dielectric matrix at each q-point to `<name_of_q_points_file>_epsilon.dat`; with `inversedielectric` it writes its inverse to `<name_of_q_points_file>_invepsilon.dat`, from which :math:`\epsilon_M(\bm{q}) = 1/\epsilon^{-1}_{00}(\bm{q})`. Both files have the layout described in :doc:`../outputs/invepsilon`.

