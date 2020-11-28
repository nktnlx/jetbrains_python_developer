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
import random

user_inp = input()

# random choice of a computer
options = ['rock', 'paper', 'scissors']
comp_choice = random.choice(options)

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

# concatenating user and computer choices to receive a key for our dictionary
game = user_inp + comp_choice

# printing outcome
if results[game] == 'win':
    print(f'Well done. The computer chose {comp_choice} and failed')
elif results[game] == 'lose':
    print(f'Sorry, but the computer chose {comp_choice}')
elif results[game] == 'draw':
    print(f'There is a draw ({comp_choice})')
