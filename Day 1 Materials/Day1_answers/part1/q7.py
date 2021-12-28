
#a
celsius = float(input("enter temperature in celsius: "))
farenheit = ((9/5 * celsius) + 32)
print(f"the temperature converted to farenheit is {farenheit}")



#b
loop = True
while loop:
    try:
        celsius = float(input("enter temperature in celsius: "))
        farenheit = ((9/5 * celsius) + 32)
    except Exception as e:
        print(e)
    else:
        print(f"the temperature converted to farenheit is {farenheit}")
        loop = False
