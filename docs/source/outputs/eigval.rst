==============================
.eigval — Exciton Energies
==============================

This file contains the exciton eigenvalues (binding energies) computed from solving the Bethe-Salpeter Equation (BSE).

It is generated when running `xatu` with an exciton input file and requesting eigenvalues explicitly (via `-e`).

Format
======

A plain text list of exciton energies in **electron volts (eV)**:

.. code-block:: text

   Ncells
   BSE dimension
   Number of states
   E_1
   E_2
   E_3
   E_4
   .
   .
   .

Each line corresponds to a different exciton state, in ascending order of energy.