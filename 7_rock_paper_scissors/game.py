# STAGE 1
user_choice = input()

if user_choice == 'scissors':
    computer_choice = 'rock'
    print(f'Sorry, but the computer chose {computer_choice}')

elif user_choice == 'rock':
    computer_choice = 'paper'
    print(f'Sorry, but the computer chose {computer_choice}')

elif user_choice == 'paper':
    computer_choice = 'scissors'
    print(f'Sorry, but the computer chose {computer_choice}')
