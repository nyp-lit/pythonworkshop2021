
num = int(input("enter a number to divide: "))

listRange = list(range(1, num+1))
divisorList = []

for i in listRange:
    if num % i == 0:
        divisorList.append(i)

print(f"divisors of {num}: {divisorList}")
