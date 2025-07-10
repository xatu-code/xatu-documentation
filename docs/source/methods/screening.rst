=====================================
Screening Potentials in Xatu
=====================================

In Xatu, the electron-hole interaction kernel in the Bethe-Salpeter Equation (BSE) is built assuming point-like localized orbitals and a phenomenological screening. Two models are implemented to describe the screened Coulomb interaction:

- The **bare Coulomb potential**
- The **Rytova-Keldysh potential**, suitable for 2D systems

These screening models are used to compute the direct and exchange terms of the BSE kernel either in real space or reciprocal space.

.. contents::
   :local:
   :depth: 2

Coulomb Interaction
=====================

The standard 3D Coulomb interaction is used as the default in vacuum and bulk systems:

.. math::

   V(r) = \frac{e^2}{4\pi\epsilon_0 \epsilon_r r}

In reciprocal space:

.. math::

   V(\mathbf{q}) = \frac{e^2}{\epsilon_0 \epsilon_r q^2}

where \( a \) is the in-plane lattice constant. In Fourier-based calculations, the divergence at \( q=0 \) is removed by setting \( V(q=0) = 0 \).

Rytova-Keldysh Potential
==========================

The Rytova-Keldysh model describes screened Coulomb interactions in two-dimensional (2D) materials embedded in a dielectric environment:

.. math::

   V(r) = \frac{e^2}{8 \epsilon_0 \bar{\epsilon} r_0} \left[ H_0\left( \frac{r}{r_0} \right) - Y_0\left( \frac{r}{r_0} \right) \right]

where:

- \( \bar{\epsilon} = \frac{\epsilon_m + \epsilon_s}{2} \) is the average dielectric constant of the surrounding media
- \( r_0 \) is the effective screening length of the 2D material
- \( H_0 \) is the Struve function of order 0
- \( Y_0 \) is the Bessel function of the second kind

This potential captures the non-local screening effects in layered materials and decays faster than the bare Coulomb interaction.

Regularization
--------------------------

Both potential diverges as \( r \rightarrow 0 \). This divergence is regularized by setting:

.. math::

   V(0) = V(a)

where \( a \) is the lattice parameter.

Cutoff and Regularization
--------------------------

Since the interaction decays quickly, a radial cutoff \( R_c \) is applied:

.. math::

   \tilde{V}(r) = 
   \begin{cases}
     V(a) & r = 0 \\
     V(r) & r < R_c \\
     0 & r \geq R_c
   \end{cases}

The default is to use the Keldysh interaction with real-space summation. 

Reciprocal Space Representation
--------------------------

As for the interactions computed using the Fourier series of the potential, we set V(q = 0) = 0 to remove the long wavelength divergence.

