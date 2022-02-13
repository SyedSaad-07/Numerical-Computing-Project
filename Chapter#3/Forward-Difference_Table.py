

                # ************************** CODE Discription ***********************************
# 1) We include / use numpy library to use arrays.
# 2) Program flow:
#                1) Take input of data points ( for size of the array ), then initialize it with zero ( for both x and y ).
#                2) Make array of x as 1-D and array of y as 2-D.
#                2) Take data for both x and y.
#                3) Finally calculates / generates the Forward Difference Table.
 
import numpy as np
import math
n = int(input('Enter number of data points: '))

x = np.zeros((n))
y = np.zeros((n,n))

print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
    
# Generating forward difference table
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

        
print('\nFORWARD DIFFERENCE TABLE\n')

for i in range(0,n):
    print('%0.5f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.5f' %(y[i][j]), end='')
    print()

def p_value(p,n):

    temp = p
    for i in range(1,n):
        temp = temp*(p-i)
    return temp
    
inter = float(input("\nEnter value to find it's approx: solution: "))

value = y[0][0]
p = (inter - x[0])/(x[1] - x[0])
for i in range(1,n):
    value = value + ( p_value(p,i)*y[0][i]) /math.factorial(i)

print('Value at: ',inter,' is %0.5f '%value)