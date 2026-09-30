============================
.eigval — exciton energies
============================

Written with ``-e``.

Format
======

.. code-block:: text

   30          <- ncells
   900         <- dimension of the BSE (number of electron–hole pairs)
   8           <- number of energies that follow
      5.3356862
      5.3356866
      6.0738001
      ...

The first three lines are a header. Then come the exciton energies :math:`E_X` in **eV**, one per
line, in ascending order. There are ``-n`` of them, or those up to ``-t``.

These are **excitation energies** measured from the ground state, not binding energies. The binding
energy of an exciton is the band gap minus :math:`E_X`.

.. code-block:: python

   import numpy as np
   E = np.loadtxt("hBN_N30.eigval", skiprows=3)
