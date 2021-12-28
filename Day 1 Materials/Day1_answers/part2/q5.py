
try:
    numList = []
    count = int(input("enter how many numbers you want to capture: "))
    for i in range(count):
        num = input("Enter number #" +str(i+1) + ": ")
        while num.isdigit() == False:
            num = input("Enter number #" +str(i+1) + ": ")
        numList.append(int(num))

    print(numList)
    print(f"lowest number in the list: {min(numList)}")
    print(f"highest number in the list: {max(numList)}")
    print(f"total of numbers in the list: {sum(numList)}")
    print(f"average of numbers in the list: {sum(numList)/len(numList):.2f}")

except Exception as e:
    print(e)
