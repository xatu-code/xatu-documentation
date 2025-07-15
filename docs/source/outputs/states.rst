==============================
.states — Exciton Eigenstates
==============================

The ``.states`` file (written with the ``-c`` / ``--eigenstates`` flag) contains the **complex coefficients**  
:math:`A^{Q}_{vc}(\mathbf{k})` that define each exciton wavefunction in the electron–hole basis.  
These are exactly the amplitudes that appear in the Bethe‑Salpeter Equation (see Eq. 14 of the paper):

.. math::

   (\varepsilon_{c,\mathbf{k+Q}} - \varepsilon_{v,\mathbf{k}})
   A^{Q}_{vc}(\mathbf{k})
   + \sum_{v'c'\mathbf{k}'} K_{vc,v'c'}(\mathbf{k},\mathbf{k}',Q)\,
     A^{Q}_{v'c'}(\mathbf{k}')
   \;=\; E_X\,A^{Q}_{vc}(\mathbf{k})

File Structure
==============

1. **Header line**

   .. code-block:: text

      n_pairs

   The dimension ``n_pairs`` of the BSE matrix -- i.e. the total number of distinct  
   electron-hole pairs :math:`(v,c,\mathbf{k})` used for the calculation.

2. **Basis definition (next ``n_pairs`` lines)**

   Each line lists one electron–hole pair in the exact order used later for the coefficients:

   .. code-block:: text 

      k_x   k_y   k_z   v   c

   :math:`k_x\quad   k_y\quad   k_z\quad` are given in crystal‑momentum units (fractional coordinates or :math:`Å^{-1}`,  
   depending on input), $v$ and $c$ are valence and conduction band indices.

3. **Exciton coefficient matrix**

   After the basis section, each remaining line corresponds to **one exciton state**.  
   The coefficients are written as consecutive real–imaginary pairs following the same
   ordering of electron–hole pairs defined above:

   .. code-block:: text

      Re(A1)  Im(A1)  Re(A2)  Im(A2)  ...  Re(An)  Im(An)
      .
      .
      .
      Re(A1)  Im(A1)  Re(A2)  Im(A2)  ...  Re(An)  Im(An)


   where *n = n_pairs*.  
   If you requested `N` exciton states with ``--states N`` (*default=8*), there will be `N` such lines.

Properties
==========

* **Normalization**  
  Each row is normalized so that  
  :math:`\sum_{j=1}^{n_{\mathrm{pairs}}} |A_j|^2 = 1`.

* **Complex ordering**  
  The $j$-th complex pair in a row corresponds to the $j$-th electron–hole pair  
  listed in the basis definition.  This one‑to‑one mapping makes it straightforward  
  to reconstruct the wavefunction in k‑space or transform it to real space.

* **Units**  
  The coefficients are dimensionless.

.. Typical Use Cases
.. =================

.. * Build the k‑space probability density :math:`|\psi_X(\mathbf{k})|^2`
..   (written automatically to ``.kwf`` when using ``-k``).
.. * Reconstruct the real‑space wavefunction (``.rswf``) for visualization.
.. * Analyse band‑resolved or spin‑resolved content of a particular exciton.
.. * Feed the coefficients into custom post‑processing scripts for exciton–phonon
..   coupling, nonlinear optics, etc.

