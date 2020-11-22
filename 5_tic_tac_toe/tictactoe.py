# STAGE 1
# printing a random game result
import random

options = ['O', 'X']

lines = [[random.choice(options) for i in range(3)] for _ in range(3)]

for line in lines:
    print(line[0], line[1], line[2], sep=' ')

