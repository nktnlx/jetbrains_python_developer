# STAGE 1
def string_input():
    inp = input('Print a random string containing 0 or 1:\n')
    lst_filt = [i for i in inp if i in ('0', '1')]
    return lst_filt
    

def checking_length(lst, limit=100):
    while len(lst) < limit:
        print(f'Current data length is {len(lst)}, {limit - len(lst)} symbols left')
        temp = string_input()
        lst.extend(temp)
    print('\nFinal data string:')
    print(''.join(lst))
    
a = string_input()

checking_length(a)
