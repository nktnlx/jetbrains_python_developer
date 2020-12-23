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
# import sys
# sys.setrecursionlimit(10000)  # setting recursion limit
#
#
# # regex function for comparing a single character
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
# def equal_length(word1, word2):
#     if word1 == '':
#         return True
#     elif len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if single_char(word1[i], word2[i]):
#             continue
#         else:
#             return False
#     return True
#
#
# # regex function to compare multi-char strings of a different length
# def dif_length(user_inp):
#     word1, word2 = user_inp.split('|')[0], user_inp.split('|')[1]
#     if equal_length(word1, word2):
#         return True
#     elif not equal_length(word1, word2):
#         if len(word2) == 0:
#             return False
#         else:
#             for i in range(len(word2)):
#                 if word1 in word2[0:len(word1)]:
#                     return True
#                 elif not equal_length(word1, word2[i:]) and len(word2[i:]) != 1:
#                     continue
#                 else:
#                     return equal_length(word1, word2[i:])
#
#
# print(dif_length(input()))


# STAGE 4
# import sys
# sys.setrecursionlimit(10000)  # setting recursion limit
#
#
# # regex function for comparing a single character
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
# def equal_length(word1, word2):
#     if word1 == '':
#         return True
#     elif len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if single_char(word1[i], word2[i]):
#             continue
#         else:
#             return False
#     return True
#
#
# # regex function to compare multi-char strings of a different length
# def dif_length(user_inp):
#     word1, word2 = user_inp.split('|')[0], user_inp.split('|')[1]
#     if equal_length(word1, word2):
#         return True
#     elif word1[-1] == '$':
#         return dollar_sign(word1, word2)
#     elif not equal_length(word1, word2):
#         if len(word2) == 0:
#             return False
#         else:
#             for i in range(len(word2)):
#                 if word1[0] == '^':
#                     if word1[1:] in word2[0:len(word1)]:
#                         return True
#                     else:
#                         return False
#                 elif word1 in word2[0:len(word1)]:
#                     return True
#                 elif not equal_length(word1, word2[i:]) and len(word2[i:]) != 1:
#                     continue
#                 else:
#                     return equal_length(word1, word2[i:])
#
#
# # handling the $ metacharacter
# def dollar_sign(word1, word2):
#     word1 = word1[:-1]
#     if word1 == '.' and word2 != '':
#         return True
#     elif word1[0] == '^':
#         if word1[1:] in word2[0:len(word1)]:
#             try:
#                 word1 = word1[1:]
#                 word2_reversed = word2[::-1]
#                 idx_1 = word2.index(word1)
#                 idx_2 = word2[::-1].index(word2_reversed)
#                 if word1 == word2[idx_1:]:
#                     return True
#                 else:
#                     return False
#             except ValueError:
#                 return False
#     try:
#         word2_reversed = word2[::-1]
#         idx_1 = word2.index(word1)
#         idx_2 = word2[::-1].index(word2_reversed)
#         if word1 == word2[idx_1:]:
#             return True
#         else:
#             return False
#     except ValueError:
#         return False
#
#
# print(dif_length(input()))


# STAGE 5 (full)
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


# handling the ^ sign metacharacter
def caret(word1, word2):
    if not equal_length(word1, word2):
        if len(word2) == 0:
            return False
        else:
            for i in range(len(word2)):
                if word1[0] == '^':
                    if word1[1:] in word2[0:len(word1)]:
                        return True
                    elif '+' in word1[1:]:
                        return plus_sign(word1[1:], word2)
                    else:
                        return False
                elif word1 in word2[0:len(word1)]:
                    return True
                elif not equal_length(word1, word2[i:]) and len(word2[i:]) != 1:
                    continue
                else:
                    return equal_length(word1, word2[i:])


# handling the $ metacharacter
def dollar_sign(word1, word2):
    word1 = word1[:-1]
    if word1 == '.' and word2 != '':
        return True
    elif word1[0] == '^':
        if word1[1:] in word2[0:len(word1)]:
            try:
                word1 = word1[1:]
                idx_1 = word2.index(word1)
                if word1 == word2[idx_1:]:
                    return True
                else:
                    return False
            except ValueError:
                return False
    try:
        idx_1 = word2.index(word1)
        if word1 == word2[idx_1:]:
            return True
        else:
            return False
    except ValueError:
        if '^' in word1:
            return caret(word1, word2)
        else:
            return False


# handling the ? metacharacter
def question_mark(word1, word2):
    if '.?' == word1:
        return True
    try:
        idx = word1.index('?')
        word1_zero = word1[0:idx-1] + word1[idx+1:]
        word1_once = word1[0:idx] + word1[idx+1:]
        if word1_zero == word2 or word1_once == word2:
            return True
        else:
            return False
    except ValueError:
        return False


# handling the * and/or .* metacharacters
def asterisk(word1, word2):
    if '.*' == word1:
        return True
    elif '.*' in word1:
        idx_meta = word1.index('.*')
        word1 = word1[0:idx_meta] + word1[idx_meta+2:]
        word2 = word2[0:idx_meta] + word2[idx_meta + (len(word2) - len(word1)):]
        if word1[-1] == '$':
            return dollar_sign(word1, word2)
        elif word1 == word2:
            return True
    # when only '*' in word1
    try:
        idx = word1.index('*')
        word1_zero = word1[0:idx-1] + word1[idx+1:]
        word1_more = word1[0:idx] + word1[idx+1:]
        word2_more = word2[0:idx] + word2[idx + (len(word2) - len(word1_more)):]
        if word1_zero == word2 or word1_more == word2_more:
            return True
        else:
            return False
    except ValueError:
        return False


# handling the + sign metacharacter
def plus_sign(word1, word2):
    if '.+' == word1:
        return True
    elif '^' in word1:
        return caret(word1, word2)
    elif '.+' in word1:
        try:
            idx = word1.index('.+')
            word1_once = word1[0:idx] + word1[idx+2:]
            word1_more = word1[0:idx] + word1[idx+2:]
            word2_more = word2[0:idx] + word2[idx + (len(word2) - len(word1_more)):]
            if word1_once == word2 or word1_more == word2_more:
                return True
            else:
                return False
        except ValueError:
            return False
    try:
        idx = word1.index('+')
        word1_once = word1[0:idx] + word1[idx+1:]
        word1_more = word1[0:idx] + word1[idx+1:]
        word2_more = word2[0:idx] + word2[idx + (len(word2) - len(word1_more)):]
        if word1_once == word2 or word1_more == word2_more:
            return True
        else:
            return False
    except ValueError:
        return False


# regex function to compare multi-char strings of a different length
def dif_length(user_inp):
    word1, word2 = user_inp.split('|')[0], user_inp.split('|')[1]
    if equal_length(word1, word2):
        return True
    elif '*' in word1:
        return asterisk(word1, word2)
    elif word1[-1] == '$':
        return dollar_sign(word1, word2)
    elif '?' in word1:
        return question_mark(word1, word2)
    elif '+' in word1:
        return plus_sign(word1, word2)
    else:
        return caret(word1, word2)


print(dif_length(input()))
