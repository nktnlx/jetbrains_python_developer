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
import random

words_to_guess = ['python', 'java', 'kotlin', 'javascript']

print(*'HANGMAN')


def guess(word):
    tries = 8
    letters = []
    index = []

    while tries > 0:
        print('')
        for l in letters:
            start = 0
            c = 0
            while c < word.count(l):
                index.append(word.find(l, start))
                start = word.find(l, start) + 1
                c += 1

        for j in range(len(word)):
            if j in index:
                print(word[j], end='')
            else:
                print('-', end='')

        print('')
        user_letter = (input('Input a letter: '))
        letters.append(user_letter)
        if user_letter not in word:
            print('That letter doesn\'t appear in the word')

        tries -= 1

    print('')
    print('''Thanks for playing!
We'll see how well you did in the next stage''')


guess(random.choice(words_to_guess))




















