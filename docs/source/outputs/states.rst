==============================
.states — Exciton Eigenstates
==============================

This file stores the eigenstates for the $n$ excitons computed (via flag ``-s - -states [nstates]``, `default = 8`), in the electron-hole basis.

Format
======

The first line contains the dimension of the BSE matrix $n$, i.e. the number of different electron-hole pairs. 
The next $n$ lines specify the valence, conduction bands of each electron-hole pair and their $\mathbf{k}$ point

.. code-block:: text

   kx ky kz v c

Afterwards, each line specifies completely the coefficients of each exciton state. The format per line is

.. code-block:: text
   Re(A1) Im(A1) Re(A2) Im(A2)