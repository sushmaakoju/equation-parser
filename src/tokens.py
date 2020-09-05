from enum import Enum
import re
import constants as const
from exception import *
#define formal grammar for polynomials equations

class TokenType(Enum):
    NUMBER = 1
    VARIABLE = 2 #All X1, X2, X3 ...are IDENTIFERS may be SymPy arrays/matrices
    OPERATOR = 3

class Token(object):
    def __init__(self, text : str, index : int):
        self.input = text.strip()
        self.index = index
        self.kind = None

        if re.fullmatch(const.INVALID_PATTERN, self.input):
                raise InvalidInputTokenException()

        if re.fullmatch(const.VARIABLE_PATTERN, self.input):
                self.kind = TokenType.VARIABLE
        elif re.fullmatch(const.NUMBER_PATTERN, self.input):
                self.kind = TokenType.NUMBER
        elif re.fullmatch(const.OPERATOR_PATTERN, self.input):
                self.kind = TokenType.OPERATOR
        else:
                raise PatternMismatchException()
        
        

