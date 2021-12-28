
n = int(input("enter number of elements: "))
myList = []

for i in range(1, n+1):
    value = int(input(f"enter #{i}: "))
    myList.append(value)
myTuple = tuple(myList)
print(f"your tuple is: {myTuple}")



#a
givenTuple = (5,9,10,9,2,9)
joinedTuple = myTuple + givenTuple
print(f"the joined tuple is: {joinedTuple}")
print("======================================================")



#b
count = 0
n = int(input("enter a number to count: "))
for i in joinedTuple:
    if i == n:
        count += 1
print(f"the number of times the number {n} appeared is {count}")
print("======================================================")



#c
reverseTuple = joinedTuple[::-1]
print(f"the reversed tuple is: {reverseTuple}")


