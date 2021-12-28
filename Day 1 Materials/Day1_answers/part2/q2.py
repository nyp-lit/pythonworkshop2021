
string = "tHE QuiCk BrOWn foX jumPED oveR THe feNCE"

upperList = []
lowerList = []

for i in string:
    if i.isupper():
        upperList.append(i)
    elif i.islower():
        lowerList.append(i)

print(f"the original string is: {string}")
print(f"the reformatted string is: {''.join(lowerList + upperList)}")

