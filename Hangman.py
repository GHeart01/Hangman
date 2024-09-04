#Hangman
import random
import string
from words import words

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_words(words).upper()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = len(word) * 2

    #get user input
    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} left and have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word', ' '.join(word_list) )
        
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print("You have already used that letter)")

        else:
            print('Invalid Chatacter. Please try again.')
    if lives > 0:
        print(f'The word was {word}, CONGRADUATIONS!')
    else:
        print(f'Sorry you died. The word was {word}')

hangman()