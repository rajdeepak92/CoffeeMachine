# create a coffee machine which is coin operated(esspresso , latte , cappucino )
# coins paisa = 0.05 , tanka = 0.10 , note = 0.25
# requirements
#
# 1.print report
# 2.sufficiency
# 3.Process value.
# 4.transaction successful
# 5.make a coffee
# 6.deduct the value of resource if success or dont give
# --------------------------------------------------------------------------------------------------
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
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

profit = 0

resources = {
    "water": 300,
    "milk":200,
    "coffee":100,
}

def is_resource_sufficient(order_ingredients):
   # '''returns true when order can be made,false if ingrediants insufficient
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    # '''returns the total calculated from coins inserted'''
    print("Please insert coins.")
    total = int(input("how many quarters? :")) * 0.25
    total = int(input("how many dime? :")) * 0.1
    total = int(input("how many nickles? :")) * 0.05
    total = int(input("how many pennies? :")) * 0.01
    return total


def is_transanction_successful(money_received , drink_cost):
    # '''return True when the payment is accepted , or false if money 
    #     is insifficient.and process refund'''
    if money_received >= drink_cost:
        change  = round(money_received - drink_cost , 2)
        print(f"here is the {change}$ , returned ")
        global profit
        profit +=  drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded ")
        return False


def make_coffee(drink_name , order_ingredients):
    # '''deduct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy!!")


is_on = True


while True:

    choice = input("What would you like to drink ? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"coffee = {resources['coffee']}gms")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient["ingrediants"]:
            payment =  process_coins()
            if is_transanction_successful(payment, drink["cost"]):
                make_coffee(choice , drink["ingrediants"])


        
