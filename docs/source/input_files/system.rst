===========
System file
===========

The system file describes the crystal and its single-particle (tight-binding, DFT or Wannier)
Hamiltonian. Xatu reads four formats:

.. list-table::
   :header-rows: 1
   :widths: 30 25 45

   * - Format
     - Flag
     - Notes
   * - Xatu model file (``.model``)
     - *(default)*
     - Plain text, described below.
   * - HDF5
     - ``-f hdf5``
     - Same fields as the model file. Needs an HDF5 build.
   * - CRYSTAL output (``.outp``)
     - ``-d <ncells>``
     - DFT with localized basis, including overlaps.
   * - Wannier90 (``_tb.dat``)
     - ``-w <filling>``
     - Maximally localized Wannier functions.

Xatu model file
===============

Units are Å for lengths and eV for energies. The blocks follow the common syntax of
:doc:`../input_files`.

Required blocks
---------------

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Keyword
     - Content
   * - ``# dimension``
     - Number of periodic dimensions: ``1``, ``2`` or ``3``.
   * - ``# bravaislattice``
     - Lattice vectors, one per line: ``x y z``. There must be one per periodic dimension.
   * - ``# motif``
     - Atoms of the unit cell, one per line: ``x y z species``. ``species`` is an integer index (from
       0) into ``# norbitals``.
   * - ``# norbitals``
     - Number of orbitals of each species, in species order: ``n0 [n1 ...]``.
   * - ``# filling``
     - Number of **filled bands**, a positive integer. The highest valence band is band
       ``filling − 1`` (counting from 0), which sets the Fermi level used to build the excitons. In a
       basis with explicit spin, this equals the number of electrons per unit cell.
   * - ``# bravaisvectors``
     - The Bravais vectors :math:`\bm{R}` for which a Hamiltonian matrix is given, one per line:
       ``x y z`` (Cartesian, Å).
   * - ``# hamiltonian``
     - The matrices :math:`H(\bm{R})`, in the order of ``# bravaisvectors``, separated by a line with
       ``&``. See below.

Optional blocks
---------------

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Keyword
     - Content
   * - ``# overlap``
     - Overlap matrices :math:`S(\bm{R})` for non-orthogonal orbitals, in the same format and order as
       ``# hamiltonian``. If absent, the orbitals are taken as orthonormal.

Writing the matrices
--------------------

* Each :math:`H(\bm{R})` is a full :math:`N_\text{orb}\times N_\text{orb}` matrix, one row per line.
  **Give all elements**: Xatu does not use hermiticity to fill in missing parts.
* Matrices are separated by a line containing only ``&``.
* Entries can be real, or complex with an explicit imaginary unit (``i`` or ``j``) attached to the
  imaginary part, e.g. ``1.5 -2.1j``.
* The Bloch Hamiltonian is :math:`H(\bm{k}) = \sum_{\bm{R}} H(\bm{R})\,e^{i\bm{k}\cdot\bm{R}}`, and
  likewise :math:`S(\bm{k})`. The bands solve :math:`H(\bm{k})\psi = E\,S(\bm{k})\psi`.

Example (hBN, two orbitals)
---------------------------

.. code-block:: text

   # dimension
   2
   # norbitals
   1 1
   # bravaislattice
       2.165060     1.250000     0.000000
       2.165060    -1.250000     0.000000
   # motif
       0.000000     0.000000     0.000000     0
       1.443376     0.000000     0.000000     1
   # bravaisvectors
       0.000000     0.000000     0.000000
      -2.165060    -1.250000     0.000000
      -2.165060     1.250000     0.000000
       2.165060    -1.250000     0.000000
       2.165060     1.250000     0.000000
   # hamiltonian
       3.625000   +0.000000j    -2.300000   +0.000000j
      -2.300000   +0.000000j    -3.625000   +0.000000j
   &
       0.000000   +0.000000j    -2.300000   +0.000000j
       0.000000   +0.000000j     0.000000   +0.000000j
   &
      ... (three more matrices)
   # filling
   1

HDF5 format
===========

HDF5 files hold the same fields as the model file, as datasets in the root group, with the same names.
Unlike the model file, **dataset names are case sensitive**.

HDF5 has no complex type, so complex Hamiltonians (e.g. with spin–orbit coupling) add one dataset:

``hamiltonian.imag`` *(optional)*
   Imaginary part of the Hamiltonian matrices. Same shape as ``hamiltonian``.

Build Xatu with ``HDF5=1`` (see :doc:`../installation`) and run with ``-f hdf5``.

CRYSTAL
=======

Xatu reads the Fock and overlap matrices printed in the CRYSTAL ``.outp`` file. To print them, add to
the ``input.d3`` properties input:

.. code-block:: text

   BASISSET
   2
   60 M
   64 N
   END

where ``M`` and ``N`` are the numbers of overlap and Fock matrices printed. Run Xatu with
``-d <ncells>``, where ``<ncells>`` is the number of unit cells whose matrices are read.

Wannier90
=========

Xatu reads the ``<seedname>_tb.dat`` file written by Wannier90 when ``write_tb = .true.`` is set in
the ``.win`` file. It contains the lattice, :math:`H(\bm{R})` and the position matrix elements. The
filling is not part of that file, so give it on the command line:

.. code-block:: bash

   xatu -w <filling> system_tb.dat exciton.txt

|w90| The w90 version handles the degeneracy weights of the ``_tb.dat`` file, and places the Wannier
centres in the home unit cell for the real-space wavefunction (``.rswf``).

The ``utility/wannier2xatu`` folder of the repository has tools to convert Wannier90 output into a Xatu
model file.
