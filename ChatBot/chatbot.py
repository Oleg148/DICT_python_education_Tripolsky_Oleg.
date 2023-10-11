print("Hello! My name is DICT_Bot.")
print("I was created in 2023.")
print("Please, remind me your name.")
name = input()
print("What a great name you have, " + name)
print("Let me guess your age.\n"
      "Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
i = 0
while i < number:
    i = i + 1
    print(i, '!')

print("Let's test your programming knowledge.\n"
      "Why do we use methods?\n"
      "1. To repeat a statement multiple times.\n"
      "2. To decompose a program into several small subroutines.\n"
      "3. To determine the execution time of a program.\n"
      "4. To interrupt the execution of a program.")
while True:
    answer = int(input())
    if answer == 2:
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")

print("Congratulations, have a nice day!")
