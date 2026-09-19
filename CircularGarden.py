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

