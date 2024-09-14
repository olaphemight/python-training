#Conditional Statements, Logical operators, code block and scope

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm: "))

# if height > 120:
#     print("Hurray!, you can ride the rollercoaster")
# else:
#     print("Sorry!, you have to grow taller before you can ride the rollercoaster")


#Exercise 1
#Check if the inputed number is even / odd

# number = int(input("What number do you wan to check?: "))
# even = number % 2 
# print(even)
# if even == 0 :
#     print("This is an even number ")
# else:
#     print("This number is an odd number")


# Exercise 2
# BMI 2.0

# height = float(input("What is your height in cm?: "))
# weight = int(input("What is your weight in kg?: "))
# BMI = round(weight / height ** 2, 1)

# if BMI < 18.5:
#     print(f'{BMI} you are Underweight')
# elif BMI <25:
#      print(f'{BMI} you have a normal weight')
# elif BMI < 30:
#     print(f'{BMI} you are Overweight')
# elif BMI < 35:
#     print(f'{BMI} you are Obese')
# else:
#     print(f'{BMI} you are clinically obese')

# Exercise 
# writea programme to check if a given year is a leap year or not
# rules for calculating a leap year
"A year is a leap year if: "
" a year is evenly divisible by 4, not evenly divisible by 100 but evenly divisible by 400"
" a year is evenly divisible by 4, not evenly divisible by 100 and not evenly divisible by 400"

# year = int(input("Which year do you want to check?: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print(f"{year}, is a leap year")
#         else:
#             print(f"{year}, is not a leap year")
#     else:
#             print(f"{year}, is a leap year")        
# else:
#     print(f"{year}, is not a leap year")


#Exercise
# print("Welcome To Python Pizza Deliveries")
# size = input("What size of pizza do you want? S M L?: ").upper()
# add_pepperoni = input("Do you want Pepperoni? Y / N: ").upper()
# extra_cheese = input("Do you want extra cheese? Y / N: ").upper()
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25


# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#         print("Pepperoni added")
#     else:
#         bill += 3
#         print("Pepperoni added")

# if extra_cheese == "Y":
#         bill += 1
#         # print(bill)
#         print("extra cheese added")
        
# print(f'your final bill for size {size} is:  {bill}')

#Exercise

print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* ''')


print("Welcome To Treasure Island ")
print("You are at main road road")

move = input("where do you want to go?:\n  ").lower()



if move == "right":
    print("wait for a taxi to pick you up")
    door = input("where do you want to seat?:\n ").lower()
    if door == "front":
        
        print("Seat confortably by the driver's side")
    else:
        print("make use of the back seat")

elif move == "left":
    print("Cross to the other side to board a vechicle going in your direction")
    print("wait for a taxi to pick you up")
    door = input("where do you want to seat?:\n ").lower()
    if door == "front":
        print("Seat confortably by the next to the driver")
    else:
        print("make use of the back seat")


elif move == "wait":
    print("Find somewhere secure to decide your direction")



# print("Go back to where you are coming from!")









