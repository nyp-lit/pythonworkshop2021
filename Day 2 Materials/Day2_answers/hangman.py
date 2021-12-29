import random  # choose a random word from the word list
from words import words  # import words from words.py into hangman.py
import string  # import string library function


# print(words) # print words variable from words.py

def get_valid_word(words):
    word = random.choice(words)  # choose a word from word list
    while '-' in word or ' ' in word:  # while there is a dash or space in word
        word = random.choice(words)  # choose a word from word list again

    return word.upper() # return the word in uppercase


def hangman():
    word = get_valid_word(words)  # call the get_valid_word function
    word_letters = set(word)  # letters in the word
    # print(word_letters)
    alphabet = set(string.ascii_uppercase)  # All uppercase letters
    # print(alphabet)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        # print(word_list)
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ')
        user_letter = user_letter.upper()  # convert the letters to uppercase
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # add user_letter to used_letters
            # print(alphabet - used_letters)
            # print(used_letters)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # remove user_letter from word_letter
                # print(word_letters)

            else:
                lives = lives - 1  # take away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            # if user key in letter that is already used.
            # E.g. if user keys in 'A', and keys in 'A' again. The print statement will appear.
            print('You have already used that character. Please try again.')

        else:
            # When user did not key in a letter
            print('Invalid character. Please try again.')

        # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        # if user lives are 0 and user did not guess the word.
        print('You died, sorry. The word was', word)
    else:
        # if user managed to guess the word
        print('You guessed the word', word, '!!')


hangman()  # call the hangman function
