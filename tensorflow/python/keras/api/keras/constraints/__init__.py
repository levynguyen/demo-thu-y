# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Constraints: functions that impose constraints on weight values.
"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.keras.constraints import Constraint
from tensorflow.python.keras.constraints import MaxNorm
from tensorflow.python.keras.constraints import MaxNorm as max_norm
from tensorflow.python.keras.constraints import MinMaxNorm
from tensorflow.python.keras.constraints import MinMaxNorm as min_max_norm
from tensorflow.python.keras.constraints import NonNeg
from tensorflow.python.keras.constraints import NonNeg as non_neg
from tensorflow.python.keras.constraints import RadialConstraint
from tensorflow.python.keras.constraints import RadialConstraint as radial_constraint
from tensorflow.python.keras.constraints import UnitNorm
from tensorflow.python.keras.constraints import UnitNorm as unit_norm
from tensorflow.python.keras.constraints import deserialize
from tensorflow.python.keras.constraints import get
from tensorflow.python.keras.constraints import serialize

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.constraints", public_apis=None, deprecation=True,
      has_lite=False)
