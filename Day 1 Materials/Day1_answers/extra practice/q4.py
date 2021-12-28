
a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

median = 0
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print(f"the median is {median}")
