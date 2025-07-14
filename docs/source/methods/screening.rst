===============================
Screening Potentials in Xatu
===============================

Xatu supports two real-space interaction potentials used in the Bethe-Salpeter Equation:

1. **Coulomb potential**
2. **Rytova–Keldysh potential**

These govern the electron–hole interaction and are used to build the interaction kernel.

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

   V(r) = -\frac{e^2}{4 \varepsilon_0 \bar{\varepsilon} r_0} \left[ H_0\left(\frac{r}{r_0}\right) * Y_0\left(\frac{r}{r_0}\right) \right]

where:

* :math:`\bar{\varepsilon} = (\varepsilon_m + \varepsilon_s)/2` is the average surrounding dielectric
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

This allows the screening environment to be tuned independently along in-plane and out-of-plane directions -* a generalization that extends beyond conventional isotropic models.