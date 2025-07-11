.. Xatu documentation master file,
   G. J. Inacio

.. _Xatu: https://github.com/xatu-code/xatu
.. _xatu_paper: 

=======================================================
Xatu: eXcitons from ATomistic calcUlations
=======================================================

`Xatu`_ is a computational package and library for solving the Bethe-Salpeter Equation (BSE) in condensed matter systems. It allows efficient and flexible exciton calculations starting from electronic structures obtained via tight-binding or DFT using localized orbitals.

The BSE is constructed from user-defined input and then diagonalized to obtain the excitonic spectrum. The results can be post-processed to extract physical properties such as optical absorption and exciton localization.

.. note::

   📄 **Reference Paper:**   
   `Efficient computation of optical excitations in two-dimensional materials with the Xatu code, Computer Physics Communications, 2024 <https://doi.org/10.1016/j.cpc.2023.109001>`_



.. image:: images/hbn_xatu_example.png
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
   :caption: Outputs

   outputs/eigval
   outputs/states
   outputs/kwf
   outputs/rswf
   outputs/conductivity
   outputs/spin

.. toctree::
   :maxdepth: 2
   :caption: Theory and Methods

   methods/screening
   methods/BSE
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