# STAGE 1
# user_choice = input()
#
# if user_choice == 'scissors':
#     computer_choice = 'rock'
#     print(f'Sorry, but the computer chose {computer_choice}')
#
# elif user_choice == 'rock':
#     computer_choice = 'paper'
#     print(f'Sorry, but the computer chose {computer_choice}')
#
# elif user_choice == 'paper':
#     computer_choice = 'scissors'
#     print(f'Sorry, but the computer chose {computer_choice}')


# STAGE 2
# import random
# 
# user_inp = input()
# 
# # random choice of a computer
# options = ['rock', 'paper', 'scissors']
# comp_choice = random.choice(options)
# 
# # dictionary with all possible outcomes of the game
# results = {'rockpaper': 'lose',
#            'rockscissors': 'win',
#            'rockrock': 'draw',
#            'paperrock': 'win',
#            'paperscissors': 'lose',
#            'paperpaper': 'draw',
#            'scissorsrock': 'lose',
#            'scissorspaper': 'win',
#            'scissorsscissors': 'draw'}
# 
# # concatenating user and computer choices to receive a key for our dictionary
# game = user_inp + comp_choice
# 
# # printing outcome
# if results[game] == 'win':
#     print(f'Well done. The computer chose {comp_choice} and failed')
# elif results[game] == 'lose':
#     print(f'Sorry, but the computer chose {comp_choice}')
# elif results[game] == 'draw':
#     print(f'There is a draw ({comp_choice})')
    
    
# STAGE 3
# import random
#
# # random choice of a computer from the list
# options = ['rock', 'paper', 'scissors']
#
# # dictionary with all possible outcomes of the game
# results = {'rockpaper': 'lose',
#            'rockscissors': 'win',
#            'rockrock': 'draw',
#            'paperrock': 'win',
#            'paperscissors': 'lose',
#            'paperpaper': 'draw',
#            'scissorsrock': 'lose',
#            'scissorspaper': 'win',
#            'scissorsscissors': 'draw'}
#
#
# def main():
#     while True:
#         user_inp = input()
#         comp_choice = random.choice(options)
#         game = user_inp + comp_choice   # concatenating user and computer choices to receive a key for our dictionary
#
#         if user_inp not in options and user_inp != '!exit':
#             print('Invalid input')
#         elif results.get(game) == 'win':
#             print(f'Well done. The computer chose {comp_choice} and failed')
#         elif results.get(game) == 'lose':
#             print(f'Sorry, but the computer chose {comp_choice}')
#         elif results.get(game) == 'draw':
#             print(f'There is a draw ({comp_choice})')
#         else:
#             print('Bye!')
#             break
#
#
# main()


# STAGE 4
import random

# random choice of a computer from the list
options = ['rock', 'paper', 'scissors']

# dictionary with all possible outcomes of the game
results = {'rockpaper': 'lose',
           'rockscissors': 'win',
           'rockrock': 'draw',
           'paperrock': 'win',
           'paperscissors': 'lose',
           'paperpaper': 'draw',
           'scissorsrock': 'lose',
           'scissorspaper': 'win',
           'scissorsscissors': 'draw'}


# reading rating list
def reading_rating():
    # reading current rating from a rating.txt file
    f = open('rating.txt', 'r')
    user_list = f.readlines()

    # splitting names and scores
    for i in range(len(user_list)):
        user_list.append(user_list[i].split())  # now we have a list of double size

    # removing artefacts from the list
    for i in range(int(len(user_list) / 2)): # len of the initial list
        c = 0
        user_list.pop(0)

    return user_list


# entering user name and searching for his rating
def enter_name(user_list):
    user_name = input('Enter your name: ')

    for nested_list in user_list:
        if user_name in nested_list:
            print(f'Hello, {user_name}')
            rating = nested_list[1]
            return int(rating)
    else:
        print(f'Hello, {user_name}')
        rating = 0
        return rating


# playing the game
def main():
    score = enter_name(reading_rating())
    while True:
        user_inp = input()
        comp_choice = random.choice(options)
        game = user_inp + comp_choice   # concatenating user and computer choices to receive a key for our dictionary

        if user_inp == '!rating':
            print(f'Your rating: {score}')
        elif user_inp not in options and user_inp != '!exit':
            print('Invalid input')
        elif results.get(game) == 'win':
            print(f'Well done. The computer chose {comp_choice} and failed')
            score += 100
        elif results.get(game) == 'lose':
            print(f'Sorry, but the computer chose {comp_choice}')
            score += 0
        elif results.get(game) == 'draw':
            print(f'There is a draw ({comp_choice})')
            score += 50
        else:
            print('Bye!')
            break


main()
