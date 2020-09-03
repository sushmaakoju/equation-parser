#Top-Down Recursive Descent parser and is necessarily LL(k) parser.
# LL - Left-to-right performing Left-most derivation of expression, in this context,
# an equation. 1) Grammar must** be LL(k) 2) Iff LL(k) Grammar, parse the equation.
#This is a Predictive parser, since it has no backtracking.
# Since it is "recursive", implementation would be recursive, dynamic programming style.
# with memoization.
# key assumptions for initial tests for this Parser:
# all terms that are arrays are numpy arrays (ndarrays) and are along default axis.
# we will not worry on this for now, since all Xs are 1-dim matrices/flattened arrays.

import numpy as np

class Parser(object):
    """This is a recursive descent parser for parsing polynomial equations. 
       Example: Y' = 2*3+4*3-7
       The required Grammar is:
       following follows regular expression formatting, definition guidelines.
       https://docs.python.org/3/library/re.html and https://docs.python.org/3/howto/regex.html 
       https://docs.python.org/3/reference/expressions.html 
       equation = expression '=' expression
       expression = ['-'] term {(+|-) term}
       term = number | variable
       number = digit {digit}
       digit = 0-9
       variable = [number] 'x'
       *** we DO NOT use 'x' or 'X' for multiplication since terms, variables 
       are always represented by x, X.

    Args:
        object (object): a string or object that is serializable
    """

    def __init__(self, equation):
        self.next_index = 0
        self.equation = equation
        self.EOF = "\0"
    
    def top(self):
        if self.next_index < len(self.equation):
            return self.equation[self.next_index]
        else:
            return self.EOF
    
    def next(self):
        value = self.top()
        self.next_index += 1
        return self.top()
    
    def expression(self):
        coefficient, value =  self.term()

        while True:
            if self.top() == '+':
                self.next()
                term = self.term()
                coefficient = ""
                value = 0
                #replace sum with numpy : (get all Xs in NumPy arrays) and map
                if type(term) is str:
                    pass
                elif type(term) is int or type(term) is float:
                    coefficient, value = map(np.sum, (coefficient, value),
                                                term)
            elif self.top() == '-':
                self.next()
                this_term = self.term()
                coefficient = ""
                value = 0
                #replace sum with numpy/theano : (get all Xs in NumPy arrays) and map
                if type(term) is str:
                    pass
                elif type(term) is int or type(term) is float:
                    coefficient, value = map(np.diff, (coefficient, value),
                                                    this_term)
            else:
                break
        return coefficient, value                

    def term(self):
        """This method returns the terms in each expression along with 

        Returns:
            [type]: [description]
        """
        number = 0
        variable = ""
        sign = 1
        if self.top() == '-':
            self.next()
            sign =  -1
        this_term = self.top()
        number  = sign * (self.number() if this_term.isdigit() else 0)
        variable = sign * (self.variable() if this_term.isalnum() else 1)

        if number != 0:
            if self.top() == "*":
                self.next()
                return number, 0
            else:
                return 0, number
        if variable != "":
            if self.top() == "*":
                self.next()
                return variable, 0
            else:
                return 0, variable
    
    def number(self):
        value = 0
        while self.top().isdigit():
            value =  value * 10 + int(self.top())
            self.next()
        return value

    def interpret(self):
        left_result = self.expression()
        print(left_result)
        self.next()
        right_result = self.expression()
        print(right_result)
        #need to decide what operation numpy.diff,sum, mul, div or theano
        return map(np.sum, left_result, right_result)
    
class Evaluator(object):
    def evaluate(self, equation):
        """[summary]

        Args:
            equation (strs): [description]

        Returns:
            result (str): return the results
        """
        parser = Parser(equation)
        coefficient, value = parser.interpret()

        if coefficient == 0:
            if value != 0:
                return "No Solution"
            else:
                "Infinite solutions"
        
        return "result = {}".format(value)