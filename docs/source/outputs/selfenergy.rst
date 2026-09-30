===================================
.selfenergy — band self-energy
===================================

Written with ``-i`` (``--printSelfEnergy``). It gives the self-energy correction
:math:`\Sigma_n(\bm{k})` to each band of the BSE window at each k-point (see :doc:`../methods/BSE`).
The correction is only non-zero when ``# selfenergy true`` is set in the exciton file.

Format
======

One line per k-point:

.. code-block:: text

   kx   ky   kz   Re(S_1)   Im(S_1)   Re(S_2)   Im(S_2)   ...

* ``kx ky kz``: k-point, in the same units as the ``.states`` file.
* ``S_n``: correction to band :math:`n` of the window (eV), in the order of the band list, valence
  bands first.

There are :math:`3 + 2N_\text{bands}` columns. Adding :math:`\mathrm{Re}\,\Sigma_n(\bm{k})` to the band
energies gives the corrected bands used in the BSE.
