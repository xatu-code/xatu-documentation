======================================
.kwf — Momentum-Space Probability Density
======================================

Generated when the ``-k --kwf`` flag is provided for the first $n$ excitons chosen with ``-n --states [n=8]``.

The `.kwf` file stores the **momentum-space probability density** of each exciton wavefunction. It quantifies how the exciton is distributed over electron-hole pairs with a well-defined crystal momentum $ \mathbf{k} $.

Format
=======

The file contains a table with one row per k-point and one column per exciton state:

.. code-block:: text

   kx ky kz P
   .
   .
   .
   #
   kx ky kz P
   .
   .
   .
   #

**Units**
- $[k]=\AA^{-1}$
- $ |\psi_X(\mathbf{k})|^2 $ is dimensionless and normalized over the k-grid

Calculation
========================

Given the exciton wavefunction expressed in the electron-hole basis as $ A^{Q}_{vc}(\mathbf{k}) $, the $k$-space probability is defined as:

.. math::

   |\psi_{X}(\mathbf{k})|^2 = \sum_{v,c} \left| A^{Q}_{vc}(\mathbf{k}) \right|^2

This quantity is evaluated on the same k-point grid used in the original BSE calculation.