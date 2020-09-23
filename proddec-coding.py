# Python program to find roots of quadratic equation 
import math  
  
  
# function for finding roots 
def equationroots( x, y, z):  
  
    # calculating discriminant using formula 
    dis = y * y - 4 * x * z  
    sqrt_val = math.sqrt(abs(dis))  
      
    # checking condition for discriminant 
    if dis > 0:  
        print(" real and imaginary roots ")  
        print((-y + sqrt_val)/(2 * x))  
        print((-y - sqrt_val)/(2 * x))  
      
    elif dis == 0:  
        print(" real and same roots")  
        print(-y / (2 * x))  
      
    # when discriminant is less than 0 
    else: 
        print("Complex Roots")  
        print(- y / (2 * x), " + i", sqrt_val)  
        print(- y / (2 * x), " - i", sqrt_val)  
  
# Driver Program  
x = 1
y = 10
z = -24
  
# If x is 0, then incorrect equation 
if x == 0:  
        print("Input correct quadratic equation")  
  
else: 
    equationroots(x, y, z) 
