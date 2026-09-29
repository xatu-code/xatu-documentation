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
to determine the dimensionality of the system. The expected format is one vector per line, ``x y z``.

**# Motif:** List with the positions and chemical species of all atoms of the motif (unit cell). The chemical species are specified with an integer index, used later to retrieve the number of orbitals of that species. The expected format is one atom per line, ``x y z index``.

**# Orbitals:** Number of orbitals of each chemical species present. The position of the number of orbitals for each species follows the indexing used in the motif block. This block expects one or more numbers of orbitals, the same as the number of different species present, ``n1 [n2 ...]``.

**# Filling:** Total number of electrons in the unit cell. Required to identify the Fermi level, which is the reference point in the construction of the excitons. Must be an integer number.

**# BravaisVectors:** List of Bravais vectors :math:`\bm{R}` that participate in the construction of the Bloch Hamiltonian. Expected one per line, in format ``x y z``.

**# FockMatrices:** Matrices :math:`H(\bm{R})` that construct the Bloch Hamiltonian :math:`H(\bm{k})` . The matrices must
be fully defined, i.e., they cannot be triangular, since the code does not use hermiticity to generate the Bloch Hamiltonian. The Fock matrices given must follow the ordering given in the block `BravaisVectors`. The matrices can be real or complex, and each one must be separated from the next using the delimiter `&`. In case the matrices are complex, the real and imaginary parts must be separated by a space, and the complex part must carry the imaginary umber symbol (e.g. $1.5 −2.1j$ ). Both $i$ and $j$ can be used.

Optional Blocks
---------------

**# [OverlapMatrices]:** In case that the orbitals used are not orthonormal, one can optionally provide the overlap matrices :math:`S(\bm{R})`. The overlap in $k$ space is given by:

.. math::

   S(\bm{k}) = \sum_{\bm{R}}S(\bm{R})e^{i\bm{k}\cdot\bm{R}}

This is necessary to be able to reproduce the bands, which come from solving the generalized eigenvalue problem :math:`H(\bm{k})S(\bm{k})\Psi = ES(\bm{k})\Psi`. This will be specially necessary if the system was determined using DFT, since in tight-binding we usually assume orthonormality. This block follows the same rules as FockMatrices: each matrix :math:`S(\bm{R})` must be separated with the delimiter `&`, and they must follow the order given in `BravaisVectors`.

DFT Hamiltonians (CRYSTAL and Wannier90)
========================================

CRYSTAL
--------

One may use the hamiltonian given in ``.outp`` from CRYSTAL. When doing so, you may specify the number of unit cells to read. 

The hamiltonian can be written in ``.outp`` by writing the ``input.d3`` with

.. code-block:: bash

   BASISSET
   2
   60 M
   64 N
   END

where $M$ and $N$ are the number of overlap and Fock matrices printed.

Wannier90
-----------

One may use the hamiltonian given in ``_tb.dat`` from Wannier90. When using this hamiltonian, it is mandatory to indicate the number of filled bands ``[filling]`` when executing the commnad line. see :doc:`./usage`.

To print the hamiltonian one must include  ``write_tb = .true.`` in the ``.win`` file.


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

**# [BandList]:** Explicit list of indices of the bands that compose the exciton. 0 is taken as the last valence band, meaning that 1 would be the first conduction band, -1 is the second valence band and so on.  (overrides **# Bands**) 

**# Ncells**: Number of k-points in each direction of the Brillouin zone

**# Dielectric:** Substrate permittivity, medium permittivity, and screening length. Screening length can optionally be anisotropic: ``es em rx [ry [rz]]``. If only ``es em rx`` is provided, the Xatu uses :math:`r_{0}=r^{y}_{0}=r^{z}_{0}=r^{x}_{0}`.

Optional Blocks
---------------

**# [Submesh]:** Used to specify a submesh of the Brillouin zone. Takes a positive integer $m$ , which divides the BZ along each axis by that factor. The resulting area is meshed with the number of points specified in the `Ncells` block. This option can become memory intensive (it scales as :math:`\mathcal{O}(m^d)` , $d$ the dimension)

**# [ShiftMesh]:** Center submesh at ``kx ky kz`` provided.

**# [TotalMomentum]:** Exciton total center-of-mass momentum :math:`\bm{Q}`, expects a vector ``qx qy qz``. Defaults to zero.

**# [Gcutoff]:** calculates interaction matrix elements in reciprocal space; It takes a real argument to specify the cutoff for the reciprocal lattice vectors. Can be smaller than the one specified in the screening file.

**# [Potential]:** Specify the potential function used in the direct term of the kernel of the BSE. `keldysh` or `coulomb` (defaults to `keldysh`)

**# [Exchange]:** Whether to include exchange interaction (`true` or `false`). Defaults to `false`.

**# [Exchange.potential]:** Used to specify the potential function used in the exchange term of the kernel of the BSE (`keldysh` or `coulomb`). Defaults to `keldysh`.

**# [Scissor]:** Apply bandgap correction shift, takes a single float `shift`.

**# [Regularization]:** Set the regularization distance used in the real-space method to avoid the electrostatic divergence at $r = 0$ by setting $V (0) = V (a)$, where a is the regularization distance. By default this parameter is set to the unit cell lattice parameter. It is advised to be changed only for supercell calculations.

**# [Percentage]:** Set the regularization distance :math:`q_0` used in the reciprocal-space method to avoid the electrostatic divergence at $q = 0$ by setting $q_0 = \varsigma k_0$, where $\varsigma$ is the percentage of the smallest wavevector in the BZ mesh. By default this parameter is set to `0.5`. If `0.0` is provided, then the singular term in the potential is set to `0.0`.

Screening File Format
=====================

This file defines how the microscopic dielectric screening is computed and which parameters to use. It uses the same block-based syntax as the exciton file. Currently,  if a screening file is provided, then an exciton file must be provided as well.

Key Blocks
----------

**# ncells_aux**: Number of unit cells/kpoints, in each direction, of the auxiliary BZ mesh to compute the polarizability matrix element(s).

**# valence.bands:** Number of valence bands included in the calculations.

**# conduction.bands:** Number of conduction bands included in the calculations.

**# spin:** Indicates whether if the spin degree of freedom has been considered in the system model or not (`true` or `false`).

**# gcutoff:** Defines the cutoff ``Gcutoff`` for the reciprocal lattice vectors to be included in the calculation of the dielectric matrix. Defaults to `2.5`. Can be different (higher) than the one specified in the exciton file.

**# function:** Specifies which functionality of the screening the user intends. It can be `dielectric`, `polarizability`, `inversedielectric` or `exciton`.

.. hlist::
   :columns: 1

   * **dielectric** Computes the dielectric function at a specified momentum and for a chosen matrix element. The values of the polarizability as a function of included valence and conduction bands are computed and printed in a file named `polarizability_convergence.dat`. Each line of the file has the form ``[# valence bands] [# conduction bands] [Re{χ}] [Im{χ}]``.
   * **polarizability** Computes the polarizability matrix element :math:`\chi_{\bm{G}\bm{G}'}` for the specified pair :math:`\bm{G}`, :math:`\bm{G}'`  in the BZ mesh. The values are printed to the `polarizability_mesh.dat` file, and each line of the file has the structure ``[kx] [ky] [kz] [Re{χ}] [Im{χ}]``.  Currently works only for 2D materials, whence `kz = 0` at all times.
   * **inversedielectric** Computes the inverse of the dielectric matrix :math:`\epsilon^{-1}(\bm{q})` at the specified momentum. The matrix elements are printed to the file `<label>_invepsilon.dat`. The order of the `G` vectors is the same as the one they appear by when printed to `stdout` when this option is used. Each row in the file has the real and imaginary parts of each matrix element printed separately separated by a space (and conserving the order of the `G` vectors).
   * **exciton**  Computes the inverse of the dielectric matrix in the BZ mesh, and proceeds with the calculation of the exciton. A file containing all the points in the BZ mesh is generated. The file has a name of the form `kgrid_<ncells>.dat`, where `ncells` is the number of cells in each direction, specified in the exciton file. The object :math:`\epsilon^{-1}(\bm{q})` is printed to the file `<label>_invepsilon.dat`, where `<label>` is the value of the label parameter specified in the exciton file. All the individual matrices :math:`\epsilon^{-1}(\bm{q})` are printed by the same order of momentum points as that of the file containing the `k` points.

**# vectors:** Indicates which pair of reciprocal lattice vectors :math:`\bm{G}`, :math:`\bm{G}'` the polarizability is computed for. Two indices have to be provided as: `<index1> <index2>`. This entry is valid for both functions `dielectric` and `polarizability`. Defaults to `0 0`.

**# momentum:** Specifies which momentum the polarizability, or inverse of the dielectric matrix, is to be computed at. A vector in the form `qx qy qz` has to be given. Defaults to `0.2 0 0`.

Optional Blocks
---------------

**# [isotropic]:** Indicates whether the system is isotropic (`true` or `false`). Defaults to `false`.

**# [thickness]:** Indicates the thickness of the 2D material. If provided, it enables the Q2D calculation for the **inversedielectric** or **exciton** functions. Defaults to `0.0`.

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
