from menu import MENU, resources

turn_off = False
out_of_stock = False

water_stock = resources.get('water')
milk_stock = resources.get('milk')
coffee_stock = resources.get('coffee')
current_cash = 0


def current_resources():
    """returns current amount of water, milk, coffee, money"""
    return f'Water: {water_stock}mL\nMilk: {milk_stock}mL\nCoffee: {coffee_stock}g\nMoney: ${money}'


def check_resources(drink):
    """gives error message when insufficient resources to make drinks"""
    water_req = MENU.get(drink).get('ingredients').get('water')
    milk_req = MENU.get(drink).get('ingredients').get('milk')
    coffee_req = MENU.get(drink).get('ingredients').get('coffee')

    if milk_req is None:
        milk_req = 0

    missing_ingredient = ''

    if water_stock < water_req:
        missing_ingredient += 'water'
    elif milk_stock < milk_req:
        missing_ingredient += 'milk'
    elif coffee_stock < coffee_req:
        missing_ingredient += 'coffee'

    if missing_ingredient != '':
        print(f'Sorry there is not enough {missing_ingredient}.')
        return True


while not turn_off:
    order = input('What would you like? (espresso/latte/cappuccino): ')

    if order == 'off':
        turn_off = True
    elif order == 'report':
        print(current_resources())
    else:
        if check_resources(order):
            turn_off = True
        else:

