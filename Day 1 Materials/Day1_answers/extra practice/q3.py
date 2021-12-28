
totalSec = int(input("Enter seconds: "))

hr = (totalSec // 3600) % 60
min = (totalSec // 60) % 60
sec = totalSec % 60

print(f"{totalSec} seconds is {hr} hours {min} minutes and {sec} seconds")
