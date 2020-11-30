# STAGE 5 (final)
import random


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


# choosing the game type
def choose_game():
    options_inp = input()  # comma separated user input
    if options_inp:
        options = options_inp.split(',')
    else:
        options = ['rock', 'paper', 'scissors']  # classic variant of the game

    print('Okay, let\'s start')

    return options


# playing the game
def main():
    score = enter_name(reading_rating())
    all_options = choose_game()
    while True:
        user_inp = input()
        comp_choice = random.choice(all_options)

        # dealing with invalid input and !rating and !exit options
        if user_inp == '!rating':
            print(f'Your rating: {score}')
            continue
        elif user_inp not in all_options and user_inp != '!exit':
            print('Invalid input')
            continue
        elif user_inp == '!exit':
            print('Bye!')
            break

        # defining the losing words list and winning words list
        user_idx = [idx for idx, val in enumerate(all_options) if val == user_inp][0]
        # calculate the length of a win/lose list
        len_win_lst = (len(all_options) - 1) // 2
        # putting all words right to the user_input being in a win list
        win_lst = all_options[user_idx+1:user_idx+1+len_win_lst]
        # adding words to the win list if it is still no full after the previous step
        if len(win_lst) < len_win_lst:
            for i in range(0, len_win_lst - len(win_lst)):
                win_lst.append(all_options[i])
        # creating a lose words list by removing the user_input word and all words in the win list
        lose_lst = all_options.copy()
        lose_lst.remove(user_inp)
        for word in win_lst:
            lose_lst.remove(word)

        # game logic
        if comp_choice in win_lst:
            print(f'Sorry, but the computer chose {comp_choice}')
            score += 0
        elif comp_choice in lose_lst:
            print(f'Well done. The computer chose {comp_choice} and failed')
            score += 100
        elif user_inp == comp_choice:
            print(f'There is a draw ({comp_choice})')
            score += 50


main()




# ----------------------------------------------------------------------------------------
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
# # reading rating list
# def reading_rating():
#     # reading current rating from a rating.txt file
#     f = open('rating.txt', 'r')
#     user_list = f.readlines()
#
#     # splitting names and scores
#     for i in range(len(user_list)):
#         user_list.append(user_list[i].split())  # now we have a list of double size
#
#     # removing artefacts from the list
#     for i in range(int(len(user_list) / 2)): # len of the initial list
#         c = 0
#         user_list.pop(0)
#
#     return user_list
#
#
# # entering user name and searching for his rating
# def enter_name(user_list):
#     user_name = input('Enter your name: ')
#
#     for nested_list in user_list:
#         if user_name in nested_list:
#             print(f'Hello, {user_name}')
#             rating = nested_list[1]
#             return int(rating)
#     else:
#         print(f'Hello, {user_name}')
#         rating = 0
#         return rating
#
#
# # playing the game
# def main():
#     score = enter_name(reading_rating())
#     while True:
#         user_inp = input()
#         comp_choice = random.choice(options)
#         game = user_inp + comp_choice   # concatenating user and computer choices to receive a key for our dictionary
#
#         if user_inp == '!rating':
#             print(f'Your rating: {score}')
#         elif user_inp not in options and user_inp != '!exit':
#             print('Invalid input')
#         elif results.get(game) == 'win':
#             print(f'Well done. The computer chose {comp_choice} and failed')
#             score += 100
#         elif results.get(game) == 'lose':
#             print(f'Sorry, but the computer chose {comp_choice}')
#             score += 0
#         elif results.get(game) == 'draw':
#             print(f'There is a draw ({comp_choice})')
#             score += 50
#         else:
#             print('Bye!')
#             break
#
#
# main()