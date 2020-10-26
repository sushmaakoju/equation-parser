from __future__ import absolute_import

import re

VARIABLE_PATTERN = "^[a-zA-Z]+[_]*[1-9]+" #patterns x_1, x_2
NUMBER_PATTERN = "^[1-9]+[0]*" #2, 22, 20
OPERATOR_PATTERN = "(\(|\+|\-|\*|\\|\^|\)|\/){1}" #+-*\^
INVALID_PATTERN = "[\n\t]+"