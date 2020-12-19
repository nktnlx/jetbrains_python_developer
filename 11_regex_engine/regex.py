# STAGE 1
# def reg_func():
#     user_inp = input()
#     regex, inp = user_inp.split('|')[0], user_inp.split('|')[1]
#     if regex == '' or regex == '.':
#         return True
#     elif inp == '':
#         return False
#     elif regex == inp:
#         return True
#     else:
#         return False
#
#
# print(reg_func())


# STAGE 2
# regex function for comparing a single character
# def single_char(regex, inp):
#     if regex == '' or regex == '.':
#         return True
#     elif inp == '':
#         return False
#     elif regex == inp:
#         return True
#     else:
#         return False
#
#
# # regex function to compare multi-char strings of the same length
# def multi_char(user_inp):
#     word1, word2 = user_inp.split('|')[0], user_inp.split('|')[1]
#     if word1 == '':
#         return True
#     elif len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if single_char(word1[i], word2[i]):  # recursive call (checking letter by letter)
#             continue
#         else:
#             return False
#     return True
#
#
# print(multi_char(input()))


# STAGE 3
import sys
sys.setrecursionlimit(10000)  # setting recursion limit


# regex function for comparing a single character
def single_char(regex, inp):
    if regex == '' or regex == '.':
        return True
    elif inp == '':
        return False
    elif regex == inp:
        return True
    else:
        return False


# regex function to compare multi-char strings of the same length
def equal_length(word1, word2):
    if word1 == '':
        return True
    elif len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if single_char(word1[i], word2[i]):
            continue
        else:
            return False
    return True


# regex function to compare multi-char strings of a different length
def dif_length(user_inp):
    word1, word2 = user_inp.split('|')[0], user_inp.split('|')[1]
    if equal_length(word1, word2):
        return True
    elif not equal_length(word1, word2):
        if len(word2) == 0:
            return False
        else:
            for i in range(len(word2)):
                if word1 in word2[0:len(word1)]:
                    return True
                elif not equal_length(word1, word2[i:]) and len(word2[i:]) != 1:
                    continue
                else:
                    return equal_length(word1, word2[i:])


print(dif_length(input()))
