
import secrets
import string

while True:
    try:
        num = int(input("enter number of characters for password: "))
        if num >= 8:
            letters = int(input("enter number of letters to include: "))
            digits = int(input("enter number of digits to include: "))
            chooseLetters = "".join(secrets.choice(string.ascii_letters) for i in range(letters))
            chooseDigits = "".join(secrets.choice(string.digits) for i in range(digits))
            if letters + digits == num:
                selectFrom = chooseLetters + chooseDigits
                password = "".join(secrets.choice(selectFrom) for i in range(num))
                print(f"the password generated is: {password}")
                break
            else:
                print(f"number of letters and digits entered do not match number of characters entered!")
        else:
            print("password length must be greater than or equal to 8!")
    except Exception as e:
        print(e)

