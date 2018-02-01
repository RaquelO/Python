#This program calculates the Euclidian distance between two sets of coordinates in two dimensional space.

#import the math library that will be used for calculations
import math

#prompt the user to enter values for the coordinates and assign those values to variables
x1 = int(input("Enter the X value of the first set of coordinates: "))
y1 = int(input("Enter the Y value of the first set of coordinates: "))
x2 = int(input("Enter the X value of the second set of coordinates: "))
y2 = int(input("Enter the Y value of the second set of coordinates: "))

#calculate the Euclidian distance and round the result to two decimal places
eucldist = format ((math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))), ",.2f")

#display the result on the screen rounded to two decimal places
print ("The distance between the points is", eucldist)
