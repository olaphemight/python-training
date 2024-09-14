"Random Number"
#Exercise
# Generate a random number between 0 and 1, to output Heads and Tails
# import random
# numbers = int(input("Create a random number?: "))
# random.seed(numbers)

# generate_number = random.randint(0, 1)

# if generate_number == 1:

#     print(generate_number)
#     print("Heads")
# else:
#     print(generate_number)
#     print("Tails")

#########################################
#########################################
#Exercise on List 
"Who is going to pay"
# namesAsCSV = input("Give me everybody's name: ")
# names = namesAsCSV.split(", ")

# print(names)
# person_to_pay = random.randint(0, len(names)-1)
# topay_name = names[person_to_pay]
# print(f'{topay_name} is going to pay')


############################
############################

#Exercise 3
"""write a programe which will mark a sport with an X,
Your programme should allow you to enter the the position
 of the treasure using two digit systen"""

row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

position = input("Where do you want to put the treasure?: ")

row = int(position[0])
col = int(position[1])

map[col - 1][row-1] = "X"

print(f' {row1}\n {row2}\n {row3}')