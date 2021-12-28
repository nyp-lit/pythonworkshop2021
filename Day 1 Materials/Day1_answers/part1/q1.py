
name = input("enter your name: ")
admin_no = input("enter your admin number: ")
age = int(input("enter your age: "))
gender = input("enter your gender: ")
weight = float(input("enter your weight (kg): "))

print(f"hello {name}! your admin number is {admin_no}, \n"
      f"you are {age} years old, {gender} and weigh {weight:.2f}kg.")
