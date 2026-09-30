=========================================
.rswf — real-space probability density
=========================================

Written with ``-r <hole> [-r <ncells>]`` for each of the ``-n`` excitons. The hole is fixed on atom
``<hole>`` of the motif (in the home cell), and the file gives the probability of finding the electron on
each atom of the surrounding ``<ncells>`` unit cells (default 8):

.. math::

   P(\bm{r}_e) = \sum_{\alpha \in \bm{r}_e} \left|\psi_X(\bm{r}_e \alpha, \bm{r}_h)\right|^2 ,

summed over the orbitals :math:`\alpha` on the atom at :math:`\bm{r}_e`.

Format
======

One block per exciton, closed by ``#``. The first line of each block is the hole position, then one
line per atom:

.. code-block:: text

   xh   yh   0               <- hole position (Angstrom)
   x    y    P               <- one line per atom
   ...
   #

Positions are in Angstrom. Plot with ``plot/rswf.py``, or see the right panel of the figure on
:doc:`kwf`.
