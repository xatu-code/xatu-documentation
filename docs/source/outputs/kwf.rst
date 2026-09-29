============================================
.kwf — momentum-space probability density
============================================

Written with ``-k``, for each of the ``-n`` excitons. It gives the weight of the exciton on each
k-point, summed over bands:

.. math::

   |\psi_X(\bm{k})|^2 = \sum_{v,c} |A_{vc}(\bm{k})|^2 .

Format
======

One block per exciton, each closed by a line with ``#``:

.. code-block:: text

   kx   ky   kz   P          <- exciton 1
   ...
   #
   kx   ky   kz   P          <- exciton 2
   ...
   #

* ``kx ky kz``: k-point in Å⁻¹.
* ``P``: :math:`|\psi_X(\bm{k})|^2`, divided by the spacing between k-points.

For a full-zone mesh, the density is **repeated over neighbouring Brillouin zones** to fill a
square box around Γ. This makes plots of hexagonal zones easier to read. With ``# submesh``, only
the mesh itself is written, and each block starts with a ``kx ky kz Prob.`` header line.

.. image:: ../images/hbn_wavefunctions.png
   :width: 100%
   :align: center

Plot with ``plot/kwf.py`` from the repository, or:

.. code-block:: python

   import numpy as np, matplotlib.pyplot as plt
   blocks = open("hBN_N30.kwf").read().split("#")[:-1]
   k = np.loadtxt(blocks[0].splitlines())        # first exciton
   plt.scatter(k[:, 0], k[:, 1], c=k[:, 3], s=5); plt.gca().set_aspect("equal")
