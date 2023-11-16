import function as f
import random as r

line = [' ', ' ', ' ']
array = [line[:], line[:], line[:]]
xo = "O"
i = 0

while True:
    if xo == "O":
        try:
            indexLine, indexColumn = map(int, input("Enter the coordinates: ").split())

        except ValueError:
            print("You should enter numbers!")
            continue
    else:
        indexColumn = r.randint(1, 3)
        indexLine = r.randint(1, 3)

    if indexColumn > 3 or indexLine > 3 or indexColumn < 1 or indexLine < 1:
        print("Coordinates should be from 1 to 3!")
        continue

    elif array[indexLine - 1][indexColumn - 1] != ' ' and xo == "X":
        continue

    elif array[indexLine - 1][indexColumn - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    xo = 'O' if xo == 'X' else 'X'

    if xo == "O":
        print(f"Enter the coordinates: {indexLine} {indexColumn}")

    array[indexLine - 1][indexColumn - 1] = xo
    f.print_array(array)
    i = i + 1

    if array[0][0] == array[0][1] and array[0][0] == array[0][2] and array[0][0] != ' ':
        print(xo, "wins")
        break

    elif array[1][0] == array[1][1] and array[1][0] == array[1][2] and array[1][0] != ' ':
        print(xo, "wins")
        break

    elif array[2][0] == array[2][1] and array[2][0] == array[2][2] and array[2][0] != ' ':
        print(xo, "wins")
        break

    elif array[0][0] == array[1][0] and array[0][0] == array[2][0] and array[0][0] != ' ':
        print(xo, "wins")
        break

    elif array[0][1] == array[1][1] and array[0][1] == array[2][1] and array[0][1] != ' ':
        print(xo, "wins")
        break

    elif array[0][2] == array[1][2] and array[0][2] == array[2][2] and array[0][2] != ' ':
        print(xo, "wins")
        break

    elif array[0][0] == array[1][1] and array[0][0] == array[2][2] and array[0][0] != ' ':
        print(xo, "wins")
        break

    elif array[0][2] == array[1][1] and array[0][2] == array[2][0] and array[0][2] != ' ':
        print(xo, "wins")
        break

    elif i > 8:
        print("draw")
        break
