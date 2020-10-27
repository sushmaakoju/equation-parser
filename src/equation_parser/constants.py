from __future__ import absolute_import

import re

VARIABLE_PATTERN = "^[a-zA-Z]+[_]*[1-9]*[a-zA-Z]*" #patterns x_1, x_2, x1, f, g, delta
NUMBER_PATTERN = "^[1-9]+[0]*" #2, 22, 20
#OPERATOR_PATTERN = "(\(|\+|\-|\*|\\|\^|\)|\/){1}" #+-*\^
OPERATOR_PATTERN = "[\(|\+|\-|\*|\\|\^|\)|\/]{1}" #+-*\^
INVALID_PATTERN = "(?i)sqrt|[\n\t]"