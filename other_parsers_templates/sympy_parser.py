import numpy as np
import sympy as sp
import pandas as pd
import sys
#give input equation
expr = sp.sympify("x_1**2 + x_2*x_3")
#get number of columns from X dataframe and y dataframe
num_of_columns = 3+1 #dataframe features len(X.columns) +1
num_of_y_columns = 2 #dataframe features len(Y.columns) +1
#create equation variables as user prefers to enter like x_1 ** 2 + x_2 * x_3
symbols = sp.symarray('x',num_of_columns)
symbols = symbols[1:]
y_symbols = sp.symarray('y', num_of_y_columns)
y_symbols = y_symbols[1:]
print(symbols)
df = pd.DataFrame(
	[[21, 72, 67.1],
	[23, 78, 69.5],
	[32, 74, 56.6],
	[52, 54, 76.2]],
    columns = ['x1','x2', 'x3'])
variable_tuple = [df[c].to_numpy() for i,c in enumerate(df.columns, start=1)]
mod = sys.modules[__name__]
for i,c in enumerate(df.columns, start=1):
	setattr(mod, "x_"+str(i), df[c])
f = sp.lambdify(symbols, expr, 'numpy')
result = f(*variable_tuple)
print(result)
expr2 = sp.sympify("8*x_3/(pi * x_2^3)")
f = sp.lambdify(symbols, expr2, 'numpy')
result = f(*variable_tuple)
print(result)
