def greet(bot_name, birth_year):
    print('\nHello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + ' by nktn.lx@gmal.com.')


def remind_name():
    print('\nPlease, remind me your name:')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('\nLet me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input('Reminder of dividing by 3: '))
    rem5 = int(input('Reminder of dividing by 5: '))
    rem7 = int(input('Reminder of dividing by 7: '))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a perfect time to start programming!")


def count():
    print('\nNow I will prove to you that I can count to any number you want:')

    num = int(input('Please, enter a natural number: '))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print('"Python keyword arguments can be passed in a different order then they were defined in the function?"')
    print('''
    1. False
    2. I don't know yet.
    3. True
    4. Whaaat?
    ''')
    answer = int(input('Please, enter your answer: '))
    if answer != 3:
        print('Nope! Please, try again:\n')
        test()
    else:    
        print('Correct. You are a genius!')


def end():
    print('\nCongratulations, have a nice day!.. \nand call me when you miss me.')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
print("\nLet's test your programming knowledge:")
test()
end()
