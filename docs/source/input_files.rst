==========================
Input File Descriptions
==========================

Xatu requires two main input files: the **system file**, which defines the electronic system, and the **exciton file**, which specifies the excitonic calculation parameters. A third optional file (`kubo_w.in`) is used for optical conductivity calculations.

.. contents::
   :local:
   :depth: 2

System File Format (`.model`)
=============================

The model file specifies the real-space tight-binding or DFT system. It is composed of labeled blocks starting with **#**. Each block contains specific information:

Required Blocks
---------------

**# BravaisLattice:** Basis vectors of the Bravais lattice. The number of vectors present is also used
to determine the dimensionality of the system. The expected format is one vector per line, `x y z`.

**# Motif:** List with the positions and chemical species of all atoms of the motif (unit cell). The chemical species are specified with an integer index, used later to retrieve the number of orbitals of that species. The expected format is one atom per line, `x y z index`.

**# Orbitals:** Number of orbitals of each chemical species present. The position of the number of orbitals for each species follows the indexing used in the motif block. This block expects one or more numbers of orbitals, the same as the number of different species present, `n1 [n2 ...]`.

**# Filling:** Total number of electrons in the unit cell. Required to identify the Fermi level, which is the reference point in the construction of the excitons. Must be an integer number.

**# BravaisVectors:** List of Bravais vectors :math:`\mathbf{R}` that participate in the construction of the Bloch Hamiltonian. Expected one per line, in format ``x y z``.

**# FockMatrices:** Matrices :math:`H(\mathbf{R})` that construct the Bloch Hamiltonian :math:`H(\mathbf{k})` . The matrices must
be fully defined, i.e., they cannot be triangular, since the code does not use hermiticity to generate the Bloch Hamiltonian. The Fock matrices given must follow the ordering given in the block `BravaisVectors`. The matrices can be real or complex, and each one must be separated from the next using the delimiter `&`. In case the matrices are complex, the real and imaginary parts must be separated by a space, and the complex part must carry the imaginary umber symbol (e.g. $1.5 −2.1j$ ). Both $i$ and $j$ can be used.

Optional Blocks
---------------

**# [OverlapMatrices]:** In case that the orbitals used are not orthonormal, one can optionally provide the overlap matrices $S(\bm{R})$. The overlap in $k$ space is given by:

.. math::

   S(\bm{k}) = \sum_{\bm{R}}S(\bm{R})e^{i\bm{k}\cdot\bm{R}}

This is necessary to be able to reproduce the bands, which come from solving the generalized eigenvalue problem :math:`H(\mathbf{k})S(\mathbf{k})\Psi = ES(\mathbf{k})\Psi`. This will be specially necessary if the system was determined using DFT, since in tight-binding we usually assume orthonormality. This block follows the same rules as FockMatrices: each matrix :math:`S(\mathbf{R})` must be separated with the delimiter `&`, and they must follow the order given in `BravaisVectors`.

HDF5 Format (Alternative)
=========================

HDF5 have been introduced as a standardized alternative to the modelfiles. As a hierarchical data format, they are structured in the same way as the modelfiles, namely all the data fields are contained in the root group. The name of each dataset must be the same as those used for the modelfile. Note however that while the modelfiles are not sensitive to upper or lower case, the fields defined in the HDF5 file are. The main difference comes from the usage of complex numbers, which is not supported by the HDF5 format. To allow complex Hamiltonians (i.e. with spin-orbit coupling), in addition to the fields present in the modelfile one can also define the following dataset:  

**# [hamiltonian.imag]:** Optional dataset used to specify the imaginary part of the matrices that form the Bloch Hamiltonian. If present, its shape must be equal to that of `[hamiltonian]`.

Exciton File Format
===================

This file defines how to compute excitons and which parameters to use. It uses the same block-based syntax as the system file.

Key Blocks
----------

**# Label:** Prefix for output files (`[Label].eigval`, etc.)

**# Bands:** Number of valence and conduction bands to include

**# [BandList]:** Explicit list of indices of the bands that compose the exciton. 0 is taken as the last valence band, meaning that 1 would be the first conduction band, -1 is the second valence band and so on.  (overrides **# Bands**) **# Ncells**: Number of k-points in each direction of the Brillouin zone

**# Dielectric:** Substrate permittivity, medium permittivity, and screening length. Screening length can optionally be anisotropic: ``es em rx [ry [rz]]``. If only `es em rx` is provided, the Xatu uses ``r0=ry=rz=rx``.

Optional Blocks
---------------

**# [Submesh]:** Used to specify a submesh of the Brillouin zone. Takes a positive integer $m$ , which divides the BZ along each axis by that factor. The resulting area is meshed with the number of points specified in the Ncells block. This option can become memory intensive (it scales as $\mathcal{O}(m^d)$ , $d$ the dimension)

**# [ShiftMesh]:** Center submesh at ``kx ky kz`` provided.

**# [TotalMomentum]:** Exciton total center-of-mass momentum $\bm{Q}$, expects a vector ``qx qy qz``. Defaults to zero.

**# [Reciprocal]:** calculates interaction matrix elements in reciprocal space; It takes an integer argument to specify the number of reciprocal cells to sum over, ``nG``.

**# [Potential]:** Specify the potential function used in the direct term of the kernel of the BSE. `keldysh` or `coulomb` (defaults to `keldysh`)

**# [Exchange]:** Whether to include exchange interaction (`true` or `false`). Defaults to `true`.

**# [Exchange.potential]:** Used to specify the potential function used in the exchange term of the kernel of the BSE (`keldysh` or `coulomb`). Defaults to `keldysh`.

**# [Scissor]:** Apply bandgap correction shift, takes a single float `shift`.

**# [Regularization]:** Set the regularization distance used in the real-space method
to avoid the electrostatic divergence at $r = 0$ by setting $V (0) = V (a)$, where a is the regu-
larization distance. By default this parameter is set to the unit cell lattice parameter. It is
advised to be changed only for supercell calculations.

Absorption File: `kubo_w.in`
============================

Required when using ``-a`` or ``--absorption`` flag to compute optical absorption.

Format (fixed order):
---------------------

.. code-block:: text

   #initial frequency (eV)
   0
   #frequency range (eV)
   5
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

You can find working examples of `.model`, `exciton.config`, and `kubo_w.in` files in the `examples` folders of the Xatu repository.