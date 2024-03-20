import random


def rock_paper_scissors(choice, arr, points):
    while True:
        user_input = input("> ")

        option = random.choice(choice)

        if user_input == "!exit":
            print("Bye!")
            break

        elif user_input == "!rating":
            print(points)

        elif user_input in choice:
            if user_input == option:
                print(f"There is a draw ({option})")
                points = points + 50

            elif option in [arr[x] for x in range(arr.index(user_input) - 1, arr.index(user_input) - 8, -1)]:
                print(f"Well done. The computer chose {option} and failed")
                points = points + 100

            else:
                print(f"Sorry, but the computer chose {option}")

        else:
            print("Invalid input.")

    return points


file = open("rating.txt")
name = input("Enter your name: > ")
user_points = 0
print("Hello, " + name)
a = False
all_options = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree",
               "human", "snake", "scissors", "fire"]

index = 0
for line in file:
    if name == line.split()[0]:
        user_points = int(line.split()[1])
        a = True
        break
    index += 1

file.seek(0)
f = file.readlines()

while True:
    check = []
    player_choice = list(set(["rock", "paper", "scissors"] + input("> ").split(",")))
    if "" in player_choice:
        player_choice.remove("")

    for i in player_choice:
        check.append(i in all_options)

    if all(check):
        break

    print("Invalid input.")

print("Okay, let's start")

user_points = rock_paper_scissors(player_choice, all_options, user_points)

fileWriter = open("rating.txt", "w")

if not a:
    f.append(f"{name} {user_points}\n")
    fileWriter.write("".join(f))

else:
    f[index] = f"{name} {user_points}\n"
    fileWriter.write("".join(f))
