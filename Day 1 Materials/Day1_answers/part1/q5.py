
import math

try:
    dividend = float(input("enter the dividend: "))
    divisor = float(input("enter the divisor: "))
    quotient = dividend / divisor
    quotient_rounded = math.ceil(quotient)
except ValueError:
    print("value error, try again!")
except Exception as e:
    print(e)
else:
    print(f"the answer is {quotient_rounded}")
