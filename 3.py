# Первое значение - словарь
# Второе - список
my_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
my_list = ['Winter', 'Spring', 'Summer', 'Autumn']
user_month = int(input('Your month? (1-12): '))
if user_month == 1 or user_month == 2 or user_month == 3:
    print(my_dict.get(1))
    print(my_list[0])
elif user_month == 4 or user_month == 5 or user_month == 6:
    print(my_dict.get(2))
    print(my_list[1])
elif user_month == 7 or user_month == 8 or user_month == 9:
    print(my_dict.get(3))
    print(my_list[2])
elif user_month == 10 or user_month == 11 or user_month == 12:
    print(my_dict.get(4))
    print((my_list[3]))

