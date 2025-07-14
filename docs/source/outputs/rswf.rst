========================================
.rswf — Real-Space Probability Density
========================================

Generated when the ``-r --rswf [holeIndex=0]`` flag is provided, for the first$n $excitons chosen with ``-n --states [n=8]``.

The `.rswf` file contains the **real-space probability density**$P(\bm{r})$of the first few exciton wavefunctions, computed by fixing the hole position and evaluating the squared amplitude of the wavefunction as a function of the electron position in real space.


Format
=======

The file is organized in blocks, one for each exciton. Each block contains:

.. code-block:: text

   x   y   z   P
   ...
   #
   x   y   z   P
   ...
   #

Where:

- ``x, y, z``: Coordinates of each unit cell vector (in :math:`\text{\AA}`)
- ``P``: Squared amplitude :math:`\| \psi_X(\mathbf{r}) \|^2`

Each block is separated by a `#` delimiter.

**Units**

- Coordinates are in :math:`[x]=\text{\AA}`

Calculation
=========================

The probability density is computed as:

.. math::

   P(\bm{r}) = \left| \psi_X(\bm{r}, \bm{r}_h) \right|^2 = \sum_n \left| \psi^X_n(\bm{r}, \bm{r}_h) \right|^2

where:

- :math:`\mathbf{r}_{h}` is the fixed hole position (specified by `--rswf [holeIndex]`)
- :math:`\psi^{X}_{n}` denotes the exciton component over orbital$n $
- The sum is over orbitals centered at $\mathbf{r}$

By default, Xatu evaluates this for the **first 8 exciton states**, or as defined by the user with ``--states [n]``.

**Post-processing**

The `.rswf` output is used by the provided script ``rkwf.py`` to visualize or analyze the real-space distribution of excitons.
