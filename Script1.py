input_string = input("Введите строки через пробел: ")
words = input_string.split()

new_arr = []
for word in words:
    if len(word) <= 3:
        new_arr.append(word)

print(" ".join(new_arr))