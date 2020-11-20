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
# import random
#
# words_to_guess = ['python', 'java', 'kotlin', 'javascript']
#
# print(*'HANGMAN')


# def guess(word):
#     phrase = 'Guess the word ' + word[0:3] + '-' * (len(word)-3)
#     user_guess = input(phrase)
#     if user_guess == word:
#         print('You survived!')
#     else:
#         print('You lost!')


# guess(random.choice(words_to_guess))


# STAGE 5
# import random
#
# words_to_guess = ['python', 'java', 'kotlin', 'javascript']
#
# print(*'HANGMAN')
#
#
# def guess(word):
#     tries = 8
#     letters = []
#     index = []
#
#     while tries > 0:
#         print('')
#         for l in letters:
#             start = 0
#             c = 0
#             while c < word.count(l):
#                 index.append(word.find(l, start))
#                 start = word.find(l, start) + 1
#                 c += 1
#
#         for j in range(len(word)):
#             if j in index:
#                 print(word[j], end='')
#             else:
#                 print('-', end='')
#
#         print('')
#         user_letter = (input('Input a letter: '))
#         letters.append(user_letter)
#         if user_letter not in word:
#             print('That letter doesn\'t appear in the word')
#
#         tries -= 1
#
#     print('')
#     print('''Thanks for playing!
# We'll see how well you did in the next stage''')
#
#
# guess(random.choice(words_to_guess))


# STAGE 6
# import random
# import sys
#
# words_to_guess = ['python', 'java', 'kotlin', 'javascript']
#
# print(*'HANGMAN')
#
#
# def guess(word):
#     tries = 8
#     letters = []
#     index = []
#
#     while tries > 0:
#         print('')
#         for letter in letters:
#             start = 0
#             counter = 0
#             while counter < word.count(letter):
#                 index.append(word.find(letter, start))
#                 start = word.find(letter, start) + 1
#                 counter += 1
#
#         for j in range(len(word)):
#             if j in index:
#                 print(word[j], end='')
#             else:
#                 print('-', end='')
#
#
#         if len(set(index)) == len(word):
#             print('')
#             print('''You guessed the word!
# You survived!''')
#             sys.exit(1)
#
#         print('')
#         user_letter = (input('Input a letter: '))
#         if user_letter not in word:
#             print('That letter doesn\'t appear in the word')
#             tries -= 1
#             continue
#         elif user_letter in letters:
#             print('No improvements')
#             tries -= 1
#             continue
#         elif user_letter in word:
#             letters.append(user_letter)
#
#     print('You lost!')


# guess(random.choice(words_to_guess))


# STAGE 7
import random
import sys

words_to_guess = ['python', 'java', 'kotlin', 'javascript']

print(*'HANGMAN')


def guess(word):
    tries = 8
    letters = []
    index = []
    wrong_letters = []

    while tries > 0:
        for letter in letters:
            start = 0
            counter = 0
            while counter < word.count(letter):
                index.append(word.find(letter, start))
                start = word.find(letter, start) + 1
                counter += 1

        if len(set(index)) == len(word):
            print(f'''You guessed the word {word}!
You survived!''')
            sys.exit(1)

        print('')

        for j in range(len(word)):
            if j in index:
                print(word[j], end='')
            else:
                print('-', end='')

        print('')
        user_letter = (input('Input a letter: '))

        if len(user_letter) != 1:
            print("You should input a single letter")
            continue

        elif user_letter.isascii() == False or user_letter.islower() == False:
            print("Please enter a lowercase English letter")
            continue

        elif user_letter in letters or user_letter in wrong_letters:
            print('You\'ve already guessed this letter')
            continue

        elif user_letter not in word:
            print('That letter doesn\'t appear in the word')
            wrong_letters.append(user_letter)
            tries -= 1
            continue

        elif user_letter in word:
            letters.append(user_letter)

    print('You lost!')


#guess(words_to_guess[3])
guess(random.choice(words_to_guess))














