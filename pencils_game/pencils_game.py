import function as f

numberOfPencils = 0

while True:
    try:
        numberOfPencils = int(input("How many pencils: "))
    except ValueError:
        print("The number of pencils should be numeric")
        continue

    if numberOfPencils > 0:
        break

    elif numberOfPencils == 0:
        print("The number of pencils should be positive")

    else:
        print("The number of pencils should be numeric")


print("Who will be the first (John, Jack): ")
while True:
    name = input()
    if name == "Jack":
        break
    elif name == "John":
        break
    else:
        print("Choose between *John* and *Jack*")

computerName = "Jack" if name == "John" else "John"

while True:
    pencils = '|' * numberOfPencils

    print(pencils)
    print(f"{name}'s turn: ")

    if name != computerName:
        numberOfPencils = f.UserInput(name, numberOfPencils)

    else:
        numberOfPencils = f.computerInput(numberOfPencils)

    name = "Jack" if name == "John" else "John"

    if numberOfPencils == 0:
        print(f"{name} won!")
        break
