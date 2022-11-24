# calculate the hypotenuse length of right angle triangle
# formula is c square= a square + b square
import math
# from math import sqrt
a= int(input("enter length of side 1 of the triangle: "))
b= int(input("enter length of side 2 of the triangle: "))
c = math.sqrt(a**2 + b**2)
# print (f"The hypotenuse length of right angle triangle is {c}")
print('The hypotenuse length of right angle triangle is %f'