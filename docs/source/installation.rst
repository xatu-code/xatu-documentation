============
Installation
============

Xatu is written in C++ (with a Fortran module for the optical conductivity). It is built on the
`Armadillo <https://arma.sourceforge.net>`_ linear-algebra library, which in turn uses BLAS, LAPACK and
ARPACK.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Dependency
     - Needed for
   * - Armadillo
     - everything (linear algebra)
   * - OpenBLAS, LAPACK
     - BLAS/LAPACK back end of Armadillo
   * - ARPACK
     - the ``sparse`` BSE solver
   * - ``g++`` and ``gfortran`` with OpenMP
     - compiling
   * - HDF5 *(optional)*
     - reading system files in HDF5 format

Get the code
============

.. code-block:: bash

   git clone https://github.com/xatu-code/xatu.git
   cd xatu

Install the dependencies
========================

.. tab-set::

   .. tab-item:: Ubuntu / Debian / WSL

      .. code-block:: bash

         sudo apt-get install g++ gfortran libopenblas-dev liblapack-dev libarpack2-dev libarmadillo-dev

      The default ``Makefile`` works as is.

   .. tab-item:: macOS (Homebrew)

      .. code-block:: bash

         brew install gcc openblas lapack arpack armadillo

      Then point the ``Makefile`` to Homebrew's compiler and libraries. Adjust ``g++-13`` to the
      version you have installed:

      .. code-block:: makefile

         CC = g++-13
         INCLUDE = -I$(PWD)/include -I/opt/homebrew/include -I/opt/homebrew/opt/openblas/include
         LIBS = -DARMA_DONT_USE_WRAPPER -L$(PWD) -L/opt/homebrew/lib -L/opt/homebrew/opt/openblas/lib -lxatu -larmadillo -lopenblas -llapack -fopenmp -lgfortran -larpack

   .. tab-item:: Manual build

      If a library is not available from a package manager, build it from source. For example,
      Armadillo:

      .. code-block:: bash

         git clone https://gitlab.com/conradsnicta/armadillo-code.git
         cd armadillo-code
         cmake .
         make install

      Then add its paths to the ``Makefile``:

      .. code-block:: makefile

         INCLUDE = -I/path/to/armadillo/include -I/path/to/OpenBLAS/include
         LIBS = -L/path/to/OpenBLAS/lib

Build Xatu
==========

Building takes two steps. First build the library (``libxatu.a``), then the program:

.. code-block:: bash

   make build
   make xatu

The ``xatu`` executable is placed in ``bin/``. Check that it runs:

.. code-block:: bash

   bin/xatu --help

Your own programs using the Xatu library go in ``main/``. Each is compiled by name, e.g.
``main/my_script.cpp`` with:

.. code-block:: bash

   make my_script

Build options
-------------

Options are passed to every ``make`` call (``build``, ``xatu`` and your own scripts) and can be combined.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Option
     - Effect
   * - ``HDF5=1``
     - Enables HDF5 system files (``-f hdf5``). Needs ``libhdf5-dev`` (Ubuntu) or ``hdf5`` (Homebrew).
   * - ``DEBUG=1``
     - Builds without optimizations, for debugging.

.. code-block:: bash

   make build HDF5=1 DEBUG=1
   make xatu  HDF5=1 DEBUG=1

Parallelism
===========

Xatu is parallelized with OpenMP. Set the number of threads before running:

.. code-block:: bash

   export OMP_NUM_THREADS=8

Next step
=========

Run the :doc:`quickstart` to check the installation and see what Xatu produces.
