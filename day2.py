# #Understanding Data Types
# # Data types, Numbers, Type conversion, f-string

# #Data types
# #string, integer, float, boolean 

# name = "Hello"
# number_str = "12345" + "1234"
# print(name[0])
# print(number_str)

# # integer 
# number = 123 + 34
# print(number)
# print(int(number_str))

# num_char = len(input("what is your name: "))

# print(type(num_char))

# #type conversion
# new_num_char = str(num_char)
# print(type(new_num_char))

# print("Your name has " + new_num_char + " characters.")

# age = 20
# print(age + float("30"))

# # Exercise 1
# "type a two digit number and add them togetherto give one digit"

# two_digit_number = input("Type two digit number: ")
# print(type(two_digit_number))

# first_digit =int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print(type(first_digit), type(second_digit)) 
# print(first_digit + second_digit )

#Exercise 2
"BMI Calculator"

# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# BMI = int(weight) / float(height) ** 2
# print(type(BMI), BMI)
#  print(int(BMI))

# Exercise
# if the maximum year to live is 90 year, calculate 
# your age, years, months, weeks remaining to live on earth

# current_year = int(input("Current year: "))
# birth_year = int(input("Birth year: "))
# age = current_year - birth_year
# print(age)
# year = 90
# year_remaining = 90 - age
# days_remaining = year_remaining * 365
# weeks_remaining = year_remaining * 52
# months_remaing = year_remaining * 12

# message = f'your have {year_remaining}years, {months_remaing}months, {weeks_remaining}weeks, {days_remaining}days to live'
# print(message)


# Exercise 2
print("Welcome to Tip Calculator")
bills = float(input("What is the total bill : $"))
tip = int(input("How much tips would you like to give? 10, 12 or 15?: "))
people = int(input("How many people to split the bill: "))

total_tip = bills * (1 + tip / 100)
bill_per_person = total_tip / people


print(round(bill_per_person, 2))


