
num = float(input("enter a number a check: "))
check = float(input("enter a number to divide by: "))

if num % check == 0:
    print(f"{num} divides evenly by {check}")
else:
    print(f"{num} does not divide evenly by {check}")
