def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {'First name' : 'Marlon', 'Lastname': 'Marín'}

    super_list = [
        {'First name' : 'Martha', 'Lastname': 'Alvarez'},
        {'First name' : 'Marlon', 'Lastname': 'Marín'},
        {'First name' : 'Fernando', 'Lastname': 'Marín'},
        {'First name' : 'Jerónimo', 'Lastname': 'Marín'},
        {'First name' : 'Eliana', 'Lastname': 'Marín'},
    ] #list containing dictionaries
    

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'int_nums': [-2, -1, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items(): #look around dictionary
        print(key, ':', value)

    for i in super_list:
        for key, values in i.items(): #this code extracts each dict and same time extracts each of its values
            print(i, '-', values)

if __name__ == '__main__':
    run()