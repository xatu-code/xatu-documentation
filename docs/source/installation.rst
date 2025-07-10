====================
Installation Guide
====================

Xatu is built upon the Armadillo C++ library for linear algebra, which in turn depends on BLAS, LAPACK, and ARPACK. Below you will find instructions for installing Xatu on various platforms.

.. contents::
   :local:
   :depth: 2

Dependencies
============
Required libraries:
- Armadillo
- OpenBLAS
- LAPACK
- ARPACK

Optional:
- HDF5 (for using HDF5-format input files)

Ubuntu / Debian / WSL
======================

Install required packages via APT:

.. code-block:: bash

   sudo apt-get install libopenblas-dev liblapack-dev libarpack2-dev libarmadillo-dev

To build the Xatu library:

.. code-block:: bash

   make build

Then, to build the main Xatu binary:

.. code-block:: bash

   make xatu

To compile a custom script placed in the ``/main`` directory:

.. code-block:: bash

   make [script_name]

macOS
=====

Install dependencies via Homebrew:

.. code-block:: bash

   brew install gcc openblas lapack arpack armadillo

Edit your Makefile to set the appropriate compiler and library paths:

.. code-block:: makefile

   CC = g++-13
   INCLUDE = -I$(PWD)/include -I/opt/homebrew/include -I/opt/homebrew/opt/openblas/include
   LIBS = -DARMA_DONT_USE_WRAPPER -L$(PWD) -L/opt/homebrew/lib -L/opt/homebrew/opt/openblas/lib \
          -lxatu -larmadillo -lopenblas -llapack -fopenmp -lgfortran -larpack

General Instructions (Manual Build)
===================================

If the required libraries are not available via package managers, you can install them manually.

Example (Armadillo):

.. code-block:: bash

   git clone https://gitlab.com/conradsnicta/armadillo-code.git
   cd armadillo-code
   cmake .
   make install

Update the Makefile with the relevant paths:

.. code-block:: makefile

   INCLUDE = -I/path/to/armadillo/include -I/path/to/OpenBLAS/include
   LIBS = -L/path/to/OpenBLAS/lib

Enabling HDF5 Support
=====================

Install HDF5 libraries:

.. code-block:: bash

   # Ubuntu
   sudo apt-get install libhdf5-dev

   # macOS
   brew install hdf5

Compile with HDF5 support:

.. code-block:: bash

   make build HDF5=1
   make xatu HDF5=1
   make [script_name] HDF5=1

Enabling Debug Mode
====================

To build in debug mode, which disables compiler optimizations:

.. code-block:: bash

   make build DEBUG=1
   make xatu DEBUG=1
   make [script_name] DEBUG=1

You can also combine flags:

.. code-block:: bash

   make build HDF5=1 DEBUG=1
