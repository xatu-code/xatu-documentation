================================
.spin — Exciton Spin Projection
================================

When using the ``-s`` or ``--spin`` flag, Xatu outputs the spin characteristics of each computed exciton state. This includes the total spin projection and the individual spin projections of the electron and the hole.

Format
======

Each line in the ``.spin`` file has the format:

.. code-block:: text

   n    St    Sh    Se

Where:

* ``n``: Exciton index (starting from $0$ )
* ``St``: Total spin projection $S^z$of the exciton
* ``Sh``: Spin projection $ s^z_h$ of the hole
* ``Se``: Spin projection $ s^z_e$ of the electron

All values are given in units of :math:`\hbar`, e.g., :math:`\pm 1/2,\ \pm 1,\ 0` , etc.


=========================
Spin Projection Output
=========================

When running Xatu with the ``-s`` or ``--spin`` flag, the code outputs a file containing the total spin projection of each excitonic state, along with the spin of the constituent electron and hole states.

Each line in the output contains:

.. code-block:: text

   exciton_index   Sz_total   Sz_hole   Sz_electron

Units: :math:`\hbar`

Spin Calculation
=================

The total spin projection :math:`\langle X | \hat{S}_z^T | X \rangle` for each excitonic state :math:`|X\rangle` is computed from the exciton wavefunction coefficients using the expression (see Eq. 31 of the paper):

.. math::

   \langle S_z^T \rangle = \sum_{v,c,\mathbf{k}} |A_{vc}^{Q}(\mathbf{k})|^2 (\sigma_c - \sigma_v)

where:

- :math:`A_{vc}^{Q}(\mathbf{k})` is the excitonic coefficient in the electron-hole basis
- :math:`\sigma_c`, :math:`\sigma_v \in \{-1/2, +1/2\}` are the spin projections of the conduction and valence bands, respectively

The spin of the exciton is thus the **difference** between the electron and hole spin projections, weighted by the probability amplitude of each electron-hole pair in the excitonic state.

**Assumptions**

- Spin is assumed to be a good quantum number of the single-particle states.
- This holds when the Hamiltonian :math:`H_0` commutes with :math:`\hat{S}_z`, i.e., in the absence of spin-orbit coupling or magnetic noncollinearity.
- Under this condition, spin projections are well-defined and can be treated using scalar labels :math:`\sigma_n` for each band.

Reference
=========

For a full derivation, see Section 2.3 and Eq. (30–31) in:

`Efficient computation of optical excitations in two-dimensional materials with the Xatu code <https://doi.org/10.1016/j.cpc.2023.109001>`_

