======================================
Conductivity Outputs (.dat files)
======================================

Xatu computes the optical conductivity spectrum using both the independent-particle approximation (IPA) and the full Bethe-Salpeter equation (BSE). These are written to separate files during execution with the ``-a --absorption`` flag, provided that a valid `kubo_w.in` file is present.

Files Generated
===============

Three output files are created, tipically defined in `kubo_w.in` as:

- ``*_sp.dat`` — IPA (independent-particle) optical conductivity
- ``*_ex.dat`` — BSE (excitonic) optical conductivity
- ``*_osc.dat`` — Exciton oscillator strengths (see :doc:`../methods/optical_properties`)

Structure of `*_sp.dat` and `*_ex.dat`
=======================================

Each file contains real parts of the conductivity tensor components for different photon energies:

.. code-block:: text

   # omega (eV)   Re[$\sigma_{$_xx}]   Re[$\sigma_{$_xy}]   Re[$\sigma_{$_xz}]   Re[$\sigma_{$_yx}]   Re[$\sigma_{$_yy}]   Re[$\sigma_{$_yz}]   Re[$\sigma_{$_zx}]   Re[$\sigma_{$_zy}]   Re[$\sigma_{$_zz}]
   ...

Units
======

- $ \omega $: photon energy in **electron volts (eV)**
- $ \sigma_{ij} $: real part of optical conductivity in units of $ \frac{e^2}{\hbar} $

Post-processing
================

These `.dat` files can be plotted directly using ``absorption.py`` at ``/plot/`` folder in Xatu repository.

Related Files
=============

For oscillator strengths used in the excitonic conductivity calculation, see:

:doc:`../methods/oscillator_strengths`

