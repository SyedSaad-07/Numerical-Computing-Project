

                # ************************** CODE Discription ***********************************

# 1) We include / use library called sympy which is used to simplify the function/expression using simpify() , calculates
# its derivative using sympy.diff() and then find the its numeric value using sympy.subs()
# 2) var( x ) generates variable x  which is used in function,  Ex: 2*cos(x)
# 3) Program flow:
#                  1) First take number of points ( 3 | 4 | 6 )
#                  2) Ask to decide for also calculating the true error or not
#                  3) On the basis of number of points which is given as input, program will decide,
#                     which method should follow to calculate the estimated derivative.
#                       1- Numerical Differentiation
#                       2- Three-Point formula
#                       3- Five-Point formula
#                  4) Finally calculates.
import sympy as sym
from sympy import var
from sympy import sympify


a = []
fx = []
r = int(input("Enter no: of points 3 | 4 | 6: "))
ran = range(r)

x = var('x')
print("Enter function: ")
function  = input()
print("Do you Want to calculate true error also: yes/no")
d = input()
if(d=='yes'):
    deri = sym.diff(function)
    expr = sympify(deri)
    print("Proceed to further calculation... ")
elif(d=='no'):
    print("Proceed to further calculation... ")



# Numerical differentiation
if( r==3 ):
    h = float(input("Enter value of h: "))
    for i in ran:
        a.append( float(input("Enter value of x: ")) )
        fx.append( float(input("Enter value of corresponding f(x): ")) )

    for i in ran:
        if(i==0 or i==1):
            j = i+1
            der = ( fx[j] - fx[i] )/h
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - der
                print("Derivative: ",f"{der:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{der:.6f}")
        elif(i==2):
            j= i-1
            der = ( fx[i] - fx[j] )/h
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - der
                print("Derivative: ",f"{der:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{der:.6f}")

# Three-Point Formula
elif( r==4 ):
    h = float(input("Enter value of h: "))
    for i in ran:
        a.append( float(input("Enter value of x: ")) )
        fx.append( float(input("Enter value of corresponding f(x): ")) )
    
    for i in ran:
        if(i==0):
            n1 = i+1
            n2= i+2
            der = ( 4*fx[n1] - fx[n2] - 3*fx[i] )
            h1 = h*2 
            cal =  der/h1
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - cal
                print("Derivative: ",f"{cal:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{cal:.6f}")
        elif(i==1 or i==2):
            n1= i+1
            n2 = i-1
            der = ( fx[n1] - fx[n2] )
            h1 = h*2
            cal =  der/h1
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - cal
                print("Derivative: ",f"{cal:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{cal:.6f}")
        elif(i==3):
            n1 = i-1
            n2 = i-2
            der = ( 4*fx[n1] - fx[n2] - 3*fx[i] )
            h1 = -(h*2)
            cal =  der/h1
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - cal
                print("Derivative: ",f"{cal:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{cal:.6f}")

# Five-Point formula
elif(r==6):
    h = float(input("Enter value of h: "))
    for i in ran:
        a.append( float(input("Enter value of x: ")) )
        fx.append( float(input("Enter value of corresponding f(x): ")) )
        
    for i in ran:
        if(i==0 or i==1):
            n1 = i+1
            n2= i+2
            n3 = i+3
            n4 = i+4
            der = (-25*fx[i] + 48*fx[n1] - 36*fx[n2] + 16*fx[n3] - 3*fx[n4])
            h1 = h*12
            cal =  der/h1
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - cal
                print("Derivative: ",f"{cal:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{cal:.6f}")
        elif( i==2 or i==3 ):
            n1= i-2
            n2 = i-1
            n3 = i+1
            n4 = i+2
            der = ( fx[n1] - 8*fx[n1] + 8*fx[n3] - fx[n4])
            h1 = h*12
            cal =  der/h1
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - cal
                print("Derivative: ",f"{cal:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{cal:.6f}")
        elif( i==4 or i==5 ):
            n1 = i-1
            n2= i-2
            n3 = i-3
            n4 = i-4
            der = (-25*fx[i] + 48*fx[n1] - 36*fx[n2] + 16*fx[n3] - 3*fx[n4])
            h1 = -(h*12)
            cal =  der/h1
            if(d=="yes"):
                true_error = expr.subs(x, float(a[i])) - cal
                print("Derivative: ",f"{cal:.6f}"," Actual error: ",f"{abs(true_error):.6f}")
            else:
                print("Derivative: ",f"{cal:.6f}")
else:
    print("Can not apply any method for Given no of points ")