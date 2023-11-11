def print_array(array):
    print("---------")
    for Line in array:
        x = ''
        for cell in Line:
            x = x + cell + ' '
        print('|', x + '|')
    print("---------")
