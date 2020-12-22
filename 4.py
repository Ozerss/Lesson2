my_str = input("Напишите несколько слов, разделённых пробелом: ")
word = []
count = 1
for el in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f" {count}. {word [el]}")
        count += 1
    else:
        print(f" {count}. {word [el] [0:10]}")
        count += 1
