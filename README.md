## Circular Garden

## Problem Identification:
The school plans to create a circular garden and will use a developed Python program that will help them determine information about the garden based on the radius entered by the user.

## Problem Decomposition:
The program needs,
Input for the radius
An area calculator
A circumference calculator
A square root calculator
A rounding calculator

## Pattern Recognition
The expected output will all use the same intro with different outros
Example:
print("The area of the garden in square meters is: ", area)
print("The circumference of the garden in meters is: ", circumference))

## Data Representation
The program will display the area, circumference, square root, the rounded up and rounded down area all in one big output

## Algorithm Development
import math

radius = float(input("Enter radius of the garden (in meters): "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
areasqrt = math.sqrt(area)
roundedup_area = math.floor(area)
roundeddown_area = math.ceil(area)

print("The area of the garden in square meters is: ", area)
print("The circumference of the garden in meters is: ", circumference)
print("The square root of the garden is: ", areasqrt)
print("The rounded up area of the garden in square meters is: ", roundedup_area)
print(" The rounded down area of the garden in square meters is: ", roundeddown_area)