#Given a non-negative integer x, compute and return the square root of x.
#
#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
#Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

#Input: x = 4
#Output: 2
#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
import math
num = float(input("Enter num: "))
a = 1.0
while(1):
	b = a*a
	if  num-0.1 < b < num+0.1 :
		break
	else:
		pass
	a = a + 0.01


print("\nSquare root value is: ",math.floor(a))