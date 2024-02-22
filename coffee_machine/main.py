from menu import menu, starting_stock

turn_off = False
no_stock = False

water_stock = starting_stock.get('water')
milk_stock = starting_stock.get('milk')
coffee_stock = starting_stock.get('coffee')
current_money = 0.00


def current_stock():
    """shows current water, milk, coffee, cash stock"""
    rounded_money = '%.2f' % current_money

    return f'Water: {water_stock}mL\nMilk: {milk_stock}mL\nCoffee: {coffee_stock}g\nMoney: ${rounded_money}'


def out_of_stock(drink):
    """gives error message when ingredients are out of stock"""
    water_req = menu.get(drink).get('ingredients').get('water')
    milk_req = menu.get(drink).get('ingredients').get('milk')
    coffee_req = menu.get(drink).get('ingredients').get('coffee')

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


def calculate_cash():
    """calculates cash value after selecting the number of coins """
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))

    quarter_value = 0.25 * quarters
    dime_value = 0.10 * dimes
    nickel_value = 0.05 * nickels
    penny_value = 0.01 * pennies

    total_money = quarter_value + dime_value + nickel_value + penny_value

    return total_money


def check_transaction(money_inserted):
    cash_req = menu.get(order).get('cost')

    if money_inserted < cash_req:
        print('Sorry, not enough money. Money refunded.')
    else:
        change = money_inserted - cash_req
        change = float('%.2f' % change)

        print(f'Here is ${change} dollars in change.')
        return cash_req


def make_coffee(drink):
    """deducts coffee resources to make drink from current stock"""
    water_req = menu.get(drink).get('ingredients').get('water')
    milk_req = menu.get(drink).get('ingredients').get('milk')
    coffee_req = menu.get(drink).get('ingredients').get('coffee')

    if milk_req is None:
        milk_req = 0

    delta_water = water_stock - water_req
    delta_milk = milk_stock - milk_req
    delta_coffee = coffee_stock - coffee_req

    delta_stock = [delta_water, delta_milk ,delta_coffee]

    return delta_stock


while not turn_off:
    order = input('What would you like? (espresso/latte/cappuccino): ')

    # off command turns of the coffee machine
    if order == 'off':
        turn_off = True
    # report command gives current resource stocks
    elif order == 'report':
        print(current_stock())
    else:
        # if ingredients are out of stock, error message given and turns off
        if out_of_stock(order):
            turn_off = True
        else:
            # gives response depending on sufficient cash for transaction
            order_cost = float(check_transaction(calculate_cash()))
            current_money += order_cost

            updated_stock = make_coffee(order)
            water_stock = updated_stock[0]
            milk_stock = updated_stock[1]
            coffee_stock = updated_stock[2]

            print(f'Here is your {order}. Enjoy!')
