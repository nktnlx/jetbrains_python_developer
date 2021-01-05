# STAGE 1
# class Calculator:
#     def __init__(self, nums):
#         self.nums = nums
#
#     def addition(self):
#         return self.nums[0] + self.nums[1]
#
#
# my_calc = Calculator([int(x) for x in input().split()])
# print(my_calc.addition())


# STAGE 2
# import sys
#
#
# class Calculator:
#     def __init__(self, nums):
#         self.nums = nums
#
#     def addition(self):
#         return self.nums[0] + self.nums[1]
#
#     def menu(self):
#         if not self.nums:  # doing nothing if no input was given
#             pass
#         elif self.nums[0] == '/exit':  # exiting the script when user enter the exit command
#             print('Bye!')
#             return sys.exit()
#         elif len(self.nums) == 2:  # passing numbers to addition if two numbers were provided as input
#             self.nums = [int(x) for x in self.nums]
#             return self.addition()
#         elif len(self.nums) == 1:  # returning the number if only one number was provided as input
#             return self.nums[0]
#
#
# while True:
#     my_calc = Calculator(input().split())
#     if my_calc.menu() is None:  # doing nothing if no input was given
#         continue
#     else:
#         print(my_calc.menu())  # printing the result if input was provided


# STAGE 3
# import sys
#
#
# class Calculator:
#     def __init__(self, nums):
#         self.nums = nums
#
#     @property
#     def addition(self):
#         # noinspection PyAttributeOutsideInit
#         self.sum_ = 0
#         for number in self.nums:
#             self.sum_ += number
#         return self.sum_
#
#     def menu(self):
#         if not self.nums:  # doing nothing if no input was given
#             pass
#         elif self.nums[0] == '/exit':  # exiting the script when user enter the exit command
#             print('Bye!')
#             return sys.exit()
#         elif self.nums[0] == '/help':  # adding a '/help' command to print some information about the program.
#             return 'The program calculates the sum of numbers'
#         elif len(self.nums) >= 2:  # passing numbers to addition if two numbers were provided as input
#             self.nums = [int(x) for x in self.nums]
#             return self.addition
#         elif len(self.nums) == 1:  # returning the number if only one number was provided as input
#             return self.nums[0]
#
#
# while True:
#     my_calc = Calculator(input().split())
#     if my_calc.menu() is None:  # doing nothing if no input was given
#         continue
#     else:
#         print(my_calc.menu())  # printing the result if input was provided


# STAGE 4
import sys


class Calculator:
    def __init__(self, nums):
        self.nums = nums
        self.sum_ = 0

    def addition(self, lst):
        for idx, val in enumerate(lst):
            if '+' in val:
                continue
            elif '-' in val and val.count('-') % 2 == 0:
                continue
            elif '-' in val and val.count('-') == len(val):
                self.sum_ -= int(lst[idx + 1])
                lst.remove(lst[idx + 1])
            elif '-' in val:
                self.sum_ += int(val)
            else:
                self.sum_ += int(val)
        return self.sum_

    def menu(self):
        if not self.nums:  # doing nothing if no input was given
            pass
        elif self.nums[0] == '/exit':  # exiting the script when user enter the exit command
            print('Bye!')
            return sys.exit()
        elif self.nums[0] == '/help':  # adding a '/help' command to print some information about the program.
            return 'The program performs addition and subtraction'
        elif len(self.nums) >= 2:  # passing numbers to addition if two numbers were provided as input
            self.nums = [item for item in self.nums if item != '']
            print(self.addition(self.nums))
        elif len(self.nums) == 1:  # returning the number if only one number was provided as input
            return self.nums[0]


while True:
    my_calc = Calculator(input().split())
    if my_calc.menu() is None:  # doing nothing if no input was given
        continue
    else:
        print(my_calc.menu())  # printing the result if input was provided
