==========================
Developer and API Guide
==========================

While this documentation focuses on the usage of Xatu as a command-line tool, developers may also use it as a **library** to integrate excitonic calculations into other workflows.

The Xatu source code exposes key functionalities via a documented **C++ API**, intended for direct use in scientific software development.

API Documentation
===================

- Full API documentation is available and maintained using **Doxygen**
- To generate the API documentation:

.. code-block:: bash

   cd docs
   doxygen docs.cfg

This will produce a browsable HTML documentation of the internal structure and classes.

Code Structure Overview
=========================

The API is organized in a namespace, and its usage typically follows:

1. Create a ``System`` object using a system file or subclass it to define a custom Hamiltonian.
2. Pass the system to an ``Exciton`` object, which is then configured and solved.
3. Extract results from the ``Result`` object: eigenvalues, eigenvectors, and observables.

Example structure:

.. code-block:: cpp

   systemConfig.reset(new xatu::SystemConfiguration(systemfile))
   xatu::ExcitonTB bulkExciton = xatu::ExcitonTB(*systemConfig, *excitonConfig);
   ...
   [calls relevant methods]
   ...
   auto results = bulkExciton.diagonalize(method, nstates);

   auto eigvals = result.eigenvalues();
   auto eigvecs = result.eigenvectors();

- API header files are located under `include/`
- Example usages are available in the `main/` directory
