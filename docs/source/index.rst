.. Xatu documentation master file,
   G. J. Inacio

=======================================================
Xatu: eXcitons from ATomistic calcUlations
=======================================================

Xatu is a computational package and library for solving the Bethe-Salpeter Equation (BSE) in condensed matter systems. It allows efficient and flexible exciton calculations starting from electronic structures obtained via tight-binding or DFT using localized orbitals.

The BSE is constructed from user-defined input and then diagonalized to obtain the excitonic spectrum. The results can be post-processed to extract physical properties such as optical absorption and exciton localization.

For more information, see our paper:  
`Efficient computation of optical excitations in two-dimensional materials with the Xatu code <https://doi.org/10.1016/j.cpc.2023.109001>`_.

.. image:: hbn_xatu_example.png
   :width: 90%
   :align: center

Documentation Contents
=======================

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   input_files
   usage

.. toctree::
   :maxdepth: 2
   :caption: Theory and Methods

   methods/screening
   methods/bse
   methods/optical_properties

.. toctree::
   :maxdepth: 1
   :caption: Developer Reference

   api
   contributing
   changelog

.. toctree::
   :maxdepth: 1
   :caption: Miscellaneous

   citing
   license
