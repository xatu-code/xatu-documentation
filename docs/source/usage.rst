==================
Command-line usage
==================

The ``xatu`` binary takes a **system file** and an **exciton file**, plus optional flags:

.. code-block:: bash

   xatu [OPTIONS] systemfile [excitonfile]

The format of the system file sets how it is read:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - System file
     - Command
   * - Xatu model file (``.model``)
     - ``xatu [OPTIONS] system.model exciton.txt``
   * - HDF5 model file
     - ``xatu -f hdf5 [OPTIONS] system.hdf5 exciton.txt`` (needs an HDF5 build)
   * - CRYSTAL output (``.outp``)
     - ``xatu -d <ncells> [OPTIONS] system.outp exciton.txt``
   * - Wannier90 Hamiltonian (``_tb.dat``)
     - ``xatu -w <filling> [OPTIONS] system_tb.dat exciton.txt``

See :doc:`input_files/system` for each format.

Options
=======

Physics and input
-----------------

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Flag
     - Description
   * - ``-w, --w90 <filling>``
     - The system file is a Wannier90 ``_tb.dat``. ``<filling>`` is the number of filled bands and is
       **mandatory**, because the file does not contain it.
   * - ``-d, --dft <ncells>``
     - The system file is a CRYSTAL ``.outp``. Read the Fock and overlap matrices of the first
       ``<ncells>`` unit cells. The value is required.
   * - ``-f, --format model|hdf5``
     - Format of a Xatu system file. Default ``model``.
   * - ``-m, --method diag|davidson|sparse``
     - BSE solver: full diagonalization (default), iterative Davidson, or sparse Lanczos (ARPACK). The
       iterative solvers only compute the lowest ``-n`` states and are faster for large BSE matrices.
   * - ``-z, --screening <file>`` |scr|
     - Compute the microscopic RPA screening described in ``<file>`` (see
       :doc:`input_files/screening`). An exciton file is required too.
   * - ``-b, --bands <kpointsfile>``
     - Only compute the band structure at the k-points listed in ``<kpointsfile>`` (one ``kx ky kz`` per
       line), write the eigenvalues (eV, one row per k-point) to ``<kpointsfile>.bands``, and exit. No
       exciton file is needed.

What to write
-------------

Output files are named after the ``# label`` of the exciton file.

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Flag
     - Output
   * - ``-n, --states <n>``
     - Number of excitons printed and written to every output file. Default 8.
   * - ``-t, --ecut <E>`` |w90|
     - Instead of a fixed number, keep the excitons up to energy ``E`` (eV) in the terminal,
       ``.eigval``, ``.states`` and ``.spin`` output. Overrides ``-n`` for those outputs.
   * - ``-p, --precision <d>``
     - Decimals used to print energies and to decide which states are degenerate. Default 6.
   * - ``-e, --energy``
     - Exciton energies → :doc:`outputs/eigval`.
   * - ``-c, --eigenstates``
     - Exciton coefficients :math:`A_{vc}(\bm{k})` → :doc:`outputs/states`.
   * - ``-k, --kwf``
     - Reciprocal-space densities → :doc:`outputs/kwf`.
   * - ``-r, --rswf <hole> [-r <ncells>]``
     - Real-space densities with the hole on atom ``<hole>`` of the motif, over ``<ncells>`` unit cells
       (default 8) → :doc:`outputs/rswf`. Give ``-r`` twice to set both, e.g. ``-r 0 -r 10``.
   * - ``-s, --spin``
     - Spin of each exciton → :doc:`outputs/spin`. Spin must be part of the orbital basis.
   * - ``-a, --absorption``
     - Optical conductivity with and without excitons, and oscillator strengths →
       :doc:`outputs/conductivity`. Reads ``kubo_w.in`` (see :doc:`input_files/absorption`).
   * - ``-h, --help``
     - Print the help and exit.

Examples
========

Energies of the lowest 8 excitons (the defaults):

.. code-block:: bash

   xatu -e system.model exciton.txt

Ten excitons, with eigenstates, k-space densities, absorption and energies:

.. code-block:: bash

   xatu -n 10 -kace system.model exciton.txt

Wannier90 Hamiltonian with 8 filled bands, keeping every exciton below 3 eV |w90|:

.. code-block:: bash

   xatu -w 8 -t 3.0 -e -c MoS2_tb.dat exciton.txt

CRYSTAL calculation reading 50 cells, real-space wavefunction with the hole on atom 2, over 10 cells:

.. code-block:: bash

   xatu -d 50 -r 2 -r 10 hBN.outp exciton.txt

Large BSE with the Davidson solver:

.. code-block:: bash

   xatu -m davidson -n 20 -e system.model exciton.txt

Exciton with the RPA-screened interaction |scr|:

.. code-block:: bash

   xatu -d 50 -z screening.txt -e hBN.outp exciton.txt
