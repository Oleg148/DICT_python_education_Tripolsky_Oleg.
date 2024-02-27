def add_matrix(a, b):
    sum_matrix = []
    for i in range(len(a)):
        res = []
        for j in range(len(a[1])):
            res.append(a[i][j] + b[i][j])

        sum_matrix.append(res)
    return sum_matrix


def multiply_matrix_constant(a, c):
    for i in range(len(a)):
        for j in range(len(a[1])):
            a[i][j] = a[i][j] * c

    return a


def multiply_matrices(a, b):
    if len(a[1]) != len(b):
        raise IndexError

    m_matrices = []
    for i in range(len(a)):
        matrices = []
        for j in range(len(b[1])):
            summ = 0
            for n in range(len(a[1])):
                multiply = a[i][n] * b[n][j]
                summ = summ + multiply

            matrices.append(summ)
        m_matrices.append(matrices)
    return m_matrices


def side_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix) - i - 1):
            matrix[j][i], matrix[len(matrix) - i - 1][len(matrix) - j - 1] = (
                matrix[len(matrix) - i - 1][len(matrix) - j - 1], matrix[j][i])

    return matrix


def main_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def vertical_line(matrix):
    return [matrix[i][::-1] for i in range(len(matrix))]


def horizontal_line(matrix):
    return matrix[::-1]


def determinative_matrix2(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def determinative_matrix3(matrix):
    matrix = matrix + matrix[:2]
    res1 = []
    res2 = []
    for i in range(len(matrix[1])):
        plus = 1
        minus = 1
        for j in range(len(matrix[1])):
            plus = plus * matrix[j + i][j]
            minus = minus * matrix[j + i][len(matrix[1]) - j - 1]

        res1.append(plus)
        res2.append(minus)

    return sum(res1) - sum(res2)


def inverse_matrix3(matrix):
    res2 = []
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            for i in range(len(matrix)):
                if i == b:
                    continue
                res1 = []
                for j in range(len(matrix)):
                    if j == a:
                        continue

                    res1.append(matrix[i][j])

                res2.append(res1)

    res3 = []
    z = 0
    for i in range(0, len(res2), 2):
        z = -1 if z == 1 else 1
        res3.append(round(determinative_matrix2(res2[i: i + 2]) / determinative_matrix3(matrix) * z, 2))

    return [res3[i:i + 3] for i in range(0, len(res3), 3)]


def print_matrix(matrix):
    print("The result is:")
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            print(matrix[i][j], end=' ')

        print()
    print()


def enter_matrix():
    line, column = map(int, input("Enter matrix size: ").split())
    print("Enter matrix: ")
    return [[*map(int, input().split())][:column] for _ in range(line)]


def matrix_calculator():
    while True:
        try:
            print("1. Add matrices\n"
                  "2. Multiply matrix by a constant\n"
                  "3. Multiply matrices\n"
                  "4. Transpose matrix\n"
                  "5. Calculate a determinant\n"
                  "6. Inverse matrix\n"
                  "0. Exit")

            user_input = int(input("Your choice: "))

            if user_input == 1:
                matrix1 = enter_matrix()
                matrix2 = enter_matrix()
                print_matrix(add_matrix(matrix1, matrix2))

            elif user_input == 2:
                matrix1 = enter_matrix()
                constant = int(input("Enter constant: "))
                print_matrix(multiply_matrix_constant(matrix1, constant))

            elif user_input == 3:
                matrix1 = enter_matrix()
                matrix2 = enter_matrix()
                print_matrix(multiply_matrices(matrix1, matrix2))

            elif user_input == 4:
                transpose_matrix_menu()

            elif user_input == 5:
                matrix1 = enter_matrix()
                print(determinative_matrix3(matrix1), end="\n\n")

            elif user_input == 6:
                matrix1 = enter_matrix()
                print_matrix(inverse_matrix3(matrix1))

            elif user_input == 0:
                break

            else:
                print("Enter a number from 0 to 6")

        except ValueError:
            print("Invalid input")
            print()

        except IndexError:
            print("Wrong matrix size")
            print()


def transpose_matrix_menu():
    print("1. Main diagonal\n"
          "2. Side diagonal\n"
          "3. Vertical line\n"
          "4. Horizontal line")

    num = int(input("Your choice: "))

    if num == 1:
        matrix1 = enter_matrix()
        print_matrix(main_diagonal(matrix1))

    elif num == 2:
        matrix1 = enter_matrix()
        print_matrix(side_diagonal(matrix1))

    elif num == 3:
        matrix1 = enter_matrix()
        print_matrix(vertical_line(matrix1))

    elif num == 4:
        matrix1 = enter_matrix()
        print_matrix(horizontal_line(matrix1))

    else:
        print("enter a number from 1 to 4")
        print()


matrix_calculator()