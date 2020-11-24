# Write your code here
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
WATER = 200
MILK = 50
BEANS = 15


# entering data about coffee machine load with ingredients
def amount():
    """
    :rtype: tuple
    """
    water_available = int(input('Write how many ml of water the coffee machine has:\n'))
    milk_available = int(input('Write how many ml of milk the coffee machine has:\n'))
    beans_available = int(input('Write how many grams of coffee beans the coffee machine has:\n'))

    return water_available, milk_available, beans_available


# logic beyond the machine making coffee
def making_coffee(water, milk, beans):
    cups_inp = int(input('Write how many cups of coffee you will need:\n'))

    if water // WATER == cups_inp and milk // MILK == cups_inp and beans // BEANS >= 1:
        print('Yes, I can make that amount of coffee')

    elif water == 0 and milk == 0 and beans == 0 and cups_inp == 0:
        print('Yes, I can make that amount of coffee')

    elif water // WATER >= cups_inp and milk // MILK >= cups_inp and beans // BEANS >= 1:
        cups = min([water // WATER, milk // MILK, beans // BEANS])
        if cups == cups_inp:
            print('Yes, I can make that amount of coffee')
        else:
            print(f'Yes, I can make that amount of coffee (and even {cups - cups_inp} more than that)')

    elif water // WATER < cups_inp and milk // MILK < cups_inp and beans // BEANS >= 1:
        cups = min([water // WATER, milk // MILK, beans // BEANS])
        print(f'No, I can make only {cups} cups of coffee')


water_in_machine, milk_in_machine, beans_in_machine = amount()
making_coffee(water_in_machine, milk_in_machine, beans_in_machine)










