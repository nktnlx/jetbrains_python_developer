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
def multi_char(user_inp):
    word1, word2 = user_inp.split('|')[0], user_inp.split('|')[1]
    if word1 == '':
        return True
    elif len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if single_char(word1[i], word2[i]):  # recursive call (checking letter by letter)
            continue
        else:
            return False
    return True


print(multi_char(input()))
