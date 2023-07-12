# A polynomial equation parser for one-dimensional to multi-dimensional valued arrays, matrices.

## Implementation of polynomial equation parser algorithms in Python.
This is a **proof-of-concept** implementation of polynomial equations in string format, using SymPy, NumPy software libraries and parsing strings to symbols and types. The goal is to assign symbols and create equations from string-based inputs that can be evaluated over data with csv, excel files as input sources. The equations and expressions are auto-instantiated and evaluated to types at runtime. Supports polynomial equations with linear, quadratic, cubic, quartic and higher degrees with recursive substitution as well as terms with squareroots.

### Note
We do not need to pre-define expressions, types and assign variables, since we would not have information about type of equations, types of symbols that could be available in the input files. So this parser takes a string and detects an equation and its terminal and non-terminal symbols and auto-instantiates to types, functions that evaluate the true mathematical expressions. Expressions just need to be less recursive due to underlying limitations in SymPy, due to recursive substitutions, recursive evaluations since the Expression trees may need to preserve the order of evaluation under recursion. The types can be: integer, floats, vectors, int/float arrays, int/float tensors etc.

Also works over (derived from latest SymPy version): matrices, Tensorflow tensors and parses more complex equations in string format, using context-free grammar and abstract syntax trees and can be expanded, WLOG.

## Define Context-free grammar for polynomials equation:

Context-free grammar CFG: G=(N, Σ, P, S), defined as follows:

1. N is a finite set of non-empty symbols (essentially  non-terminal symbols). 
    Here for the polynomial equations, following are non-terminal symbols: 
    - equation ( '8*x3/(pi*x2^3+(x4+x7))' )
    - expressions appearing between brackets ( '(x1^2 + x3)' )
2. Σ (sigma) is a finite set of symbols (terminal symbols essentially leaf nodes). 
    Here for the polynomial equations, following are terminal symbols
    - Numerical coefficients i.e. Digits (1, 2, 3 etc)
    - Operators (+,-,*,/,^)
    - Variables (X1, x2, x_3, x5 etc)
    - mathematical constants (pi, e (eulers_number), sqrt_2 (pythogoras constant) etc)
3. N ∩ Σ = Φ (there is absolutely no intersection between terminal and non-terminal symbols)
4. Define vocabulary V = N u Σ (Union set of terminal and non-terminal symbols is vocabulary)
5. S ∈ N (Goal/start symbol)
6. P is a finite subset of N x V* (Production rules , which in this case are regular expression      
    patterns using Python's regex library)
    Some examples of production rules: 
    a an equation can start with digit or variable or bracket. 
    - if it contains a variable, then it must start with an alphabet (lower/upper case allowed), 
        followed by a digit or underscore followed by a difit
    - Allowed operators are +, -, *, / and can occur multiple times.
    - the operators are always seperated by digits or variables
    - we need atleast one variable in a given equation (since we dont support numeric/digit       
        evaluations)
7. We just evaluate the input equation for token validations (for terminals vs non-terminals) for 
      production rules. We use sympy which has its own, but very similar production rules as well. We use SymPy to evaluate equations. We just need to know if the incoming equation is valid or not before parsing it through SymPy.
8. All variables defined are one-dimensional arrays. Here we represent using NumPy Arrays. 
       However these are extendable to TensorFlow arrays/matrices.

## Steps to install
Assumption: Python3.8.x is already installed.

Clone the repository:
```
git clone https://github.com/sushmaakoju/parser.git
```

- Make sure you have command prompt from cloned repository:

    ```
    cd parser or
    cd parser-master
    ```

- Install the requirements for running tests:

    ```
    pip install -r requirements.txt
    ```
- Run following tests:

    ```
    python -m test
    ```
### Code of conduct

Resources were used for specific literature/code, it is provided in the respective implementation file. The code provided here is implicitly expected not to be replicated for homeworks, assignments or any other programming work. It is welcome to take inspiration, but it is implicitly expected to cite this resource if used for learning, inspiration esp. for any homeworks/projects purposes. Please refer <a href="https://github.com/sushmaakoju/parser/blob/master/CODE_OF_CONDUCT.md">code of conduct</a>.
