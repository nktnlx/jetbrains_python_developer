# STAGE 5 (final)
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msgs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, msg_10, msg_11, msg_12]
memory = [0]


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
        if answer == "y":
            return True
        elif answer == "n":
            return False
        
        
def store_res(x):
    counter = 0
    c = 0
    while counter <= 0:
        answer = input(msg_4)
        if answer == "y":
            if is_one_digit(x):
                msg_idx = 10
                while c <=0:
                    answer = input(msgs[msg_idx])
                    if answer == "y":
                        if msg_idx < 12:
                            msg_idx += 1
                        else:
                            c += 1
                            counter += 1
                            return x
                    if answer == "n":
                        answer = "not store"
                        c += 1
            if answer == "not store":
                return float()
            return x
        elif answer == "n":
            return float()
        else:
          break
            
            
def is_one_digit(v):
    if v.is_integer() and (v > -10 and v < 10):
        return True
    else:
        return False
        
        
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1.0 or v2 == 1.0) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0.0 or v2 == 0.0) and (v3 in ["*", "+", "-"]):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        
        
c = 0
m_idx = 0
while c <= 0:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(' ')
 
    if x == "M":
        x = memory[m_idx]
    if y == "M":
        y = memory[m_idx]

    if is_digit(x) and is_digit(y):
        x = float(x)
        y = float(y)
        if oper in ["+", "-", "*", "/"]:
            check(x, y, oper)
            if oper == '+':
                result = x + y
                print(result)
                res = store_res(result)
                if res != 0:
                    memory.append(res)
                    m_idx += 1
                if not continue_calc():
                    c += 1
            elif oper == '-':
                result = x - y
                print(result)
                res = store_res(result)
                if res != 0:
                    memory.append(res)
                    m_idx += 1
                if not continue_calc():
                    c += 1
            elif oper == '*':
                result = x * y
                print(result)
                res = store_res(result)
                if res != 0:
                    memory.append(res)
                    m_idx += 1
                if not continue_calc():
                    c += 1
            else:
                try:
                    result = x / y
                    print(result)
                    res = store_res(result)
                    if res != 0:
                        memory.append(res)
                        m_idx += 1
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
# STAGE 4
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):" 
# msg_5 = "Do you want to continue calculations? (y / n):"
# msg_6 = " ... lazy"
# msg_7 = " ... very lazy"
# msg_8 = " ... very, very lazy"
# msg_9 = "You are"
# memory = float()


# def is_digit(x):
#     try:
#         float(x)
#         return True
#     except ValueError:
#         return False
        
        
# def continue_calc():
#     const = 0
#     while const <= 0:
#         answer = input(msg_5)
#         if answer == 'y':
#             return True
#         elif answer == 'n':
#             return False
        
        
# def store_res(x):
#     counter = 0
#     while counter <= 0:
#         answer = input(msg_4)
#         if answer == 'y':
#             return x
#         elif answer == 'n':
#             return float()
            
            
# def is_one_digit(v):
#     if v.is_integer() and (v > -10 and v < 10):
#         return True
#     else:
#         return False
        
        
# def check(v1, v2, v3):
#     msg = ""
#     if is_one_digit(v1) and is_one_digit(v2):
#         msg = msg + msg_6
#     if (v1 == 1.0 or v2 == 1.0) and v3 == "*":
#         msg = msg + msg_7
#     if (v1 == 0.0 or v2 == 0.0) and (v3 in ["*", "+", "-"]):
#         msg = msg + msg_8
#     if msg != "":
#         msg = msg_9 + msg
#         print(msg)
        
        
# c = 0
# while c <= 0:
#     print(msg_0)
#     calc = input()
#     x, oper, y = calc.split(' ')
    
#     if x == "M":
#         x = memory
#     if y == "M":
#         y = memory

#     if is_digit(x) and is_digit(y):
#         x = float(x)
#         y = float(y)
#         if oper in ['+', '-', '*', '/']:
#             check(x, y, oper)
#             if oper == '+':
#                 result = x + y
#                 print(result)
#                 memory = store_res(result)
#                 if not continue_calc():
#                     c += 1
#             elif oper == '-':
#                 result = x - y
#                 print(result)
#                 memory = store_res(result)
#                 if not continue_calc():
#                     c += 1
#             elif oper == '*':
#                 result = x * y
#                 print(result)
#                 memory = store_res(result)
#                 if not continue_calc():
#                     c += 1
#             else:
#                 try:
#                     result = x / y
#                     print(result)
#                     memory = store_res(result)
#                     if not continue_calc():
#                         c += 1
#                 except ZeroDivisionError:
#                     print(msg_3)
#                     continue
#         else:
#             print(msg_2)
#     else:
#         print(msg_1)
        

#-----------------------------------------------------------------------------
# STAGE 3
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):" 
# msg_5 = "Do you want to continue calculations? (y / n):"
# memory = float()


# def is_digit(x):
#     try:
#         float(x)
#         return True
#     except ValueError:
#         return False
        
        
# def continue_calc():
#     const = 0
#     while const <= 0:
#         answer = input(msg_5)
#         if answer == 'y':
#             return True
#         elif answer == 'n':
#             return False
        
        
# def store_res(x):
#     counter = 0
#     while counter <= 0:
#         answer = input(msg_4)
#         if answer == 'y':
#             return x
#         elif answer == 'n':
#             return float()
   

# c = 0
# while c <= 0:
#     print(msg_0)
#     calc = input()
#     x, oper, y = calc.split(' ')
    
#     if x == "M":
#         x = memory
#     if y == "M":
#         y = memory

#     if is_digit(x) and is_digit(y):
#         x = float(x)
#         y = float(y)
#         if oper in ['+', '-', '*', '/']:
#             if oper == '+':
#                 result = x + y
#                 print(result)
#                 memory = store_res(result)
#                 if not continue_calc():
#                     c += 1
#             elif oper == '-':
#                 result = x - y
#                 print(result)
#                 memory = store_res(result)
#                 if not continue_calc():
#                     c += 1
#             elif oper == '*':
#                 result = x * y
#                 print(result)
#                 memory = store_res(result)
#                 if not continue_calc():
#                     c += 1
#             else:
#                 try:
#                     result = x / y
#                     print(result)
#                     memory = store_res(result)
#                     if not continue_calc():
#                         c += 1
#                 except ZeroDivisionError:
#                     print(msg_3)
#                     continue
#         else:
#             print(msg_2)
#     else:
#         print(msg_1)


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
