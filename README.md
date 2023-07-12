# A polynomial equation parser for one-dimensional to multi-dimensional valued arrays, matrices.

## Implementation of polynomial equation parser in Python (for various degrees of polynomial equations).
This is a **proof-of-concept** implementation of polynomial equations in string format, using SymPy, NumPy software libraries and parsing strings to symbols and types. The goal is to assign symbols and create equations from string-based inputs that can be evaluated over data with csv, excel files as input sources. The equations and expressions are auto-instantiated and evaluated to types at runtime. Supports polynomial equations with linear, quadratic, cubic, quartic and higher degrees with recursive substitution as well as terms with squareroots.

### Example
In <a href="https://github.com/sushmaakoju/polynomial-equation-parser/tree/master/src">polynomial-equation-parser/src</a>, it takes set of equations each assigned to a variable. There can be equations that use the variables which should have been existing symbols in memory i.e. an equation of f = x1 + 4 and g = (f/3) + 25. If both equations are instantiated in SymPy, we would have f, x1, g in memory such that order is preserved i.e. to compute g, we first should have instantiated symbol f and x1 and generated corresponding expressions and "evaluated" these expressions first before instantiating symbol g, its corresponding expressions and evaluations. There can be variable to expression mapping in an given input excel sheet or not. In the absence of variable/column correspondence to a polynomial equation, the polynomial equation parser auto-generates and auto-assignes variables to these expressions and/or equations for symbolic instantiation and evaluation with data.

### Note
We do not need to pre-define expressions, types and assign variables, since we would not have information about type of values to these variables in these equations that could be available in the input data files. So this parser takes a string formatted equation/s and detects an equation/s, its terminal and non-terminal symbols and auto-instantiates to types, functions that evaluate the underlying mathematical expressions. Expressions just need to be less recursive due to underlying limitations in SymPy, due to recursive substitutions, recursive evaluations since the Expression trees may need to preserve the order of evaluation under recursion esp. if there are square roots, derivatives, integrals involved in the equations. The types can be: integer, floats, vectors, int/float arrays, int/float tensors, numpy arrays, matrices etc.

Also works over (derived from latest SymPy version): matrices, Tensorflow tensors and parses more complex equations in string format, using abstract syntax trees and trees can be expanded, WLOG.

### Future work
Can be expanded to variable degrees of polynomial equations but with approximations (since degrees >= 5 are unsolvable by radicals. Examples: irreducible/prime polynomials). 

### Differences between SymPy and NumPy
SymPy supports symbolic computation is different from NumPy. π, sin, cosine in SymPy are symbolic representations of π, sine, cosine operations. π, sin, cosine in NumPy are numerical approximations of mathematical operations π, sine, cosine.
Everything is initially a "symbol" instance in SymPy until the corresponding symbol instance is created by defining a type and/or by data correspondence at the time of the symbol instance creation. Such abstraction holds options to adapt a variable "x" in an equation to a real number, integer, array, vector, matrix, or even a tensor. Symbol to data and datatype correspondence requires explicit mappings between symbols and data + datatypes when using SymPy. Until symbol instances are created, symbols are abstract representations of variables, functions or operations in SymPy, which is synonymous to terminal vs non-terminal symbols in formal representation of Context-free grammar theory.

The scripts under <a href="https://github.com/sushmaakoju/polynomial-equation-parser/tree/master/other_parsers_templates"> other_parsers_templates</a> have examples of how SymPy and NumPy with or without using either a) abstract symbols instances with Lambda Calculus to evaluate, parse and generate syntax trees with data type correspondences dynamically or b) simply evaluate operations over the data. 

## Define Context-free grammar for polynomial equation:

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
