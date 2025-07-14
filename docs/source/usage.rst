========================
Command-Line Usage
========================

Xatu can be used either as a standalone executable with input files or as a C++ library (API). This section covers the command-line interface (CLI) usage of the `xatu` binary.

Basic Command
=============

The program expects at least one file describing the system and a second file describing the excitonic properties.

For thigh-binding ``.model`` files, the command to execute is

.. code-block:: console

   xatu [OPTIONS] systemfile.model [excitonfile]
   

For thigh-binding-like ``_tb.dat`` Wannier90 hamiltonians, the command to execute is

.. code-block:: console

   xatu --w90 [filling] [OPTIONS] systemfile.model [excitonfile]
    
and have a mandatory ``[filling]`` parameter.

For DFT ``.outp`` CRYSTAL hamiltonians, the command to execute is

.. code-block:: console

   xatu --dft [ncells] [OPTIONS] systemfile.model [excitonfile]
    
You may optionally specify the number of unit cells to read.

Flags can be passed to modify the behavior and output of the simulation.

Available Options
=================

``-h, --help``  
Print a help message and exit.

``-s, --states nstates``  
Number of exciton states to compute and output (default: 8).

``-p, --precision decimals``  
Set the number of decimal places for energy output (default: 6).

``-d, --dft [ncells]``  
Indicate that the system file is in CRYSTAL output format. You may optionally specify the number of unit cells to read.

``-w, --w90 [filling]``  
Indicate that the system file is in Wannier90 output format. You must specify the number of filled bands.

``-eck, --energy / --eigenstates / --kwf``  
Flags to write exciton outputs:
* `-e`: energies
* `-c`: eigenvectors
* `-k`: reciprocal-space densities  
These can be combined: e.g., `-ek`.

``-r, --rswf [holeIndex] [-r ncells]``  
Write real-space wavefunction amplitudes. The hole index and number of unit cells can be specified.

``-s, --spin``  
Compute the total spin of each exciton. Assumes spin is part of the basis.

``-a, --absorption``  
Compute the optical conductivity using the Kubo formalism. Requires `kubo_w.in` input file in working directory.

``-m, --method diag | davidson | sparse``  
Choose BSE solver. Options:
* `diag`: full diagonalization (default)
* `davidson`: iterative Davidson method
* `sparse`: sparse Lanczos method

``-b, --bands kpointsfile``  
Diagonalize the Bloch Hamiltonian at k-points specified in a file. Does not compute excitons.

``-f, --format model | hdf5``  
Specify format of the system file. Defaults to `model`. Note: HDF5 support requires compilation with `HDF5=1`.

Examples
========

Run with default output for 8 exciton states:

.. code-block:: bash

   xatu system.model exciton.in

Run with custom number of states and output eigenstates and absorption:

.. code-block:: bash

   xatu -s 10 -cek -a system.model exciton.in

Run with DFT input and extract real-space amplitudes:

.. code-block:: bash

   xatu -d 3 -r 2 -r 10 system.dft exciton.in
