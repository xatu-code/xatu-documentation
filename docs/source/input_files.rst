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

**# [Gcutoff]:** Calculates the interaction matrix elements in reciprocal space. It takes a real argument, the cutoff for the reciprocal lattice vectors :math:`\bm{G}` summed over. With the `rpa` potential it can be smaller than the one specified in the screening file.

**# [Potential]:** Specify the potential function used in the direct term of the kernel of the BSE: `keldysh`, `coulomb` or `rpa` (defaults to `keldysh`). `rpa` uses the numerical screened potential and requires a screening file (see `Screening File Format`_) and the reciprocal-space method (**# Gcutoff**).

**# [Exchange]:** Whether to include exchange interaction (`true` or `false`). Defaults to `false`.

**# [Exchange.potential]:** Used to specify the potential function used in the exchange term of the kernel of the BSE (`keldysh`, `coulomb` or `rpa`). Defaults to `keldysh`.

**# [Scissor]:** Apply bandgap correction shift, takes a single float `shift`.

**# [Regularization]:** Set the regularization distance used in the real-space method to avoid the electrostatic divergence at $r = 0$ by setting $V (0) = V (a)$, where a is the regularization distance. By default this parameter is set to the unit cell lattice parameter. It is advised to be changed only for supercell calculations.

**# [Percentage]:** Sets the radius :math:`q_0 = \varsigma k_0` of the disk around :math:`\Gamma` used in the reciprocal-space method to regularize the divergent :math:`\bm{q} = 0` term of the interaction, where :math:`\varsigma` is this parameter and :math:`k_0` the smallest nonzero wavevector of the BZ mesh. The divergent term is replaced by the average of the screened potential over that disk (see :doc:`./methods/BSE`). Defaults to `0.5`. If `0.0` is provided, the :math:`\bm{q} = 0` term is set to zero. This term shifts all exciton energies rigidly by an amount that vanishes as the BZ mesh is refined; splittings, wavefunctions and oscillator strengths do not depend on it.

Screening File Format
=====================

This file defines how the microscopic dielectric screening is computed and which parameters to use. It is passed with the ``-z`` flag and uses the same block-based syntax as the exciton file. If a screening file is provided, an exciton file must be provided as well; its ``label`` names the output files. The screening model is chosen with **# screening.mode** and described in :doc:`./methods/screening`.

Key Blocks
----------

**# function:** Specifies which screening functionality is run: `dielectric`, `polarizability`, `inversedielectric` or `exciton`. Except for `exciton`, the calculation stops after writing its output. What each function writes depends on **# screening.mode**:

.. hlist::
   :columns: 1

   * **dielectric** Computes the dielectric matrix :math:`\epsilon_{\bm{G}\bm{G}'}(\bm{q})` at the momentum given in **# momentum** and writes it to `<label>_epsilon.dat`, with the same layout as the inverse (see :doc:`./outputs/invepsilon`). In `q2d_averaged` mode this is the inverse of the projected inverse response, not an average of the microscopic dielectric function.
   * **polarizability** In `2d` mode, computes the polarizability matrix element :math:`\chi_{\bm{G}\bm{G}'}` for the pair of **# vectors** over the BZ mesh and writes it to `polarizability_mesh.dat`, one line ``[kx] [ky] [kz] [Re{χ}] [Im{χ}]`` per k point. In `q2d_legacy` mode, writes the polarizability matrix at **# momentum** to `<label>_polarizability.dat`. Not available in `q2d_averaged` mode.
   * **inversedielectric** Computes the inverse dielectric matrix :math:`\epsilon^{-1}_{\bm{G}\bm{G}'}(\bm{q})` at **# momentum** and writes it to `<label>_invepsilon.dat` (see :doc:`./outputs/invepsilon`). The order of the :math:`\bm{G}` vectors is the one printed to `stdout`. In `q2d_averaged` mode the file holds the projected inverse response :math:`M`, and :math:`\epsilon_M(\bm{q}) = 1/M_{00}(\bm{q})`.
   * **exciton** Computes the screening on the BZ mesh and continues with the exciton calculation using the `rpa` potential. The BZ mesh is written to `kgrid_<ncells>.dat`. In the `2d`, `q2d_legacy` and `q2d_averaged` modes the inverse dielectric matrices on that mesh are written to `<label>_invepsilon.dat`, in the order of `kgrid_<ncells>.dat`. In `q2d_atomic` mode the screened interaction is built internally and not written.

In `q2d_atomic` mode, every function other than `exciton` computes the atomic-plane screening at **# momentum** and writes it to `<label>_q2d_atomic.dat`: the plane heights, the :math:`\bm{G}` vectors, and for each :math:`\bm{q}` the matrices :math:`P`, :math:`B`, :math:`R`, :math:`W`, :math:`I - BP` and :math:`I + BR` of :doc:`./methods/screening`, indexed as ``G*Nplanes + plane``.

**# ncell_aux:** Number of k points in each direction of the auxiliary BZ mesh used to compute the polarizability.

**# valence.bands:** Number of valence bands included in the polarizability.

**# conduction.bands:** Number of conduction bands included in the polarizability.

**# spin:** Whether the spin degree of freedom is included in the system model (`true`) or not (`false`). With `false` a spin degeneracy factor of 2 is applied.

**# gcutoff:** Cutoff for the reciprocal lattice vectors :math:`\bm{G}` included in the dielectric matrix. It can be larger than the one specified in the exciton file.

Optional Blocks
---------------

**# [screening.mode]:** Screening model. Defaults to `2d`.

.. hlist::
   :columns: 1

   * **2d** Strictly two-dimensional RPA dielectric matrix.
   * **q2d_legacy** Quasi-2D RPA dielectric matrix averaged over a slab of thickness **# thickness**.
   * **q2d_atomic** Quasi-2D RPA resolved on the atomic planes of the structure, solved analytically in :math:`z`.
   * **q2d_averaged** The `q2d_atomic` response, averaged uniformly in :math:`z` after the inversion.

**# [momentum]:** Momentum :math:`\bm{q}` at which the dielectric function, polarizability or atomic screening is computed, as ``qx qy qz``. Not used by the `exciton` function. Defaults to `0.2 0 0`.

**# [vectors]:** Pair of indices of the reciprocal lattice vectors :math:`\bm{G}`, :math:`\bm{G}'` for which the `polarizability` function computes :math:`\chi_{\bm{G}\bm{G}'}` in `2d` mode, as ``<index1> <index2>``. Defaults to `0 0`.

**# [isotropic]:** Whether the system is isotropic (`true` or `false`). If `false`, the :math:`\bm{q} = 0` regularization of the `2d` and `q2d_legacy` modes averages the dielectric function along :math:`\bm{q}_0` and the perpendicular direction. Defaults to `false`.

**# [thickness]:** Thickness :math:`d_\perp` of the slab in `q2d_legacy` mode, in Angstrom. Required and positive in that mode; ignored by the others.

**# [zaverage.margin]:** Used by `q2d_averaged` only. The averaging interval in :math:`z` defaults to the extent of the atomic planes, :math:`[z_\mathrm{min}, z_\mathrm{max}]`. A margin :math:`m` widens it to :math:`[z_\mathrm{min} - m, z_\mathrm{max} + m]`, a width proportional to the structure. Defaults to `0`. The result depends on this choice; the interval used is printed.

**# [zaverage.zmin], [zaverage.zmax]:** Used by `q2d_averaged` only. Explicit bounds of the averaging interval, in Angstrom; each replaces the bound on its side, including the margin. All atomic planes must lie inside the interval. A structure whose atoms all share one height needs a margin or both bounds.

**# [zdecomposition.states]:** `q2d_atomic` with function `exciton` only. List of 1-based exciton indices whose direct interaction term is decomposed into contributions from each ordered pair of atomic planes, for both the screened and the bare interaction. The result is written to `<label>_zdecomposition.dat`. This is a read-only diagnostic: it changes no energy or state.

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
