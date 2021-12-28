
import random

def generate_number():
    return random.randint(1, 9)

def compare(guess, actual):
    if guess > actual:
        result = "too high"
    elif guess < actual:
        result = "too low"
    else:
        result = "bingo"
    return result

actual = generate_number()
print(actual)

playing = True
while playing:
    try:
        lives = 3
        while lives > 0:
            guess = int(input("Enter a number between 1-9: "))
            print(compare(guess, actual))
            lives -= 1
            if guess == actual:
                playing = False
                break
        print("thanks for playing!")
        playing = False
    except Exception as e:
        print(e)
