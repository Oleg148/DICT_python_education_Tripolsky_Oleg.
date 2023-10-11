import my_animals as a

print("I love animals! \n"
      "Let's check out the animals...\n"
      "The deer looks fine.\n"
      "The lion looks healthy.")

animals = {'1': a.camel(), '2': a.lion(), '3': a.deer(), '4': a.goose(), '5': a.bat(), '6': a.rabbit()}

while True:
    try:
        animals_input = input("Please enter the number of the habitat you would like to view: ")

        if animals_input == "exit":
            break

        else:
            print(animals[animals_input])

    except KeyError:
        print("please enter a number from 1 to 6 or 'exit' to exit")

print("See you later!")
