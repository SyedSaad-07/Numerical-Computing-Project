

# ************************** CODE Discription ***********************************
# 1) We include / use library called sympy which is used to simplify the function/expression using simpify() , calculates
# its derivative using sympy.diff() and then find the its numeric value using sympy.subs()
# Program flow:
#             1) Take inputs of lower and upper limits, program will select initial value using (a+b)/2 formula.
#             2) Then wants to take fucntion as input.
#             3) Find it's derivative.
#             4) Take input of no: of maximum iterations and tolerance value
#             5) Program will terminate if, tolerance value is matched / pre-value == cur-value / no: of iteration will greater than user input
#             6) Check if solution exist or not.
#             7) Final print the outputs according to the method.
import sympy as sym
from sympy import var
from sympy import sympify

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
P = (a+b)/2
error = P
x = var('x')
print("Enter function: ")
function  = input()
print("Derivative= ",sym.diff(function))
der = sym.diff(function)
expr1 = sympify(function)
expr2 = sympify(der)
r = int(input("Enter max no: of iterations: "))
e = float(input("Enter tolerance value: "))
ran = range(r)
pre = P
far = P
text0 = expr1.subs(x, float(a))
text1 = expr1.subs(x,float(b))
if text0 * text1 > 0.0:
    print("Solution Doesn't exist because, it doesn't satisfies the intermediate value theorem")
else:
    i=1
    print("At Iteration no:",i,"value= ",P," and error= ",error)
    termination = True
    while termination:
        pre = P
        text2 = expr2.subs(x, float(P))

        text1 = expr1.subs(x, float(P))

        V = ( float(text1) / float(text2) )
        P = P - V
        far = P 
        error = abs(pre-far)
        termination = abs( expr1.subs(x,float(P)) ) > e 
        if( (far==pre) or i>r ):
            break
        print("At Iteration no: ",i, "value= ",f"{P:.6f}"," and error= ",f"{error:.6f}")
        i+=1