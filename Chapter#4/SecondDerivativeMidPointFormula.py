

                # ************************** CODE Discription ***********************************
# 1) Take input value of h 
# 2) Take no: of points
# 3) Values each value of x and it's corresponding value of f(x)
# 4) Then finally take the valid point from given points to find 2nd derivative at that point.
# 5) Finally calculate the 2nd derivative if point is present in given points,
#    if not then simply print the message that this particular point is not in given point
a = []
fx = []

h = float(input("Enter value of h: "))
r = int(input("Enter no: of points: "))
ran = range(r)
for i in ran:
    a.append( float(input("Enter value of x: ")) )
    fx.append( float(input("Enter value of corresponding f(x): ")) )

print("Enter any valid point from given points to find 2nd derivative at that point: ")
p = float(input())
j = p-h
k = p+h
c=0
for i in range(r):
    if(a[i]==p):
        m = fx[i]
    
    if(a[i]==j):
        f = fx[i]
        c +=1
    
    elif(a[i]==k):
        l = fx[i]
        c +=1

if(c==2):
    der = ( f - 2*m + l ) 
    h1 = h*h
    cal = der/h1
    print(f"{cal:.6f}")
else:
    print("Points are not in the givens points: ")