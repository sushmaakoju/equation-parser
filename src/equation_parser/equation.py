from __future__ import absolute_import

#SymPy is a non-commercial alternative to Mathematica and Maple
# SymPy can map variable to a value or a matrix.
# SymPy's Symbolic Statistical Modelling uses scintific computing.
import sys
import numpy as np
import sympy as sp
import pandas as pd
from .tokens import *

__all__ = ['Equation']

class Equation:
    def __init__(self, eq_string : str, X : pd.DataFrame ):
        """
        """
        self.expr = eq_string
        #give input equation
        self.tokens = Tokens(eq_string)
        if self.tokens.validate():
            print("valid tokens!")
        self.X = X
        self.symbols = None
        self.columns_mappings = dict()
        self.result = None
    
    def set_symbols(self, columns_symbol_mappings):
        self.symbols = []
        self.columns_mappings = dict()
        if columns_symbol_mappings is None:
            #"x_1**2 + x_2*x_3")
            #get number of columns from X dataframe and y dataframe
            num_of_columns = len(self.X.columns)+1 #dataframe features len(X.columns) +1
            #create equation variables as user prefers to enter like x1 ** 2 + x2 * x3
            self.symbols =  list(sp.symbols('x1:{}'.format(num_of_columns)))
            for col, symbol in zip(self.X.columns.values, self.symbols): 
                self.columns_mappings[str(symbol)] = str(symbol)
        else:
            for col, symbol in zip(columns_symbol_mappings['column'], 
                        columns_symbol_mappings['variable']):                    
                self.symbols.append(sp.Symbol(symbol))
                self.columns_mappings[symbol] = col

    def evaluate(self, values):
        self.expression = sp.sympify(self.expr)
        variable_tokens = self.tokens.get_variables()
        this_eq_symbols = [token for token in variable_tokens if token in str(self.symbols)]
        #create variables SymPy way and store it as a stuple for creating f_1(x) -> H_1(x)
        variable_tuple = self.get_columns(this_eq_symbols, values)
        #define the R.H.S of equation as user inputs and as parsed
        #expr =  x_1**2 + x_2*x_3
        #use lambdify with symbols that are actually created as variables and expression and 
        #package to be used
        f = sp.lambdify(this_eq_symbols, self.expr, 'numpy')
        #replace features in f(x_1,x_2,x_3) => map x_1, x_2, x_3 to x1,x2,x3
        #evaluate
        self.result = f(*variable_tuple)
        print(self.result)
        return self.result
    
    def get_columns(self, this_eq_symbols, values):
        cols = []
        evaluated_cols = []
        for symbol in this_eq_symbols: 
            if symbol in self.columns_mappings: 
                if self.columns_mappings[symbol] == "None":
                    evaluated_cols.append(symbol)
                else:
                    cols.append(self.columns_mappings[symbol])
        result = [self.X[c].to_numpy() for i,c in enumerate(self.X.columns, start=1) if c in cols]
        [ result.append(values[c]) for c in evaluated_cols]
        return result
