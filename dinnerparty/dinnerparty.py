import function as f

dictionary = {}
print("Enter the number of friends joining (including you): ")
while True:
    user_input_quantity = int(input())
    if user_input_quantity > 1:
        break
    else:
        print("Enter a number greater than one")

print("Enter the name of every friend (including you), each on a new line: ")
f.wefwef(dictionary, user_input_quantity)

print("Enter the total amount: ")
user_input_sum = int(input())

while True:
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    user_input_lucky = input()

    if user_input_lucky == "Yes":
        f.luckyYes(dictionary, user_input_quantity, user_input_sum)
        print("Vladislav is the lucky one!")
        break

    elif user_input_lucky == "No":
        f.luckyNo(dictionary, user_input_sum, user_input_quantity)
        print("No one is going to be lucky")
        break


print(dictionary)