# How it works?
1. Define a function of the mathematical expression.
*Example:*
```
def math_expr(x, y):
    return x**2+y
```

2. Import the module and use the functions defined in the module.
*Example:*
```
from eulers_method import *
'''
Get the values xn, x0, y0, n, h
'''
result = eulers_method(xn, x0, y0, n, h, math_expr)

# to print the graph
show_graph(result)

# to print table
create_table(result)

# to print the value of x and y
print(result['x'][-1], result['y'][-1])
```
