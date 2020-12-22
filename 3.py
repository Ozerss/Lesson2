# Первое значение - словарь
# Второе - список
my_dict = {1: 'This is Winter(dict)', 2: 'This is Spring(dict)', 3: 'This is Summer(dict)', 4: 'This is Autumn(dict)'}
my_list = ['This is Winter(list)', 'This is Spring(list)', 'This is Summer(list)', 'This is Autumn(list)']
user_month = int(input('Your month? (1-12): '))
if user_month == 12 or user_month == 1 or user_month == 2:
    print(my_dict.get(1))
    print(my_list[0])
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(my_dict.get(2))
    print(my_list[1])
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(my_dict.get(3))
    print(my_list[2])
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(my_dict.get(4))
    print((my_list[3]))

