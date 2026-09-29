================================
Inverse Dielectric Matrix Output
================================

Xatu computes the inverse RPA dielectric matrix if the ``-z`` flag enabling the screening functionalities is provided and the user passes either one of the functions `inversedielectric` or `exciton` in the screening input file.
If the function `exciton` is used, then a file with the format ``kgrid_*.dat`` containing all the momentum vectors in the BZ mesh is created, alongside the file containing the inverse dielectric matrix.
The file containing all the generated matrix elements has the format ``*_invpesilon.dat``.

Structure of ``*_invepsilon.dat``
=================================

If the function `inversedielectric` is used, then only a single inverse dielectric matrix is printed with the structure:

 .. code-block:: text

      Re(G0G0)  Im(G0G0)  Re(G0G1)  Im(G0G1)  ...  Re(G0Gn)  Im(G0Gn)
      .
      .
      .
      Re(G1G0)  Im(G1G0)  Re(G1G1)  Im(G1G1)  ...  Re(G1Gn)  Im(G1Gn)

where *n-1* is the total number of :math:`\bm{G}`-vectors (including the null one). They are sorted by the same order as they are printed when running Xatu.

If the function `exciton` is used, then the inverse dielectric matrix in the entire BZ mesh is printed into the ``*_invpesilon.dat`` file with a table format, with the structure:

.. code-block:: text

      Re(q0G0G0)  Im(q0G0G0)  Re(q0G0G1)  Im(q0G0G1)  ...  Re(q0G0Gn)  Im(q0G0Gn)
      .
      .
      .
      Re(q0GnG0)  Im(q0GnG0)  Re(q0GnG1)  Im(q0GnG1)  ...  Re(q0GnGn)  Im(q0GnGn)
      Re(q1G0G0)  Im(q1G0G0)  Re(q1G0G1)  Im(q1G0G1)  ...  Re(q1G0Gn)  Im(q1G0Gn)
      .
      .
      .
      Re(q1GnG0)  Im(q1GnG0)  Re(q1GnG1)  Im(q1GnG1)  ...  Re(q1GnGn)  Im(q1GnGn)
      .
      .
      .
      Re(qNG0G0)  Im(qNG0G0)  Re(qNG0G1)  Im(qNG0G1)  ...  Re(qNG0Gn)  Im(qNG0Gn)
      .
      .
      .
      Re(qNGnG0) Im(qNGnG0)  Re(qNGnG1)  Im(qNGnG1)  ...  Re(qNGnGn)  Im(qNGnGn)

where *N-1* is the total number of :math:`\bm{q}`-points in the BZ mesh.
The table has *2(n-1)* columns and *n-1* rows for each :math:`\bm{q}`-point.
The :math:`\bm{G}`-vectors are sorted by the same order as they are printed when running Xatu, and the :math:`\bm{q}`-points are sorted in the same order as they appear in the ``kgrid_*.dat`` file.

The method ``ExcitonTB::readInverseDielectricMatrix(std::string filename)`` provided in the Xatu library can be used to read the inverse dielectric matrix from a file with the name ``filename`` containing a previously computed one in the same format.
In this way, the user can repeat an exciton calculation with different parameters (e.g., different BSE solver or regularization scheme) without having to recompute the inverse dielectric matrix.
For an example of its use in a script, see the ``read_screening.cpp`` file in the main folder of the project's repository.

**Pro tip**: Using the Xatu as an API tool, the user can also use any language of their preference to read the inverse dielectric matrix, invert it to obtain the dielectric matrix and reduce it, and invert it once again if the user wishes to compute the exciton with a smaller ``Gcutoff`` without having to recompute the inverse dielectric matrix.

**Pro tip**: Using the Xatu as an API tool, the user can start with a previously computed inverse dielectric matrix by reading it from a file and augment it with the method ``ExcitonTB::augment_2D_DielectricMatrix(double Gcutoff)`` upon passing a larger ``Gcutoff`` value. In this way, only the missing matrix elements will be computed, without the need to recompute the entire inverse dielectric matrix from scratch. For this, the method ``ExcitonTB::augment_2D_DielectricMatrix(double Gcutoff)`` has to be called after a succesful call of ``ExcitonTB::readInverseDielectricMatrix(std::string filename)``.


Structure of ``kgrid_*.dat``
============================

The file contains a table with one row per k-point and one column per each momentum component:

.. code-block:: text

   qx0 qy0 qz0
   qx1 qy1 qz1
   .
   .
   .
   qxN qyN qzN