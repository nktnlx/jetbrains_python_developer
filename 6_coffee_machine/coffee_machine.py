# STAGE 6 (final)
class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    # method to brew espresso
    def espresso(self, water, beans, cups, money):
        resources = [self.water // water,
                     self.beans // beans,
                     self.cups // cups]

        items = ['water', 'beans', 'cups']

        if all(resources):
            self.water -= water
            self.beans -= beans
            self.cups -= cups
            self.money += money
            print('I have enough resources, making you a coffee!')

        else:
            for ind, item in enumerate(resources):
                if item == 0:
                    print(f'Sorry, not enough {items[ind]}!')

    # method to brew latte
    def latte(self, water, milk, beans, cups, money):
        resources = [self.water // water,
                     self.milk // milk,
                     self.beans // beans,
                     self.cups // cups]

        items = ['water', 'milk', 'beans', 'cups']

        if all(resources):
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= cups
            self.money += money
            print('I have enough resources, making you a coffee!')

        else:
            for ind, item in enumerate(resources):
                if item == 0:
                    print(f'Sorry, not enough {items[ind]}!')

    # method to brew cappuccino
    def cappuccino(self, water, milk, beans, cups, money):
        resources = [self.water // water,
                     self.milk // milk,
                     self.beans // beans,
                     self.cups // cups]

        items = ['water', 'milk', 'beans', 'cups']

        if all(resources):
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= cups
            self.money += money
            print('I have enough resources, making you a coffee!')

        else:
            for ind, item in enumerate(resources):
                if item == 0:
                    print(f'Sorry, not enough {items[ind]}!')

    # cash collection method
    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    # filling coffee machine with the supplies
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))

    # representation method for printing the coffee machine status
    def __repr__(self):
        return f'''\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money\n'''


# function to run the script
def main():
    my_machine = CoffeeMachine()
    
    while True:
        action = input('\nWrite action (buy, fill, take, remaining, exit):\n')

        if action == 'remaining':
            print(my_machine)

        elif action == 'fill':
            my_machine.fill()

        elif action == 'take':
            my_machine.take()

        elif action == 'buy':
            choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::\n')
            if choice == 'back':
                continue
            elif choice == '1':
                my_machine.espresso(250, 16, 1, 4)
            elif choice == '2':
                my_machine.latte(350, 75, 20, 1, 7)
            elif choice == '3':
                my_machine.cappuccino(200, 100, 12, 1, 6)


        elif action == 'exit':
            break


if __name__ == '__main__':
    main()





# --------------------------------------------------------------------------
# STAGE 1
# print('''Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!''')


# STAGE 2
# cups = int(input('Write how many cups of coffee you will need:\n'))
#
# water = 200
# milk = 50
# beans = 15
#
# print(f'''For {cups} cups of coffee you will need:
# {water * cups} ml of water
# {milk * cups} ml of milk
# {beans * cups} g of coffee beans''')


# STAGE 3
# constants to brew one cup of coffee
# WATER = 200
# MILK = 50
# BEANS = 15
#
#
# # entering data about coffee machine load with ingredients
# def amount():
#     """
#     :rtype: tuple
#     """
#     water_available = int(input('Write how many ml of water the coffee machine has:\n'))
#     milk_available = int(input('Write how many ml of milk the coffee machine has:\n'))
#     beans_available = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
#
#     return water_available, milk_available, beans_available
#
#
# # logic beyond the machine making coffee
# def making_coffee(water, milk, beans):
#     cups_inp = int(input('Write how many cups of coffee you will need:\n'))
#
#     if water // WATER == cups_inp and milk // MILK == cups_inp and beans // BEANS >= 1:
#         print('Yes, I can make that amount of coffee')
#
#     elif water == 0 and milk == 0 and beans == 0 and cups_inp == 0:
#         print('Yes, I can make that amount of coffee')
#
#     elif water // WATER >= cups_inp and milk // MILK >= cups_inp and beans // BEANS >= 1:
#         cups = min([water // WATER, milk // MILK, beans // BEANS])
#         if cups == cups_inp:
#             print('Yes, I can make that amount of coffee')
#         else:
#             print(f'Yes, I can make that amount of coffee (and even {cups - cups_inp} more than that)')
#
#     elif water // WATER < cups_inp and milk // MILK < cups_inp and beans // BEANS >= 1:
#         cups = min([water // WATER, milk // MILK, beans // BEANS])
#         print(f'No, I can make only {cups} cups of coffee')
#
#
# water_in_machine, milk_in_machine, beans_in_machine = amount()
# making_coffee(water_in_machine, milk_in_machine, beans_in_machine)


# STAGE 4
# printing the current state of the coffee machine
# def status(water, milk, beans, cups, money):
#     print(f'''The coffee machine has:
# {water} of water
# {milk} of milk
# {beans} of coffee beans
# {cups} of disposable cups
# {money} of money''')
#
#     return water, milk, beans, cups, money
#
#
# # filling coffee machine with the supplies
# def fill(water, milk, beans, cups, money):
#     water_add = int(input('Write how many ml of water do you want to add:\n'))
#     milk_add = int(input('Write how many ml of milk do you want to add:\n'))
#     beans_add = int(input('Write how many grams of coffee beans do you want to add:\n'))
#     cups_add = int(input('Write how many disposable cups of coffee do you want to add:\n'))
#     money_add = 0
#
#     water += water_add
#     milk += milk_add
#     beans += beans_add
#     cups += cups_add
#     money += money_add
#
#     return water, milk, beans, cups, money
#
#
# # cash collection
# def take(water, milk, beans, cups, money):
#     print(f'I gave you ${money}')
#     money = 0
#
#     return water, milk, beans, cups, money
#
#
# # brewing coffee and updating coffee machine's supplies
# def buy(water, milk, beans, cups, money, beverage):
#     coffee = {'espresso': [250, 0, 16, 4],  # [water, milk, beans, money]
#               'latte': [350, 75, 20, 7],
#               'cappuccino': [200, 100, 12, 6]}
#
#     water -= coffee[beverage][0]
#     milk -= coffee[beverage][1]
#     beans -= coffee[beverage][2]
#     cups -= 1
#     money += coffee[beverage][3]
#
#     return water, milk, beans, cups, money
#
#
# # coffee machine operations logic
# def coffee_machine():
#     water, milk, beans, cups, money = status(water=400, milk=540, beans=120, cups=9, money=550)
#     action = input('\nWrite action (buy, fill, take):\n')
#
#     if action == 'fill':
#         water, milk, beans, cups, money = fill(water, milk, beans, cups, money)
#         print('')
#         status(water, milk, beans, cups, money)
#
#     elif action == 'take':
#         water, milk, beans, cups, money = take(water, milk, beans, cups, money)
#         print('')
#         status(water, milk, beans, cups, money)
#
#     elif action == 'buy':
#         menu = {'1': 'espresso',
#                 '2': 'latte',
#                 '3': 'cappuccino'}
#
#         choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
#         beverage = menu[choice]
#
#         water, milk, beans, cups, money = buy(water, milk, beans, cups, money, beverage)
#         print('')
#         status(water, milk, beans, cups, money)
#
#
# coffee_machine()


# STAGE 5
# printing the current state of the coffee machine
# def status(water, milk, beans, cups, money):
#     print(f'''\nThe coffee machine has:
# {water} of water
# {milk} of milk
# {beans} of coffee beans
# {cups} of disposable cups
# ${money} of money''')
#
#     return water, milk, beans, cups, money
#
#
# # filling coffee machine with the supplies
# def fill(water, milk, beans, cups, money):
#     water_add = int(input('Write how many ml of water do you want to add:\n'))
#     milk_add = int(input('Write how many ml of milk do you want to add:\n'))
#     beans_add = int(input('Write how many grams of coffee beans do you want to add:\n'))
#     cups_add = int(input('Write how many disposable cups of coffee do you want to add:\n'))
#     money_add = 0
#
#     water += water_add
#     milk += milk_add
#     beans += beans_add
#     cups += cups_add
#     money += money_add
#
#     return water, milk, beans, cups, money
#
#
# # cash collection
# def take(water, milk, beans, cups, money):
#     print(f'I gave you ${money}')
#     money = 0
#
#     return water, milk, beans, cups, money
#
#
# # brewing coffee and updating coffee machine's supplies
# def buy(water, milk, beans, cups, money, beverage):
#     coffee = {'espresso': [250, 0, 16, 4],  # [water, milk, beans, money]
#               'latte': [350, 75, 20, 7],
#               'cappuccino': [200, 100, 12, 6]}
#
#     resources = [water // coffee[beverage][0],
#                  [milk // coffee[beverage][1] if coffee[beverage][1] != 0 else milk],  # avoiding ZeroDivision for espresso
#                  beans // coffee[beverage][2],
#                  cups // 1]  # you always need one cup
#
#     items = ['water', 'milk', 'beans', 'cups']
#
#     if all(resources):
#         water -= coffee[beverage][0]
#         milk -= coffee[beverage][1]
#         beans -= coffee[beverage][2]
#         cups -= 1
#         money += coffee[beverage][3]
#         print('I have enough resources, making you a coffee!')
#         return water, milk, beans, cups, money
#
#     else:
#         for ind, item in enumerate(resources):
#             if str(item).find('0') != -1:
#                 print(f'Sorry, not enough {items[ind]}!')
#                 return water, milk, beans, cups, money
#
#
# # coffee machine operations logic
# def coffee_machine():
#     water, milk, beans, cups, money = 400, 540, 120, 9, 550
#
#     while True:
#         action = input('\nWrite action (buy, fill, take, remaining, exit):\n')
#
#         if action == 'remaining':
#             water, milk, beans, cups, money = status(water, milk, beans, cups, money)
#             continue
#
#         elif action == 'fill':
#             water, milk, beans, cups, money = fill(water, milk, beans, cups, money)
#             continue
#
#         elif action == 'take':
#             water, milk, beans, cups, money = take(water, milk, beans, cups, money)
#             continue
#
#         elif action == 'buy':
#             menu = {'1': 'espresso',
#                     '2': 'latte',
#                     '3': 'cappuccino'}
#
#             choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::\n')
#             if choice == 'back':
#                 continue
#             else:
#                 beverage = menu[choice]
#                 water, milk, beans, cups, money = buy(water, milk, beans, cups, money, beverage)
#                 continue
#
#         elif action == 'exit':
#             break


# coffee_machine()