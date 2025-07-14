==========================
.spin — Exciton Spin Projection
==========================

When using the ``-s`` flag, Xatu outputs the spin characteristics of each computed exciton state. This includes the total spin projection and the individual spin projections of the electron and the hole.

Format
======

Each line in the ``.spin`` file has the format:

.. code-block:: text

   n    St    Sh    Se

Where:

- ``n``: Exciton index (starting from 0)
- ``St``: Total spin projection $S^z$of the exciton
- ``Sh``: Spin projection $ s^z_h$ of the hole
- ``Se``: Spin projection $ s^z_e$ of the electron

All values are given in units of :math:`\hbar`, e.g., :math:`\pm 1/2,\ \pm 1,\ 0` , etc.


Calculation
=========================

The spin projections are calculated from the expectation values of the spin operator along the $z$-axis for each quasiparticle, based on their wavefunction composition.

From the Xatu paper (Section 2.3):

- The spin projection $S^z$ of the exciton is obtained as the **sum** of the electron and hole spin projections.
- The projection of each single-particle state is computed using:

  .. math::

     \langle \phi_{n,\bm{k}} | \hat{S}_z | \phi_{n,\bm{k}} \rangle

  where $\phi_{n,\mathbf{k}}$ is the HF eigenstate of band $n$ and momentum $\mathbf{k}$ , and :math:`\hat{S}_z` is the spin operator.

- For an exciton state $M$, the total spin projection is:

  .. math::

     S^z_M = \sum_{vc\bm{k}} | A^M_{vc}(\bm{k}) |^2 (s^z_c - s^z_v)

This assumes spin is well-defined for each state -- i.e., spin-orbit coupling or noncollinear magnetism is not explicitly required for the output.