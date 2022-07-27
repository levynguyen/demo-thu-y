# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Math Operations.

Note: Functions taking `Tensor` arguments can also take anything accepted by
`tf.convert_to_tensor`.

Note: Elementwise binary operations in TensorFlow follow [numpy-style
broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

TensorFlow provides a variety of math functions including:

* Basic arithmetic operators and trigonometric functions.
* Special math functions (like: `tf.math.igamma` and `tf.math.zeta`)
* Complex number functions (like: `tf.math.imag` and `tf.math.angle`)
* Reductions and scans (like: `tf.math.reduce_mean` and `tf.math.cumsum`)
* Segment functions (like: `tf.math.segment_sum`)

See: `tf.linalg` for matrix and tensor functions.

<a id=Segmentation></a>

## About Segmentation

TensorFlow provides several operations that you can use to perform common
math computations on tensor segments.
Here a segmentation is a partitioning of a tensor along
the first dimension, i.e. it  defines a mapping from the first dimension onto
`segment_ids`. The `segment_ids` tensor should be the size of
the first dimension, `d0`, with consecutive IDs in the range `0` to `k`,
where `k<d0`.
In particular, a segmentation of a matrix tensor is a mapping of rows to
segments.

For example:

```python
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
tf.math.segment_sum(c, tf.constant([0, 0, 1]))
#  ==>  [[0 0 0 0]
#        [5 6 7 8]]
```

The standard `segment_*` functions assert that the segment indices are sorted.
If you have unsorted indices use the equivalent `unsorted_segment_` function.
These functions take an additional argument `num_segments` so that the output
tensor can be efficiently allocated.

``` python
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
tf.math.unsorted_segment_sum(c, tf.constant([0, 1, 0]), num_segments=2)
# ==> [[ 6,  8, 10, 12],
#       [-1, -2, -3, -4]]
```


"""

from __future__ import print_function as _print_function

import sys as _sys

from . import special
from tensorflow.python.ops.bincount_ops import bincount
from tensorflow.python.ops.check_ops import is_non_decreasing
from tensorflow.python.ops.check_ops import is_strictly_increasing
from tensorflow.python.ops.confusion_matrix import confusion_matrix
from tensorflow.python.ops.gen_array_ops import invert_permutation
from tensorflow.python.ops.gen_math_ops import acosh
from tensorflow.python.ops.gen_math_ops import asin
from tensorflow.python.ops.gen_math_ops import asinh
from tensorflow.python.ops.gen_math_ops import atan
from tensorflow.python.ops.gen_math_ops import atan2
from tensorflow.python.ops.gen_math_ops import atanh
from tensorflow.python.ops.gen_math_ops import betainc
from tensorflow.python.ops.gen_math_ops import cos
from tensorflow.python.ops.gen_math_ops import cosh
from tensorflow.python.ops.gen_math_ops import digamma
from tensorflow.python.ops.gen_math_ops import erf
from tensorflow.python.ops.gen_math_ops import erfc
from tensorflow.python.ops.gen_math_ops import expm1
from tensorflow.python.ops.gen_math_ops import floor_mod as floormod
from tensorflow.python.ops.gen_math_ops import floor_mod as mod
from tensorflow.python.ops.gen_math_ops import greater
from tensorflow.python.ops.gen_math_ops import greater_equal
from tensorflow.python.ops.gen_math_ops import igamma
from tensorflow.python.ops.gen_math_ops import igammac
from tensorflow.python.ops.gen_math_ops import is_finite
from tensorflow.python.ops.gen_math_ops import is_inf
from tensorflow.python.ops.gen_math_ops import is_nan
from tensorflow.python.ops.gen_math_ops import less
from tensorflow.python.ops.gen_math_ops import less_equal
from tensorflow.python.ops.gen_math_ops import lgamma
from tensorflow.python.ops.gen_math_ops import log
from tensorflow.python.ops.gen_math_ops import log1p
from tensorflow.python.ops.gen_math_ops import logical_and
from tensorflow.python.ops.gen_math_ops import logical_not
from tensorflow.python.ops.gen_math_ops import logical_or
from tensorflow.python.ops.gen_math_ops import maximum
from tensorflow.python.ops.gen_math_ops import minimum
from tensorflow.python.ops.gen_math_ops import neg as negative
from tensorflow.python.ops.gen_math_ops import next_after as nextafter
from tensorflow.python.ops.gen_math_ops import polygamma
from tensorflow.python.ops.gen_math_ops import reciprocal
from tensorflow.python.ops.gen_math_ops import rint
from tensorflow.python.ops.gen_math_ops import segment_max
from tensorflow.python.ops.gen_math_ops import segment_mean
from tensorflow.python.ops.gen_math_ops import segment_min
from tensorflow.python.ops.gen_math_ops import segment_prod
from tensorflow.python.ops.gen_math_ops import segment_sum
from tensorflow.python.ops.gen_math_ops import sin
from tensorflow.python.ops.gen_math_ops import sinh
from tensorflow.python.ops.gen_math_ops import square
from tensorflow.python.ops.gen_math_ops import squared_difference
from tensorflow.python.ops.gen_math_ops import tan
from tensorflow.python.ops.gen_math_ops import tanh
from tensorflow.python.ops.gen_math_ops import unsorted_segment_max
from tensorflow.python.ops.gen_math_ops import unsorted_segment_min
from tensorflow.python.ops.gen_math_ops import unsorted_segment_prod
from tensorflow.python.ops.gen_math_ops import unsorted_segment_sum
from tensorflow.python.ops.gen_math_ops import xdivy
from tensorflow.python.ops.gen_math_ops import xlogy
from tensorflow.python.ops.gen_math_ops import zeta
from tensorflow.python.ops.gen_nn_ops import softsign
from tensorflow.python.ops.math_ops import abs
from tensorflow.python.ops.math_ops import accumulate_n
from tensorflow.python.ops.math_ops import acos
from tensorflow.python.ops.math_ops import add
from tensorflow.python.ops.math_ops import add_n
from tensorflow.python.ops.math_ops import angle
from tensorflow.python.ops.math_ops import argmax_v2 as argmax
from tensorflow.python.ops.math_ops import argmin_v2 as argmin
from tensorflow.python.ops.math_ops import ceil
from tensorflow.python.ops.math_ops import conj
from tensorflow.python.ops.math_ops import count_nonzero_v2 as count_nonzero
from tensorflow.python.ops.math_ops import cumprod
from tensorflow.python.ops.math_ops import cumsum
from tensorflow.python.ops.math_ops import cumulative_logsumexp
from tensorflow.python.ops.math_ops import div_no_nan as divide_no_nan
from tensorflow.python.ops.math_ops import divide
from tensorflow.python.ops.math_ops import equal
from tensorflow.python.ops.math_ops import erfcinv
from tensorflow.python.ops.math_ops import erfinv
from tensorflow.python.ops.math_ops import exp
from tensorflow.python.ops.math_ops import floor
from tensorflow.python.ops.math_ops import floordiv
from tensorflow.python.ops.math_ops import imag
from tensorflow.python.ops.math_ops import log_sigmoid
from tensorflow.python.ops.math_ops import logical_xor
from tensorflow.python.ops.math_ops import multiply
from tensorflow.python.ops.math_ops import multiply_no_nan
from tensorflow.python.ops.math_ops import ndtri
from tensorflow.python.ops.math_ops import not_equal
from tensorflow.python.ops.math_ops import polyval
from tensorflow.python.ops.math_ops import pow
from tensorflow.python.ops.math_ops import real
from tensorflow.python.ops.math_ops import reciprocal_no_nan
from tensorflow.python.ops.math_ops import reduce_all
from tensorflow.python.ops.math_ops import reduce_any
from tensorflow.python.ops.math_ops import reduce_euclidean_norm
from tensorflow.python.ops.math_ops import reduce_logsumexp
from tensorflow.python.ops.math_ops import reduce_max
from tensorflow.python.ops.math_ops import reduce_mean
from tensorflow.python.ops.math_ops import reduce_min
from tensorflow.python.ops.math_ops import reduce_prod
from tensorflow.python.ops.math_ops import reduce_std
from tensorflow.python.ops.math_ops import reduce_sum
from tensorflow.python.ops.math_ops import reduce_variance
from tensorflow.python.ops.math_ops import round
from tensorflow.python.ops.math_ops import rsqrt
from tensorflow.python.ops.math_ops import scalar_mul_v2 as scalar_mul
from tensorflow.python.ops.math_ops import sigmoid
from tensorflow.python.ops.math_ops import sign
from tensorflow.python.ops.math_ops import sobol_sample
from tensorflow.python.ops.math_ops import softplus
from tensorflow.python.ops.math_ops import sqrt
from tensorflow.python.ops.math_ops import subtract
from tensorflow.python.ops.math_ops import truediv
from tensorflow.python.ops.math_ops import unsorted_segment_mean
from tensorflow.python.ops.math_ops import unsorted_segment_sqrt_n
from tensorflow.python.ops.math_ops import xlog1py
from tensorflow.python.ops.nn_impl import l2_normalize
from tensorflow.python.ops.nn_impl import zero_fraction
from tensorflow.python.ops.nn_ops import in_top_k_v2 as in_top_k
from tensorflow.python.ops.nn_ops import log_softmax_v2 as log_softmax
from tensorflow.python.ops.nn_ops import softmax_v2 as softmax
from tensorflow.python.ops.nn_ops import top_k
from tensorflow.python.ops.special_math_ops import bessel_i0
from tensorflow.python.ops.special_math_ops import bessel_i0e
from tensorflow.python.ops.special_math_ops import bessel_i1
from tensorflow.python.ops.special_math_ops import bessel_i1e
from tensorflow.python.ops.special_math_ops import lbeta

del _print_function
