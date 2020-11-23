# STAGE 1
# printing a random game result
# import random
#
# options = ['O', 'X']
#
# lines = [[random.choice(options) for i in range(3)] for _ in range(3)]
#
# for line in lines:
#     print(line[0], line[1], line[2], sep=' ')


# STAGE 2
# user_inp = input('Enter cells: ')
#
#
# line2 = '| ' + user_inp[0] + ' ' + user_inp[1] + ' ' + user_inp[2] + ' |'
# line3 = '| ' + user_inp[3] + ' ' + user_inp[4] + ' ' + user_inp[5] + ' |'
# line4 = '| ' + user_inp[6] + ' ' + user_inp[7] + ' ' + user_inp[8] + ' |'
# line1 = '-' * len(line2)
# line5 = line1
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# print(line5)


# STAGE 3
# gathering user input
# user_inp = input('Enter cells: ')
#
#
# # defining the game field based on user input
# def field(inp):
#     matrix = []
#     matrix.append('| ' + inp[0] + ' ' + inp[1] + ' ' + inp[2] + ' |')  # creating line 2
#     width = len(matrix[0])  # width of game field
#     matrix.append('-' * width)  # creating line 1
#     matrix.append('| ' + inp[3] + ' ' + inp[4] + ' ' + inp[5] + ' |')  # creating line 3
#     matrix.append('| ' + inp[6] + ' ' + inp[7] + ' ' + inp[8] + ' |')  # creating line 4
#     matrix.append('-' * width)  # creating line 5
#     matrix[0], matrix[1] = matrix[1], matrix[0]  # swapping line 1 and line 2
#     return matrix
#
#
# # finding the game state
# def game_states(state):
#     dia_1 = state[1][2] + state[2][4] + state[3][6]  # creating diagonal TopLeft - RightBottom
#     dia_2 = state[1][6] + state[2][4] + state[3][2]  # creating diagonal TopRight - BottomLeft
#     col_1, col_2, col_3 = ['' for _ in range(3)]
#
#     x_count = 0
#     o_count = 0
#     for el in state[1:4]:
#         col_1 += el[2]  # creating leftmost column
#         col_2 += el[4]  # creating central column
#         col_3 += el[6]  # creating rightmost column
#         x_count += el.count('X')  # counting X elements on the field
#         o_count += el.count('O')  # counting O elements on the field
#
#     result = []
#     for el in state[1:4]:
#         if el.count('X') == 3 or dia_1.count('X') == 3 or dia_2.count('X') == 3 or col_1.count('X') == 3 or col_2.count('X') == 3 or col_3.count('X') == 3:
#             result.append('X wins')
#         if el.count('O') == 3 or dia_1.count('O') == 3 or dia_2.count('O') == 3 or col_1.count('O') == 3 or col_2.count('O') == 3 or col_3.count('O') == 3:
#             result.append('O wins')
#         if abs(x_count - o_count) >= 2 or len(result) == 2:
#             return 'Impossible'
#         if (el.count('X') < 3 or el.count('O') < 3) and '_' in el:
#             return 'Game not finished'
#         if not result:
#             return 'Draw'
#         if result[0] == 'X wins':
#             return 'X wins'
#         if result[0] == 'O wins':
#             return 'O wins'
#
#
# game = field(user_inp)
#
# [print(item) for item in game]  # visualizing the game
# print(game_states(game))  # returning the game state



# STAGE 4
import string

user_inp = input('Enter cells: ')


# defining the game field based on user input
def field(inp):
    matrix = []
    matrix.append('| ' + inp[0] + ' ' + inp[1] + ' ' + inp[2] + ' |')  # creating line 2
    width = len(matrix[0])  # width of game field
    matrix.append('-' * width)  # creating line 1
    matrix.append('| ' + inp[3] + ' ' + inp[4] + ' ' + inp[5] + ' |')  # creating line 3
    matrix.append('| ' + inp[6] + ' ' + inp[7] + ' ' + inp[8] + ' |')  # creating line 4
    matrix.append('-' * width)  # creating line 5
    matrix[0], matrix[1] = matrix[1], matrix[0]  # swapping line 1 and line 2
    return matrix


# a dictionary that matches indexes with coordinates of each cell on the game field:
# suppose the bottom left cell has the coordinates (1, 1)
# and the top right cell has the coordinates (3, 3)
coord_dict = {0: 13,
              1: 23,
              2: 33,
              3: 12,
              4: 22,
              5: 32,
              6: 11,
              7: 21,
              8: 31}


# finding empty cells on the game field
def empty(inp):
    empty_cells = []
    for ind, val in enumerate(user_inp):
        if val == '_':
            empty_cells.append(ind)
    return empty_cells


# entering coordinates of the next move
def enter_coord(cells):
    while True:
        user = input('Enter the coordinates: ')

        if user.replace(' ', '')[0] not in string.digits or user.replace(' ', '')[1] not in string.digits:
            print('You should enter numbers!')
            continue
        elif int(user[0]) > 3 or int(user[2]) > 3:
            print('Coordinates should be from 1 to 3!')
            continue

        user_choice = int(user.replace(' ', ''))

        # switching from string index to coordinates of empty cells
        empty_coords = []
        for ind in cells:
            empty_coords.append(coord_dict[ind])

        if user_choice not in empty_coords:
            print('This cell is occupied! Choose another one!')
            continue
        else:
            for k, v in coord_dict.items():  # converting coordinate back to string index
                if v == user_choice:
                    user_choice_ind = k

        return user_choice_ind


# prints the 'X' symbol due to entered coordinates of the user
def next_move(inp, user_choice):
    lst = list(inp)
    lst[user_choice] = 'X'
    inp = ''.join(lst)
    return inp


game = field(user_inp)
[print(item) for item in game]  # visualizing the game

new_cells = empty(user_inp)
user_ind = enter_coord(new_cells)
next_field = next_move(user_inp, user_ind)

game = field(next_field)
[print(item) for item in game]  # visualizing the game after users input
