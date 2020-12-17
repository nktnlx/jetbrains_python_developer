# STAGE 1
def reg_func():
    user_inp = input()
    regex, inp = user_inp.split('|')[0], user_inp.split('|')[1]
    if regex == '' or regex == '.':
        return True
    elif inp == '':
        return False
    elif regex == inp:
        return True
    else:
        return False


print(reg_func())
