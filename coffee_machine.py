class CoffeeMachine:
    def __init__(self) -> None:
        self.state = 'main menu'
        self.resources = {
            'water': 400,
            'milk': 540,
            'beans': 120,
            'cups': 9,
            'money': 550,
        }
        self.drink_types = {
            '1': {
                "water": -250,
                "beans": -16,
                "money": 4
            },
            '2': {
                "water": -350,
                "milk": -75,
                "beans": -20,
                "money": 7
            },
            '3': {
                "water": -200,
                "milk": -100,
                "beans": -12,
                "money": 6
            }
        }
        self.main_menu()

    def main_menu(self) -> None:
        print("Write action (buy, fill, take, remaining, exit):")

    def buy_menu(self) -> None:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

    def filling_menu(self) -> None:
        if self.state == 'filling water':
            print("Write how many ml of water do you want to add:")
        elif self.state == 'filling milk':
            print('Write how many ml of milk do you want to add:')
        elif self.state == 'filling beans':
            print('Write how many grams of coffee beans do you want to add:')
        elif self.state == 'filling cups':
            print('Write how many disposable cups of coffee do you want to add:')
        elif self.state == 'main menu':
            self.main_menu()

    def interact(self, input_string) -> None:
        if self.state == 'main menu':

            if input_string == 'exit':
                self.state = 'turned off'
            elif input_string == 'buy':
                self.state = 'choosing product'
                self.buy_menu()
            elif input_string == 'fill':
                self.state = 'filling water'
                self.filling_menu()
            elif input_string == 'take':
                self.take()
                self.main_menu()
            elif input_string == 'remaining':
                self.remaining()
                self.main_menu()

        elif self.state.startswith('filling'):
            self.fill(int(input_string))
            self.filling_menu()
        elif self.state == 'choosing product':
            if input_string != 'back':
                self.buy(input_string)
            self.main_menu()
            self.state = 'main menu'

    def buy(self, choice):
        if self.enough_resources(choice):
            print("I have enough resources, making you a coffee!")
            drink = self.drink_types[choice]
            for key in drink:
                self.resources[key] += drink[key]
            self.resources['cups'] -= 1

    def enough_resources(self, n) -> bool:
        drink = self.drink_types[n]

        for key in drink:
            if not self.resources[key] >= abs(drink[key]):
                print(f"Sorry, not enough {key}!")
                return False
        return True

    def fill(self, amount) -> None:
        if self.state == 'filling water':
            self.resources['water'] += amount
            self.state = 'filling milk'
        elif self.state == 'filling milk':
            self.resources['milk'] += amount
            self.state = 'filling beans'
        elif self.state == 'filling beans':
            self.resources['beans'] += amount
            self.state = 'filling cups'
        elif self.state == 'filling cups':
            self.resources['cups'] += amount
            self.state = 'main menu'

    def take(self) -> None:
        print(f'I gave you ${self.resources["money"]}')
        self.resources['money'] = 0

    def remaining(self) -> None:
        print("The coffee machine has:")
        print(f"{self.resources['water']} of water")
        print(f"{self.resources['milk']} of milk")
        print(f"{self.resources['beans']} of coffee beans")
        print(f"{self.resources['cups']} of disposable cups")
        print(f"${self.resources['money']} of money")


cm = CoffeeMachine()

while cm.state != 'turned off':
    cm.interact(input().lower())
