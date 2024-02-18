class Test:
    amountOfWater = 0
    amountOfMilk = 0
    numberOfCoffeeBeans = 0
    numberOfCups = 0
    amountOfMoney = 0
    water = 0
    milk = 0
    coffeeBeans = 0
    cost = 0

    def cappuccino(self):
        self.water = 200
        self.milk = 100
        self.coffeeBeans = 12
        self.cost = 6

    def latte(self):
        self.water = 350
        self.milk = 75
        self.coffeeBeans = 20
        self.cost = 7

    def espresso(self):
        self.water = 350
        self.milk = 75
        self.coffeeBeans = 20
        self.cost = 7

    def order(self):
        check = (self.amountOfWater - self.water >= 0, self.amountOfMilk - self.milk >= 0,
                 self.numberOfCoffeeBeans - self.coffeeBeans >= 0, self.numberOfCups - 1 >= 0)

        if all(check):
            self.amountOfWater = self.amountOfWater - self.water
            self.amountOfMilk = self.amountOfMilk - self.milk
            self.numberOfCoffeeBeans = self.numberOfCoffeeBeans - self.coffeeBeans
            self.numberOfCups = self.numberOfCups - 1
            self.amountOfMoney = self.amountOfMoney + self.cost
            print("Thank you for your purchase")

        else:
            print("no ingredients")

    def buy(self, numbers):
        """метод реалізує покупку кави"""
        if numbers == 1:
            self.espresso()
            self.order()

        elif numbers == 2:
            self.latte()
            self.order()

        elif numbers == 3:
            self.cappuccino()
            self.order()

        else:
            print("incorrect input")

    def fill(self, water, milk, coffeeBeans, cups):
        """метод реалізує додавання до кавоварки інгредієнтів"""
        self.amountOfWater = self.amountOfWater + water
        self.amountOfMilk = self.amountOfMilk + milk
        self.numberOfCoffeeBeans = self.numberOfCoffeeBeans + coffeeBeans
        self.numberOfCups = self.numberOfCups + cups

    def take(self):
        """метод реалізує зняття коштів із кавомашини"""

        self.amountOfMoney = 0

    def remaining(self):
        """метод реалізує виведення в консоль кількість інгідієнтів"""
        print("The coffee machine has:")
        print(self.amountOfWater, "of water")
        print(self.amountOfMilk, "of milk")
        print(self.numberOfCoffeeBeans, "of coffee beans")
        print(self.numberOfCups, "of disposable cups")
        print(self.amountOfMoney, "of money")

    def menu(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            userInput = input()
            if userInput == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                inputCoffee = int(input())
                self.buy(inputCoffee)

            elif userInput == "fill":
                print("Write how many ml of water you want to add:")
                water = int(input())
                print("Write how many ml of milk you want to add:")
                milk = int(input())
                print("Write how many grams of coffee beans you want to add:")
                coffeeBeans = int(input())
                print("Write how many disposable coffee cups you want to add:")
                cups = int(input())

                self.fill(water, milk, coffeeBeans, cups)

            elif userInput == "take":
                print(f"I gave you {self.amountOfMoney}")
                self.take()

            elif userInput == "remaining":
                self.remaining()

            elif userInput == "exit":
                break


ob1 = Test()
ob1.menu()
