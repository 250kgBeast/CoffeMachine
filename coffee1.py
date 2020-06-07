coffeeMachine = {
    "water": 400,
    "milk": 540,
    "beans": 120,
    "cups": 9,
    "money": 550
}
espresso = {
    "water": 250,
    "beans": 16,
    "cups": 1,
}
latte = {
    "water": 350,
    "milk": 75,
    "beans": 20,
    "cups": 1,
}
cappuccino = {
    "water": 200,
    "milk": 100,
    "beans": 12,
    "cups": 1,
}


def ingredient_check(coffee):
    global coffeeMachine
    action = True
    for k in coffee.keys():
        if coffeeMachine[k] < coffee[k]:
            print("Sorry, not enough {}!".format(k))
            action = False
            break
    if action:
        print("I have enough resources, making you a coffee!")
        if coffee == espresso:
            coffeeMachine["money"] += 4
        elif coffee == latte:
            coffeeMachine["money"] += 7
        elif coffee == cappuccino:
            coffeeMachine["money"] += 6
        for k in coffee.keys():
            coffeeMachine[k] -= coffee[k]


def remaining():
    print('''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money
'''.format(coffeeMachine["water"], coffeeMachine["milk"], coffeeMachine["beans"], coffeeMachine["cups"],
           coffeeMachine["money"]))


def buy():
    global espresso
    global latte
    global cappuccino
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    coffee = input()
    if coffee == "1":
        ingredient_check(espresso)
    if coffee == "2":
        ingredient_check(latte)
    if coffee == "3":
        ingredient_check(cappuccino)
    if coffee == "back":
        action()


def fill():
    water = int(input("Write how many ml of water do you want to add: "))
    coffeeMachine["water"] += water
    milk = int(input("Write how many ml of milk do you want to add: "))
    coffeeMachine["milk"] += milk
    beans = int(input("Write how many grams of coffee beans do you want to add: "))
    coffeeMachine["beans"] += beans
    cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    coffeeMachine["cups"] += cups


def take():
    print("I gave you {}".format(coffeeMachine["money"]))
    coffeeMachine["money"] -= coffeeMachine["money"]


def action():
    global coffeeLoop
    print("Write action (buy, fill, take, remaining, exit): ")
    coffeeMachineAction = input()
    if coffeeMachineAction == "buy":
        return buy()
    elif coffeeMachineAction == "fill":
        return fill()
    elif coffeeMachineAction == "take":
        return take()
    elif coffeeMachineAction == "remaining":
        return remaining()
    elif coffeeMachineAction == "exit":
        coffeeLoop = False


coffeeLoop = True
while coffeeLoop:
    action()
