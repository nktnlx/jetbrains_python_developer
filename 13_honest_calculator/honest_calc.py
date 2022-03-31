# STAGE 1
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

def is_digit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

c = 0
while c <= 0:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(' ')

    if is_digit(x) and is_digit(y):
        if oper in ['+', '-', '*', '/']:
            c += 1
        else:
            print(msg_2)
    else:
        print(msg_1)
        