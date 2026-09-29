===========
Input files
===========

A Xatu run reads up to four files:

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: System file
      :link: input_files/system
      :link-type: doc

      The crystal and its single-particle Hamiltonian: a Xatu ``.model`` file, HDF5, a CRYSTAL
      ``.outp`` or a Wannier90 ``_tb.dat``. **Always required.**

   .. grid-item-card:: Exciton file
      :link: input_files/exciton
      :link-type: doc

      k-mesh, bands, interaction potential and other BSE parameters. **Required** except for
      band-structure runs (``-b``).

   .. grid-item-card:: Screening file |scr|
      :link: input_files/screening
      :link-type: doc

      Parameters of the microscopic RPA screening. Only with ``-z``.

   .. grid-item-card:: kubo_w.in
      :link: input_files/absorption
      :link-type: doc

      Frequency window and broadening of the optical conductivity. Only with ``-a``.

Common syntax
=============

The system, exciton and screening files share one simple block format:

.. code-block:: text

   # keyword
   value(s)
   # another keyword
   value(s)

* A line containing ``#`` starts a new block. The keyword is the text after it, and it is **case
  insensitive with spaces ignored**: ``# Bravais Lattice``, ``#bravaislattice`` and ``## BravaisLattice``
  are the same.
* Lines containing ``!`` are comments and are skipped:

  .. code-block:: text

     # ncells
     ! number of k-points along each direction
     30

* Values on a line can be separated by spaces, commas or semicolons.
* Empty lines are ignored.
* Unknown keywords are skipped with a message (``Unexpected argument: ..., skipping block...``).
* Except for matrices and lists of vectors, each block holds a single line.

.. tip::

   Working examples of every file are in the ``examples/`` folder of the Xatu repository:
   ``material_models/``, ``excitonconfig/``, ``screeningconfig/``, and ``kubo_w.in`` at the top level.

.. toctree::
   :hidden:

   input_files/system
   input_files/exciton
   input_files/screening
   input_files/absorption
