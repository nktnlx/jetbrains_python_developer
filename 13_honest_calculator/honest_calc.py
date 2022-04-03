# STAGE 3
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
memory = float()


def is_digit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
        
        
def continue_calc():
    const = 0
    while const <= 0:
        answer = input(msg_5)
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        
        
def store_res(x):
    counter = 0
    while counter <= 0:
        answer = input(msg_4)
        if answer == 'y':
            return x
        elif answer == 'n':
            return float()
   

c = 0
while c <= 0:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(' ')
    
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    if is_digit(x) and is_digit(y):
        x = float(x)
        y = float(y)
        if oper in ['+', '-', '*', '/']:
            if oper == '+':
                result = x + y
                print(result)
                memory = store_res(result)
                if not continue_calc():
                    c += 1
            elif oper == '-':
                result = x - y
                print(result)
                memory = store_res(result)
                if not continue_calc():
                    c += 1
            elif oper == '*':
                result = x * y
                print(result)
                memory = store_res(result)
                if not continue_calc():
                    c += 1
            else:
                try:
                    result = x / y
                    print(result)
                    memory = store_res(result)
                    if not continue_calc():
                        c += 1
                except ZeroDivisionError:
                    print(msg_3)
                    continue
        else:
            print(msg_2)
    else:
        print(msg_1)


#-----------------------------------------------------------------------------
# STAGE 2
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."

# def is_digit(x):
#     try:
#         float(x)
#         return True
#     except ValueError:
#         return False

# c = 0
# while c <= 0:
#     print(msg_0)
#     calc = input()
#     x, oper, y = calc.split(' ')

#     if is_digit(x) and is_digit(y):
#         x = float(x)
#         y = float(y)
#         if oper in ['+', '-', '*', '/']:
#             if oper == '+':
#                 print(x + y)
#             elif oper == '-':
#                 print(x - y)
#             elif oper == '*':
#                 print(x * y)
#             else:
#                 try:
#                     print(x / y)
#                 except ZeroDivisionError:
#                     print(msg_3)
#                     continue
#             c += 1 
#         else:
#             print(msg_2)
#     else:
#         print(msg_1)
        

#-----------------------------------------------------------------------------
# STAGE 1
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

# def is_digit(x):
#     try:
#         float(x)
#         return True
#     except ValueError:
#         return False

# c = 0
# while c <= 0:
#     print(msg_0)
#     calc = input()
#     x, oper, y = calc.split(' ')

#     if is_digit(x) and is_digit(y):
#         if oper in ['+', '-', '*', '/']:
#             c += 1
#         else:
#             print(msg_2)
#     else:
#         print(msg_1)
