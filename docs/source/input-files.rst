==========================
Input File Descriptions
==========================

Xatu requires two main input files: the **system file**, which defines the electronic system, and the **exciton file**, which specifies the excitonic calculation parameters. A third optional file (`kubo_w.in`) is used for optical conductivity calculations.

.. contents::
   :local:
   :depth: 2

System File Format (`.model`)
=============================

The model file specifies the real-space tight-binding or DFT system. It is composed of labeled blocks starting with `#`. Each block contains specific information:

Required Blocks
---------------

- **# BravaisLattice**: Bravais lattice vectors, one per line (`x y z`)
- **# Motif**: Atom positions and species indices (`x y z species_index`)
- **# Orbitals**: Number of orbitals for each species
- **# Filling**: Total number of electrons in unit cell
- **# BravaisVectors**: Real-space vectors `R` for the Hamiltonian
- **# FockMatrices**: Real-space matrices `H(R)`, separated by `&`. Complex numbers must use `i` or `j`.

Optional Blocks
---------------

- **# OverlapMatrices**: For non-orthonormal basis. Matches structure of `FockMatrices`.

All comments begin with `!` and empty lines are ignored.

HDF5 Format (Alternative)
=========================

Instead of `.model` files, you can use `.hdf5` files containing the same fields as datasets in the root group. Field names are **case-sensitive**. For complex Hamiltonians, an extra dataset `hamiltonian.imag` can be included.

Exciton File Format
===================

This file defines how to compute excitons and which parameters to use. It uses the same block-based syntax as the system file.

Key Blocks
----------

- **# Label**: Prefix for output files (`[Label].eigval`, etc.)
- **# Bands**: Number of valence and conduction bands to include
- **# [BandList]**: Explicit list of bands (overrides `# Bands`)
- **# Ncells**: Number of k-points in each direction of the Brillouin zone
- **# Dielectric**: Substrate permittivity, medium permittivity, and screening length: `es em r0`

Optional Blocks
---------------

- **# [Submesh]**: Divide BZ into m×m×m submeshes
- **# [ShiftMesh]**: Center submesh: `kx ky kz`
- **# [TotalMomentum]**: Exciton total momentum `Q`
- **# [Reciprocal]**: Use reciprocal-space interactions; takes `nG`
- **# [Potential]**: `keldysh` or `coulomb` (defaults to `keldysh`)
- **# [Exchange]**: Whether to include exchange (`true` or `false`)
- **# [Exchange.potential]**: Same options as above
- **# [Scissor]**: Apply bandgap correction shift
- **# [Regularization]**: Set real-space regularization length `a`

Absorption File: `kubo_w.in`
============================

Required when using `-a` flag to compute optical absorption.

Format (fixed order):
---------------------

.. code-block:: text

   #initial frequency (eV)
   5
   #frequency range (eV)
   8
   #number of frequency points
   300
   #broadening parameter (eV)
   0.05
   #type of broadening
   lorentzian
   #output kubo name files
   kubo_sp.dat
   kubo_ex.dat

Supported broadening types: `lorentzian`, `gaussian`, `exponential`

Example Input Files
===================

You can find working examples of `.model`, `.in`, and `kubo_w.in` files in the `/models` and `/main` folders of the Xatu repository.
