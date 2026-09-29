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

These potentials model the electron–hole interaction in momentum space through the 2D Fourier transform of the real-space potentials: Coulomb, Rytova–Keldysh and the screened potential with discrete translation symmetry.

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

Xatu supports anisotropic screening in the Rytova–Keldysh model by allowing directional dependence in the screening length. This is implemented by constructing an effective vector :math:`\mathbf{r}_0 = (r_{0}^{x}, r_{0}^{y}, r_{0}^{z})` , and rescaling the coordinates accordingly.

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


The matrix elements in the sum are computed for Bloch states written within the linear combination of atomic orbitals (LCAO) approximation and in the point-like orbital approximation.

If the thickness :math:`d_{\perp}` is provided in the screening input file, then the dielectric function to be computed is the symmetric quasi-2D one :math:`\bar{\epsilon}_{\bm{G} \bm{G}'} (\bm{q})`.

To illustrate the new functionalities, we show below the macroscopic dielectric function of monolayer hBN computed with our implementation, and explain to the user how they can obtain it themselves.

.. note::

   📄 **Reference Paper:**   
   `Microscopic screening theory for excitons in two-dimensional materials: A bridge between effective models and ab initio descriptions, arxiv 2603.10966 <https://arxiv.org/abs/2603.10966>`_

.. image:: ../images/epsilon_vs_q_hBN.jpg
   :width: 75%
   :align: center

The continuous black curve above was obtained in Phys. Rev. B 92, 245123 (2015), while the dashed black one was obtained using the QEH package for Python from Nano Lett. 2015, 15, 7, 4616-462.

With the script called ``write_screening.cpp`` in the main folder and using the CRYSTAL model file `hBN_base_HSE0.outp` for monolayer hBN with the HSE06 functional, included among the models provided with Xatu, we obtain the red and blue curves with the new screening functionalities.
The script can be compiled like any other in the main folder. To run it, execute the following command in the terminal:

.. code-block:: bash

   ./write_screening ../examples/material_models/DFT/hBN_base_HSE06.outp ../examples/excitonconfig/hBN_test.txt ../examples/screeningconfig/hBN_DFT_screening.txt <name_of_q_points_file>.dat

similarly to the command-line usage of the `xatu` binary  (but without any flags), and providing the name of the input file containing the list of q-points at the end of the command. Such a file is already provided in the data folder.

The method which reads the input file containing the list of q-points and computes the dielectric matrix accordingly is called ``ExcitonTB::compute_2D_DielectricMatrix(file_name)``, which can be identified in the script.
To enable the Q2D calculation, a finite value for the thickness parameter must be provided in the screening input file, as mentioned above.
After concluding the computation, the file containing the inverse dielectric matrix at each q-point is created, analogously to when running the `xatu` binary to compute the exciton using the RPA screened Coulomb potential (see the previous section).