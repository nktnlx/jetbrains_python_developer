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
cups = int(input('Write how many cups of coffee you will need:\n'))

water = 200
milk = 50
beans = 15

print(f'''For {cups} cups of coffee you will need:
{water * cups} ml of water
{milk * cups} ml of milk
{beans * cups} g of coffee beans''')
