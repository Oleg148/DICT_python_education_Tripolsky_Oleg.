import sys
import random as rand

print("HANGMAN")
while True:
    while True:
        play_exit = input("Type 'play' to play the game, 'exit' to quit: ")
        if play_exit == "exit":
            sys.exit()
        elif play_exit == "play":
            print("")
            break
        else:
            print("Enter the correct command")

    my_word = ('python', 'java', 'javascript', 'php')
    num = rand.randint(0, 3)
    word = my_word[num]
    answer = ''
    alphabet = []

    answer = answer.rjust(len(word), '-')

    attempt = 0

    while True:
        print(answer)
        user_input = input("Input a letter: ")
        letter_checking = len(user_input)
        check_register = user_input.isupper()

        repeated_letter = 0
        # цикл проверяет не вводил ли пользователь букву или нет
        for letter in alphabet:
            if user_input == letter:
                repeated_letter = 1

        alphabet.append(user_input)

        li = list(answer)
        i = 0
        error_checking = True
        # цикл отвечает за проверку сходства букв в слове с введенними пользователем и присваевает списку li правельные
        for letter in word:
            if letter == user_input:
                li[i] = user_input
                error_checking = False

            i = i + 1

        answer = ''.join(li)

        if answer == word:
            print(f"You guessed the word {word}\n" + "You survived!\n")
            break

        elif user_input == word:
            print(f"You guessed the word {word}\n" + "You survived!\n")
            break

        elif attempt == 8:
            print("You lost! \n")
            break

        elif letter_checking > 1 or letter_checking == 0:
            print("You should input a single letter.")

        elif check_register == 1:
            print("Please enter a lowercase English letter.")

        elif repeated_letter == 1:
            print("You've already guessed this letter")

        elif error_checking:
            print("That letter doesn't appear in the word")
            attempt += 1
