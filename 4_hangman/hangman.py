# STAGE 1
# print(*'HANGMAN', 'The game will be available soon.', sep='\n')

# STAGE 2
# print(*'HANGMAN')
#
# guessed_word = 'python'
#
#
# def guess(word_to_guess):
#     user_guess = input('Guess the word: ')
#     if user_guess == word_to_guess:
#         print('You survived!')
#     else:
#         print('You are hanged!')
#
#
# guess(guessed_word)


# STAGE 3
# import random
#
# words_to_guess = ['python', 'java', 'kotlin', 'javascript']
#
# print(*'HANGMAN')
#
#
# def guess(word_to_guess):
#     user_guess = input('Guess the word: ')
#     if user_guess == word_to_guess:
#         print('You survived!')
#     else:
#         print('You are hanged!')
#
#
# guess(random.choice(words_to_guess))


# STAGE 4
import random

words_to_guess = ['python', 'java', 'kotlin', 'javascript']

print(*'HANGMAN')


def guess(word):
    phrase = 'Guess the word ' + word[0:3] + '-' * (len(word)-3)
    user_guess = input(phrase)
    if user_guess == word:
        print('You survived!')
    else:
        print('You lost!')


guess(random.choice(words_to_guess))



































