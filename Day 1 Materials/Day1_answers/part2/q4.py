
num = int(input("enter a number: "))

i = 2
print(f"the prime factors of {num} are: ")
while i <= num:
    #check if its a prime
    j = 2
    count = 0
    while j<= i:
        if i % j == 0:
            count += 1
        j += 1
    #if count is greater than 1, it is not a prime
    #if prime and factor, then it is a prime
    if count <= 1 and num % i == 0:
        print(i)
    i += 1
