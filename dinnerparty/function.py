import random as r


def wefwef(dictionary, user_input_quantity):
    i = 0

    while i < user_input_quantity:
        user_input_name = input()
        dictionary[user_input_name] = 0
        i += 1


def luckyYes(dictionary, user_input_quantity, user_input_sum):
    quantity = user_input_quantity - 1
    share = user_input_sum / quantity
    li = list(dictionary.keys())
    for key in li:
        dictionary[key] = round(share, 2)

    rand = r.randint(0, len(li) - 1)
    rand_key = li[rand]
    dictionary[rand_key] = 0


def luckyNo(dictionary, user_input_sum, user_input_quantity):
    share = user_input_sum / user_input_quantity
    li = list(dictionary.keys())
    for key in li:
        dictionary[key] = round(share, 2)
