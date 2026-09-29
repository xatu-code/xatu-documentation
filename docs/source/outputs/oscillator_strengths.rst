================================================
Oscillator strengths (``*_ex_osc.dat``)
================================================

Written with ``-a``, next to the excitonic conductivity. The name is the excitonic file name of
``kubo_w.in`` with ``_osc`` inserted before the extension (``hBN_ex.dat`` → ``hBN_ex_osc.dat``). It lists
the velocity matrix element between the ground state and **every** exciton of the BSE, which is what
sets each exciton's brightness.

Format
======

One line per exciton, in order of energy. There are as many lines as the BSE dimension, independent
of ``-n``:

.. code-block:: text

   E      Re(Vx)   Im(Vx)   Re(Vy)   Im(Vy)   Re(Vz)   Im(Vz)

* ``E``: exciton energy :math:`E_X` (eV).
* ``V``: velocity matrix element :math:`V^a_X = \langle GS|\hat v^a|X\rangle` along :math:`a = x,y,z`, in
  atomic units.

Excitons with :math:`V_X \approx 0` are dark. The conductivity of :doc:`conductivity` is

.. math::

   \sigma^{ab}(\omega) \propto \sum_X \frac{(V^a_X)^*\,V^b_X}{E_X}\,\delta(\hbar\omega - E_X),

so :math:`|V^a_X|^2/E_X` is the weight of exciton :math:`X` in the absorption along :math:`a`.

Definition
==========

.. math::

   V^a_X = \sum_{v c \bm{k}} A_{vc}^X(\bm{k})\, v^a_{vc}(\bm{k}),
   \qquad
   v^a_{vc}(\bm{k}) = \langle v\bm{k}|\hat v^a|c\bm{k}\rangle
   = \frac{i}{\hbar}\langle v\bm{k}|[H_0,\hat r^a]|c\bm{k}\rangle ,

where :math:`A^X_{vc}(\bm{k})` are the exciton coefficients (:doc:`states`) and :math:`H_0` is the
single-particle Hamiltonian.

.. code-block:: python

   import numpy as np
   osc = np.loadtxt("hBN_ex_osc.dat")
   E = osc[:, 0]
   Vx = osc[:, 1] + 1j * osc[:, 2]
   bright = np.abs(Vx)**2 / E            # weight in σ^xx
