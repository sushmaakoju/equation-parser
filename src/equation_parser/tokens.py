from __future__ import absolute_import

from enum import Enum
import re
from .constants import *
from .exception import *

#define formal grammar for polynomials equations
#Attempt context-free grammar CFG: G=(N, Σ, P, S)
# 1) N is a finite, non-empty symbols (essentially  non-terminal symbols). 
# Here for the polynomial equations: 
#       a) equation ( '8*x3/(pi*x2^3+(x4+x7))' )
#       b) expressions appearing between brackets ( '(x1^2 + x3)' )
# 2) Σ (sigma) is a finite set of symbols (terminal symbols essentially leaf nodes). 
# Here for the polynomial equations, following are terminal symbols
#       a) Numerical coefficients i.e. Digits (1, 2, 3 etc)
#       b) Operators (+,-,*,/,^)
#       c) Variables (X1, x2, x_3, x5 etc)
#       d) mathematical constants (pi, e (eulers_number), sqrt_2 (pythogoras constant) etc)
#3)N ∩ Σ = Φ (there is absolutely no intersection between terminal and non-terminal symbols)
#4)Define vocabulary V = N u Σ (Union set of terminal and non-terminal symbols is vocabulary)
#5)S ∈ N (Goal/start symbol)
#6)P is a finite subset of N x V* (Production rules , which in this case are regular expression patterns)
#       example production rules: 
#       a) an equation can start with digit or variable or bracket. 
#       b) if it contains a variable, then it must start with an alphabet (lower/upper case allowed), 
#               followed by a digit or underscore followed by a difit
#       c) Allowed operators are +, -, *, / and can occur multiple times.
#       d) the operators are always seperated by digits or variables
#       f) we need atleast one variable
#7)We just evaluate the input equation for token validations (for terminals vs non-terminals) for production rules,
#       but we use sympy which has its own production rules as well. We use SymPy to evaluate equations.
#       we just need to know if the incoming equation is valid or not before parsing it through SymPy.
#8)All variables defined are one-dimensional arrays. Here we represent using NumPy Arrays. 
#       However these are extendable to TensorFlow arrays/matrices.

class TokenType(Enum):
    NUMBER = 1
    VARIABLE = 2 #All X1, X2, X3 ...are IDENTIFERS may be SymPy arrays/matrices
    OPERATOR = 3

class Token(object):
    def __init__(self, text : str, index : int):
        self.input = text.strip()
        self.kind = None

    def is_valid_token(self):
        if re.fullmatch(INVALID_PATTERN, self.input):
            raise Exception()

        if re.fullmatch(VARIABLE_PATTERN, self.input):
            self.kind = TokenType.VARIABLE
            return True
        elif re.fullmatch(NUMBER_PATTERN, self.input):
            self.kind = TokenType.NUMBER
            return True
        elif re.fullmatch(OPERATOR_PATTERN, self.input):
            self.kind = TokenType.OPERATOR
            return True
        else:
            raise Exception()
        return False

class Tokens:
        def __init__(self, eq_str: str):
            pattern = re.compile(OPERATOR_PATTERN)
            self.token_list = list(filter(None, pattern.split(eq_str)))
            self.tokens = dict()
        
        def validate(self):
            for i, token in enumerate(self.token_list):
                if token == "":
                    continue
                t = Token(token, i)
                try:
                    if t.is_valid_token():
                        self.tokens[token] = t
                    else:
                        False
                except Exception as e:
                    print(e)
            if len(self.tokens) ==len(self.token_list):
                return True
            return False