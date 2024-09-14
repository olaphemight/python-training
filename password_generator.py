import random

letters = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
"O", "p", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "£", "#", "$", "%", "^", "&", "*", ")", "(", "_", "+", "-", "~", "?", "/",]

nr_letters = int(input("How many letters do you want?: "))
nr_numbers = int(input("How many numbers?: "))
nr_symbols = int(input("How many symbols?: "))

# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# # print(password)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(number)
# # print(password)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# print(password)

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
# print(password_list)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(number)
# print(password_list)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# print(password_list)

random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")






