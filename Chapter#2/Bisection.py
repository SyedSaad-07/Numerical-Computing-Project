

# ************************** CODE Discription ***********************************
# 1) We include / use library called sympy which is used to simplify the function/expression using simpify() , calculates
# its derivative using sympy.diff() and then find the its numeric value using sympy.subs()
# Program flow:
#             1) Take inputs of lower and upper limits.
#             2) Then wants to take fucntion as input.
#             4) Take input of Tolerance value
#             5) Program will terminate if, tolerance value is matched.
#             6) Check if solution exist or not.
#             7) Final print the outputs according to the method.
import sympy as sym
from sympy import var
from sympy import sympify

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

x = var('x')
print("Enter function: ")
function  = input()

expr1 = sympify(function)

e = float(input("Enter tolerance value: "))

text0 = expr1.subs(x, float(a))
text1 = expr1.subs(x,float(b))
if text0 * text1 > 0.0:
    print("Solution Doesn't exist because, it doesn't satisfies the intermediate value theorem")
else:
    i=1
    termination = True
    while termination:
        c = (a + b)/2
        sol = expr1.subs(x,float(c))
        print('Iteration-%d, x = %0.6f and f(x) = %0.6f' % ( i, c, sol ) )
        text0 = expr1.subs(x, float(a))
        text1 = expr1.subs(x,float(c))

        if text0 * text1 < 0:
            b = c
        else:
            a = c
        i+=1
        sol = expr1.subs(x,float(c))
        termination = abs( sol ) > e 