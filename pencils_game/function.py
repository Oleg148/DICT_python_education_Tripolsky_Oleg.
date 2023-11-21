import random as r


def UserInput(UserName, numberOfPencils):
    while True:
        try:
            inputPencils = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue

        if not 0 < inputPencils < 4:
            print("Possible values: '1', '2' or '3'")
            continue

        numberOfPencils = numberOfPencils - inputPencils

        if numberOfPencils < 0:
            numberOfPencils = numberOfPencils + inputPencils
            print("Too many pencils were taken")
            print(f"{UserName}'s turn: ")
        else:
            break

    return numberOfPencils


def computerInput(numberOfPencils):
    losingPosition = [x for x in range(5, 18, 4)]
    wonPosition1 = [x for x in range(4, 17, 4)]
    wonPosition2 = [x for x in range(3, 16, 4)]
    wonPosition3 = [x for x in range(2, 15, 4)]

    if numberOfPencils in losingPosition:
        rand = r.randint(1, 3)
        numberOfPencils = numberOfPencils - rand
        print(rand)

    elif numberOfPencils == 1:
        numberOfPencils = numberOfPencils - 1
        print(1)

    elif numberOfPencils in wonPosition1:
        numberOfPencils = numberOfPencils - 3
        print(3)

    elif numberOfPencils in wonPosition2:
        numberOfPencils = numberOfPencils - 2
        print(2)

    elif numberOfPencils in wonPosition3:
        numberOfPencils = numberOfPencils - 1
        print(1)

    else:
        rand = r.randint(1, 3)
        numberOfPencils = numberOfPencils - rand
        print(rand)

    return numberOfPencils
