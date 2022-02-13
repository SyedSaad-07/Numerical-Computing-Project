

# ************************** CODE Discription ***********************************
# 1) We include / use library called sympy which is used to simplify the function/expression using simpify() 
#    then find the its numeric value using sympy.subs()
# 2) var( x ) generates variable x  which is used in function,  Ex: 2*cos(x)
# 3) Program flow:
#                  1) First take the lower and upper limit of function.
#                  2) value of n ( divides the limits into " n " points: )
#                  3) Take input function and use simplify() to simplify the function / expression.
#                  4) Calculate h
#                  5) Finally, integrate the function using Simpson's Formula.

import sympy as sym
from sympy import var
from sympy import sympify

a = float(input("Enter value of lower-limit: "))
b = float(input("Enter value of upper-limit: "))
n = int(input("Enter value of n: "))

l = []
x = var('x')
print("Enter function: ")
function  = input()
expr = sympify(function)
h = (b-a)/n

sol = 0
for i in range(0,2):
    function = sym.diff(function)

der = function
expr_dr = sympify(der)

text_a = expr_dr.subs(x,float(a))
text_b = expr_dr.subs(x,float(b))
if(text_a > text_b):
    sol = text_a
elif(text_b > text_a):
    sol = text_b


k=0
z = 0.0
l.append(a)
k+=1
z = h+a
while(k!=n+1):
    l.append( z )
    z = z + h
    k+=1


i = 0
while(i!=k):
    print(l[i])
    i+=1

first_two = ( expr.subs(x, float(a)) + expr.subs(x, float(b)) )
integ = 0
i=1
while(i!=n):
    integ = integ +  expr.subs(x, float(l[i])) 
    i+=1

    # integ = integ*2
final = (first_two + 2*integ)
final = final*h/2

bound_error = (b-a)*(h*h)*sol
bound_error = bound_error/12

print("Approximation value of Integration= ",f"{final:.6f}", " And Bound_Error= ",f"{bound_error:.6f}")