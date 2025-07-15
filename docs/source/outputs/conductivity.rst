======================================
Conductivity Outputs (.dat files)
======================================

Xatu computes the optical conductivity spectrum using both the independent-particle approximation (IPA) and the full Bethe-Salpeter equation (BSE). These are written to separate files during execution with the ``-a --absorption`` flag, provided that a valid `kubo_w.in` file is present.

Files Generated
===============

Three output files are created, tipically defined in `kubo_w.in` as:

* ``*_sp.dat`` : IPA (independent-particle) optical conductivity
* ``*_ex.dat`` : BSE (excitonic) optical conductivity
* ``*_osc.dat``: Exciton oscillator strengths (see :doc:`./oscillator_strengths`)

Structure of `*_sp.dat` and `*_ex.dat`
=======================================

Each file contains real parts of the conductivity tensor components for different photon energies:

.. code-block:: text 

   omega  xx   xy   xz   yx   yy   yz   zx   zy   zz
   .
   .
   .

**Units**

* :math:`\omega` : photon energy in **electron volts (eV)**

* ``ij`` is :math:`Re{\sigma_{ij}}` : real part of optical conductivity in units of :math:`e^{2}/\hbar`

**Post-processing**

These ``.dat`` files can be plotted directly using ``absorption.py`` at ``/plot/`` folder in Xatu repository.

**Related Files**

For oscillator strengths used in the excitonic conductivity calculation, see:

:doc:`./oscillator_strengths`