
x = float(input("input length of the first side of the triangle: "))
y = float(input("input length of the second side of the triangle: "))
z = float(input("input length of the third side of the triangle: "))

if x == y == z:
    print("it is an equilateral triangle")
elif x == y or y == z or z == x:
    print("it is an isosceles triangle")
else:
    print("it is a scalene triangle")
