=======================
Using Xatu as a library
=======================

Besides the ``xatu`` program, Xatu is a C++ library (``libxatu.a``, built with ``make build``). Use it to
run excitons inside your own workflow, loop over parameters, or reach methods the command line does
not expose.

A minimal program
=================

Place your program in ``main/`` and compile it by name (``make my_program``, see
:doc:`../installation`). This example, ``main/minimal_example.cpp`` in the repository, computes the
excitons of hBN:

.. code-block:: cpp

   #include <armadillo>
   #include <xatu.hpp>

   using namespace xatu;

   int main(){
       int nbands   = 1;                           // valence and conduction bands
       int nrmbands = 0;                           // bands removed from the window
       int ncell    = 40;                          // k-points per direction
       arma::rowvec parameters = {1., 1., 10.};    // eps_s, eps_m, r0 (Keldysh)
       int nstates  = 8;

       auto config  = SystemConfiguration("./examples/material_models/hBN.model");
       auto exciton = ExcitonTB(config, ncell, nbands, nrmbands, parameters);

       exciton.brillouinZoneMesh(ncell);
       exciton.initializeHamiltonian();
       exciton.BShamiltonian();
       auto results = exciton.diagonalize("diag", nstates);

       return 0;
   }

The workflow is always the same:

1. **Configure the system** with a ``SystemConfiguration`` (or ``CRYSTALConfiguration``,
   ``Wannier90Configuration``, ``HDF5Configuration``), or subclass ``System`` for a custom
   Hamiltonian.
2. **Build the exciton**: an ``ExcitonTB``, from the system and either an ``ExcitonConfiguration``
   (exciton file) or explicit parameters. Setters such as ``setCutoff`` or ``setReciprocalVectors``
   change the parameters.
3. **Solve**: create the mesh, initialize the Hamiltonian, build the BSE matrix (``BShamiltonian``) and
   ``diagonalize``.
4. **Analyse** the returned result: energies (``results->eigval``), coefficients
   (``results->eigvec``), and the same writers the program uses (``writeEigenvalues``,
   ``writeStates``, ``writeAbsorptionSpectrum``, ...).

``main/xatu.cpp`` is the full command-line program and the most complete example. The other files in
``main/`` (``exciton_example.cpp``, and the screening scripts) show more specific uses.

API reference
=============

The classes and methods are documented in the headers under ``include/``, with Doxygen comments. To
build a browsable HTML reference:

.. code-block:: bash

   cd docs
   doxygen docs.cfg
