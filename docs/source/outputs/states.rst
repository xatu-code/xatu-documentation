=================================
.states — exciton eigenstates
=================================

Written with ``-c``. It contains the coefficients :math:`A_{vc}(\bm{k})` of each exciton in the
electron–hole basis, the solutions of the BSE (see :doc:`../methods/BSE`):

.. math::

   |X\rangle = \sum_{v,c,\bm{k}} A_{vc}(\bm{k})\; c^\dagger_{c,\bm{k}+\bm{Q}}\, c_{v,\bm{k}}\, |GS\rangle .

Format
======

.. code-block:: text

   900                                                  <- n_pairs, dimension of the BSE
   -1.4510418   0.0000000   0.0000000   0   1           <- basis: kx ky kz v c
   -1.4026738   0.0837758   0.0000000   0   1
   ...                                                  (n_pairs lines)
   Re(A1) Im(A1) Re(A2) Im(A2) ... Re(An) Im(An)        <- exciton 1
   Re(A1) Im(A1) Re(A2) Im(A2) ... Re(An) Im(An)        <- exciton 2
   ...

1. **Header**: the number of electron–hole pairs ``n_pairs``.
2. **Basis**: ``n_pairs`` lines, each giving one pair: the k-point (:math:`\text{Angstrom}^{-1}`) and the valence and conduction
   band indices ``v c``. Band indices are absolute and count from 0 at the lowest band of the
   Hamiltonian, so the top valence band is ``filling - 1``.
3. **Coefficients**: one line per exciton, with the complex coefficients as ``Re Im`` pairs. The
   :math:`j`-th pair belongs to the :math:`j`-th basis line.

Each exciton is normalised: :math:`\sum_j |A_j|^2 = 1`. There are ``-n`` exciton lines, or those up to
``-t``.

.. code-block:: python

   import numpy as np
   with open("hBN_N30.states") as f:
       n = int(f.readline())
       basis = np.array([f.readline().split() for _ in range(n)], dtype=float)
       coefs = np.loadtxt(f)
   A = coefs[:, 0::2] + 1j * coefs[:, 1::2]     # A[exciton, pair]
