
myList = [1,2,3,4,5,6,7,100,110,21,22,33,32,2,4]

evenNums = []
sum = 0

for i in myList:
    if i % 2 == 0:
        evenNums.append(i)

for i in evenNums:
    sum += i

print(f"the sum of even numbers is {sum}")
