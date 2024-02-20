MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
cost=0
print("Welcome to Aryamann's Coffee Parlour(ACP)!!!")
while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == 'off':
        break

    elif prompt == 'report':
        for ingredient, quantity in resources.items():
            print(f"{ingredient.capitalize()}: {quantity}g")

    elif prompt in MENU:
        drink = MENU[prompt]
        sufficient_resources = True

        for ingredient, quantity in drink['ingredients'].items():
            if resources[ingredient] < quantity:
                print(f"Sorry, we don't have enough {ingredient}")
                sufficient_resources = False
                break

        if sufficient_resources:
            cups=(int(input("Great! And How many cups will that be :) ")))
            cost=cups*drink['cost']
            print(f"Great Choice! That will be ${cost}")
            p = int(input("How many Pennies?: "))
            n = int(input("How many Nickels?: "))
            d = int(input("How many Dimes?: "))
            q = int(input("How many Quarters?: "))
            payment = 0.01 * p + 0.05 * n + 0.10 * d + 0.25 * q

            if payment < cost:
                print("Sorry, insufficient money given. Money refunded.")
            else:
                change = payment - cost
                print(f"Thanks! Your total change comes out to be ${change:.2f}")

                for ingredient, quantity in drink['ingredients'].items():
                    resources[ingredient] -= quantity
        else:
            print("Invalid choice. Try again.")

    else:
        print("Invalid choice. Please choose from the available options.")

print("Thanks For Coming!!!")
