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
user_inp = input('Enter cells: ')


line2 = '| ' + user_inp[0] + ' ' + user_inp[1] + ' ' + user_inp[2] + ' |'
line3 = '| ' + user_inp[3] + ' ' + user_inp[4] + ' ' + user_inp[5] + ' |'
line4 = '| ' + user_inp[6] + ' ' + user_inp[7] + ' ' + user_inp[8] + ' |'
line1 = '-' * len(line2)
line5 = line1

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
