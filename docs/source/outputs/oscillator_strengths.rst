=======================================
Exciton Oscillator Strengths (_osc.dat)
=======================================

The exciton oscillator strengths quantify the coupling of each excitonic state to the electromagnetic field and are used to compute the optical conductivity.

These values are computed internally when calculating the optical absorption spectrum and are written separatedly, following the BSE conductivity data (see :doc:`../outputs/conductivity`).

Output Format
===============

The oscillator strengths are written after the conductivity data in the **BSE output file**, following a blank line.

Each line corresponds to a single exciton and contains:

.. code-block:: text 

   En   Re(Vx)   Im(Vx)   Re(Vy)   Im(Vy)   Re(Vz)   Im(Vz)

where:

* ``En`` is :math:`E_X`: energy of the n-th exciton in eV;
* :math:`\text{Re}(V_\alpha), \text{Im}(V_\alpha)`: real and imaginary parts of the oscillator strength in direction :math:`\alpha`.

These values allow one to reconstruct the optical conductivity or analyze polarization-resolved excitonic properties.

**Units**

* :math:`[E_X] = \text{eV}`
* :math:`[V_\alpha]` is dimensionless (combined with prefactors in the conductivity formula)

See also: :doc:`../methods/optical_properties`

Definition
===========

The oscillator strength vector for a given exciton state :math:`X_k`, in direction :math:`\alpha \in \{x, y, z\}`, is given by:

.. math::

   V_k^\alpha = \sum_{v c \mathbf{k}} A_{vc}^k(\mathbf{k}) \, v_{vc}^\alpha(\mathbf{k})

where:

* :math:`A_{vc}^k(\mathbf{k})` are the exciton wavefunction coefficients
* :math:`v_{vc}^\alpha(\mathbf{k})` are the velocity matrix elements in direction :math:`\alpha`

The velocity matrix elements are defined as:

.. math::

   v_{vc}^\alpha(\mathbf{k}) = \langle v\mathbf{k} | \hat{v}^\alpha | c\mathbf{k} \rangle 
   = i\hbar^{-1} \langle v\mathbf{k} | [H_0, \hat{r}^\alpha] | c\mathbf{k} \rangle

where :math:`H_0` is the non-interacting (mean-field) Hamiltonian.