import random


def simple_arithmetic_operation(operator, a, b):
    while True:
        try:
            user_input = int(input("> "))
            break
        except ValueError:
            print("Wrong format! Try again.")

    if operator == '+':
        result = a + b
        x = answer(user_input, result)

    elif operator == '-':
        result = a - b
        x = answer(user_input, result)

    else:
        result = a * b
        x = answer(user_input, result)

    return x


def answer(user_response, response):
    if user_response == response:
        print("Right!")
        x = 1

    else:
        print("Wrong!")
        x = 0
    return x


def simple_arithmetic_test():
    n = 0
    i = 0
    while i < 5:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        print(num1, operation, num2)
        n = n + simple_arithmetic_operation(operation, num1, num2)
        i += 1

    return n


def integral_squares():
    i = 0
    n = 0
    while i < 5:
        num = random.randint(11, 29)
        print(num)
        while True:
            try:
                user_input = int(input("> "))
                break
            except ValueError:
                print("Wrong format! Try again.")

        result = num * num
        n = n + answer(user_input, result)
        i += 1
    return n


print("Which level do you want? Enter a number:")
print("1 - simple operations with numbers 2-9\n" + "2 - integral squares of 11-29")
n = 0
level = 0
while True:
    try:
        level = int(input("> "))
    except ValueError:
        print("Incorrect format.")
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9\n" + "2 - integral squares of 11-29")
        continue

    if level == 1:
        n = simple_arithmetic_test()
        break
    elif level == 2:
        n = integral_squares()
        break
    else:
        print("Incorrect format.")
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9\n" + "2 - integral squares of 11-29")

while True:
    print(f"Your mark is {n}/5. Would you like to save the result? Enter yes or no.")
    user_input = input("> ")
    if user_input == "yes":
        print("What is your name?")
        name = input()
        file = open("results.txt", "a")
        file.write(f"{name}: {n}/5 in level {level}\n")
        print("The results are saved in 'results.txt'.")
        break

    elif user_input == "no":
        break
