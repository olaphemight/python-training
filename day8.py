# #Function
# "Simple Function"
# print("   Simple Function")
# def greet():
#     print("Good morning")
#     print("Good afternoon")
#     print("Good evening")

# greet()

# # Function that allows input
# print("   Function that allows input")
# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}')
#     print(f"Isn't the weather good today {name}")


# greet_with_name("Billie")

# "Positional Argument"
# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f"Isn't the weather good today in {location}")

# "Positional argment"
# greet_with("Angella", "London")

# "keyword argument"
# greet_with(location= "U.s", name="Steeve")


# Exercise
#Paint Area Calculator
"""You're painting a wall, the instruction says 
1 can od paint can cover 5 square meter, Given a random heigth
and width of the wall, calculate how many can of paint you need to buy
Number of can = (wall height x wall width)/ coverage per can"""

# import math
# wall_height = int(input("Height of wall: "))
# wall_width = int(input("Width of wall: "))
# coverage = 5
# def paint_cal(height, width, cover):
#     number_of_paint = (height * width) / cover
#     print(f"You'll need {math.ceil(number_of_paint)} cans of paint")


# paint_cal(height=wall_height, width=wall_width, cover=coverage)

# Exercise 2
"Write a programme to check if a numberis a prime number"

n = int(input("Check a number: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not prime number')
        


prime_checker(number=n)
