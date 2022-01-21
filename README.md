# A polynomial equation parser for one-dimensional to multi-dimensional valued arrays, matrices.

### Code of conduct
Resources were used for specific literature/code, it is provided in the respective implementation file. The code provided here is implicitly expected not to be replicated for homeworks, assignments or any other programming work. It is welcome to take inspiration, but it is implicitly expected to cite this resource if used for learning, inspiration purposes. Please refer a< href="https://github.com/sushmaakoju/parser/blob/master/CODE_OF_CONDUCT.md">code of conduct</a>.

Implementation of polynomial equation parser algorithms in Python.
This is a **proof-of-concept** using SymPy, NumPy and a string Parsing algorithm to assign symbols and create equations that can be evaluated by applying data from csv, excel files data-sources.

Work-in-progress: add matrices, use Tensorflow inputs and parse more complex equations in string format, using context-free grammar and abstract syntax tree.

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
