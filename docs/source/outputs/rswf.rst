========================================
.rswf — Real-Space Probability Density
========================================

Generated when the ``-r --rswf [holeIndex=0]`` flag is provided, for the first $n$ excitons chosen with ``-n --states [n=8]``.

The `.rswf` file contains the **real-space probability density** $ P(\mathbf{r}) $ of the first few exciton wavefunctions, computed by fixing the hole position and evaluating the squared amplitude of the wavefunction as a function of the electron position in real space.


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

- ``x, y, z``: Coordinates of each unit cell vector (in Å)
- ``P``: Squared amplitude $ |\psi_X(\mathbf{r})|^2 $

Each block is separated by a `#` delimiter.

**Units**

- Coordinates are in $[x]=\text{\AA}$

Calculation
=========================

The probability density is computed as:

.. math::

   P(\mathbf{r}) = \left| \psi_X(\mathbf{r}, \mathbf{r}_h) \right|^2 = \sum_n \left| \psi^X_n(\mathbf{r}, \mathbf{r}_h) \right|^2

where:

- $ \mathbf{r}_h $ is the fixed hole position (specified by `--rswf [holeIndex]`)
- $ \psi^X_n $ denotes the exciton component over orbital $ n $
- The sum is over orbitals centered at $ \mathbf{r} $

By default, Xatu evaluates this for the **first 8 exciton states**, or as defined by the user with ``--states [n]``.

**Post-processing**

The `.rswf` output is used by the provided script ``rkwf.py`` to visualize or analyze the real-space distribution of excitons.
