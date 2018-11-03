# pyboolean
Parse infix boolean expressions to postfix (RPN), evaluate and generate truth tables.

Compatibilities
------------

* *Python 3.x*
* *Any Operating System*

Installation
------------

pyboolean is published on **PyPi**, so you only need to run the following command:

    $ pip install pyboolean
    
Usage
------------

Creating a new boolean expression:

```python
from pyboolean import BoolExpr
    
bool_expr = BoolExpr('1 or 0')
```

Printing the formatted version of the expression:

```python
print(bool_expr)
# Output: "1 + 0"
```
Evaluating our boolean expression:

```python
print(bool_expr.eval())
# Output: "1"
```

A boolean expression can also include variables:

```python
bool_expr = BoolExpr('1 . m + ( 0 + ! n ) . m')
```

In order to evaluate an expression with variables, the eval() function can take arguments to replace them:

```python
print(bool_expr.eval(1, 0))
# Output: "1"
```

For expressions with variables, one can generate a truth table like so:

```python
print(bool_expr.truthtable())
# Output:
#╔════════════╗
#║  m  n  ┃ O ║
#║━━━━━━━━╋━━━║
#║  0  0  ┃ 0 ║
#║────────╂───║
#║  0  1  ┃ 0 ║
#║────────╂───║
#║  1  0  ┃ 1 ║
#║────────╂───║
#║  1  1  ┃ 1 ║
#╚════════════╝
```

Or if you need to manipulate the raw truth table data, generate a dictionary:

```python
print(bool_expr.truthdict())
# Output: "{('0', '0'): '0', ('0', '1'): '0', ('1', '0'): '1', ('1', '1'): '1'}"
```

Finally, a note on formatting. When creating an expression, all spaces are ignored and many different versions of the operator symbols are accepted, so one can be very 'creative' with the input and not need to worry:

```python
bool_expr = BoolExpr('p+1and   ¬m.(1∧p ) ∨notxand~0')
print(bool_expr)
# Output: "p + 1 . ! m . ( 1 . p ) + ! x . ! 0"
```

Full list of accepted operator symbols:

**AND:**

and . & ∧

**OR:**

or + | ∨

**NOT:**

not ! ~ ¬
