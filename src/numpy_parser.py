import numpy as np
import pandas as pd
import sympy as sp
from sympy import *
#numpy polynomial evaluation
#using x_i notation directly which is not real-world case anyway.
df = pd.DataFrame(
	[[21, 72, 67.1],
	[23, 78, 69.5],
	[32, 74, 56.6],
	[52, 54, 76.2]],
    columns = ['x1','x2', 'x3'])
x1, x2, x3 = [df[c].to_numpy() for i,c in enumerate(df.columns, start=1)]
#expr =  x0**2 + x1*x2
expr = x1**2 + x2*x3
print(expr)