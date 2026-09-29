==================================
.spin — exciton spin projection
==================================

Written with ``-s``. It needs a basis with explicit spin, **ordered with spin as the fastest index**:
each orbital appears twice in a row, first :math:`\uparrow` then :math:`\downarrow`
(:math:`1\!\uparrow, 1\!\downarrow, 2\!\uparrow, 2\!\downarrow, \dots`). Xatu stops with an error if
the basis dimension is odd.

Format
======

.. code-block:: text

   n    St    Se    Sh
   0    ...   ...   ...
   1    ...   ...   ...

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Column
     - Meaning
   * - ``n``
     - Exciton index, from 0.
   * - ``St``
     - Total spin projection, ``St = Se + Sh``.
   * - ``Se``
     - Spin projection :math:`\langle s_z\rangle` of the electron (conduction bands).
   * - ``Sh``
     - Spin projection of the hole. This is **minus** the spin of the missing valence electron.

All values are in units of :math:`\hbar`. There are ``-n`` lines, or those up to ``-t`` |w90|.

Definition
==========

At each k-point, Xatu builds the :math:`S_z` operator in the space of the valence bands and in that of
the conduction bands, and takes its expectation value in the exciton state
(`Xatu paper <https://doi.org/10.1016/j.cpc.2023.109001>`_, Eqs. 30–31). If :math:`S_z` is a good
quantum number of the bands, with :math:`\sigma_n = \pm 1/2`, this reduces to

.. math::

   \langle S_z^T\rangle = \sum_{v,c,\bm{k}} |A_{vc}(\bm{k})|^2\,(\sigma_c - \sigma_v) .

With spin–orbit coupling that mixes the spins, the values are no longer multiples of 1/2 but remain
well-defined expectation values.
