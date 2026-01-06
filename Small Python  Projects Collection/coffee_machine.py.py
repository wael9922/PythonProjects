MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18,},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
	"money": 0
}


# from resources import MENU, resources

is_on = True

def report():
    """Return the machines resources"""
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"


def get_ingredients(order):
    """get the ingredient for the ordered drink"""
    return MENU[order]['ingredients']


def check_resources(drink):
    """Check if machine has enough resources to prepare the coffee"""
    if drink.lower() == "espresso":
        if (
            resources['water'] >= MENU[drink]['ingredients']['water']
            and resources['coffee'] >= MENU['espresso']['ingredients']['coffee']
            ):
            return True
        else:
            return False

    elif drink.lower() == "latte":
        if (
            resources['water'] >= MENU['latte']['ingredients']['water'] and
            resources['coffee'] >= MENU['latte']['ingredients']['coffee'] and
            resources['milk'] >= MENU['latte']['ingredients']['milk']
        ):
            return True
        else:
            return False

    elif drink.lower() == "cappuccino":
        if (
            resources['water'] >= MENU['cappuccino']['ingredients']['water'] and
            resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] and
            resources['milk'] >= MENU['cappuccino']['ingredients']['milk']
        ):
            return True
        else:
            return False


def coin_processor():
    """prcess the money payed by the customer"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    pay = (pennies*0.01) + (dimes*0.1) + (nickles*0.05) + (quarters*0.25)
    return pay


def check_transaction(drink,pays):
    """Check if the payment is valid"""
    if drink.lower() == "espresso":
        if pays >= MENU['espresso']['cost']:
            resources['money'] +=  MENU['espresso']['cost']
            return pays - MENU['espresso']['cost']
        else:
            return "Sorry that's not enough money. Money refunded."
    elif drink.lower() == "latte":
        if pays >= MENU['latte']['cost']:
            resources['money'] +=  MENU['latte']['cost']
            return pays - MENU['latte']['cost']
        else:
            return "Sorry that's not enough money. Money refunded."

    elif drink.lower() == "cappuccino":
        if pays >= MENU['cappuccino']['cost']:
            resources['money'] +=  MENU['cappuccino']['cost']
            return pays - MENU['cappuccino']['cost']
        else:
            return "Sorry that's not enough money. Money refunded."


while is_on:
    order = input(f"What would you like? {tuple(MENU.keys())}: ").lower()
    if order == 'off':
        is_on = False
    elif order == 'report':
        print(report())
    else:
        if check_resources(order):
            payment = coin_processor()
            transaction = check_transaction(order, payment)

            if transaction != "Sorry that's not enough money. Money refunded.":
                print(f"Here is ${transaction} in change.")
                print(f"Here is your {order}, Enjoy!")
                ingredients = get_ingredients(order)

                if order == 'espresso':
                    resources['water'] -= ingredients['water']
                    resources['coffee'] -= ingredients['coffee']
                else:
                    resources['water'] -= ingredients['water']
                    resources['coffee'] -= ingredients['coffee']
                    resources['milk'] -= ingredients['milk']

            else:
                print(transaction)
        else:
            print("Sorry, there is not enough resources to prepare your order.")


