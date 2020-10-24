#SymPy is a non-commercial alternative to Mathematica and Maple
# SymPy can map variable to a value or a matrix.
# SymPy's Symbolic Statistical Modelling uses scintific computing.
import numpy as np
import sympy as sp
import pandas as pd
import sys
#give input equation
expr = sp.sympify("x_1**2 + x_2*x_3")
#get number of columns from X dataframe and y dataframe
num_of_columns = 10+1 #dataframe features len(X.columns) +1
num_of_y_columns = 2 #dataframe features len(Y.columns) +1
#create equation variables as user prefers to enter like x_1 ** 2 + x_2 * x_3
symbols = sp.symarray('x',num_of_columns)
symbols = symbols[1:]
y_symbols = sp.symarray('y', num_of_y_columns)
y_symbols = y_symbols[1:]

df = pd.DataFrame(
	[[21, 72, 67.1],
	[23, 78, 69.5],
	[32, 74, 56.6],
	[52, 54, 76.2]],
    columns = ['feature1','feature2', 'feature3'])
#create variables by setattr with dataframe's columns i.e. numpy arrays (series essentially arrays)
mod = sys.modules[__name__]
for i,c in enumerate(df.columns, start=1):
	setattr(mod, "x"+str(i), df[c])
#just create variables SymPy way and store it as a stuple for creating f_1(x) -> H_1(x)
variable_tuple = tuple([sp.var(s.name) for s in symbols[0:len(df.columns)]])

#define the R.H.S of equation as user inputs and as parsed
#expr =  x_1**2 + x_2*x_3
#use lambdify with symbols that are actually created as variables and expression and 
#package to be used
f = sp.lambdify(variable_tuple, expr, 'numpy')
#replace features in f(x_1,x_2,x_3) => map x_1, x_2, x_3 to x1,x2,x3
#get all x1, x2, x3 values
#x1,x2,x3 = [df[c] for c in df.columns]
#evaluate
result = f(x1,x2,x3)
print(result)
expr2 = sp.sympify("8*x_3/(pi * x_2^3)")
f = sp.lambdify(symbols, expr2, 'numpy')
result = f(symbols)
print(result)