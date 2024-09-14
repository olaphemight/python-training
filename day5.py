#For Loop
#Exercise
"Calculate the average Students heught from the list of height"

# print("Welome To Average students Height calculator")
# students_height = input("Input a list of students height:\n").split()

# for n in range(0, len(students_height)):
#     students_height[n] = int(students_height[n])
# print(students_height)

# total_height = 0 
# for height in students_height:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in students_height:
#     number_of_students += 1
# print(number_of_students)


# average_height = total_height / number_of_students
# print(f'The average height of students is : {round(average_height)}')

# 180 124 165 173 189 169 146

# Using sum method
# total_height = sum(students_height)
# number_of_students = len(students_height)
# average_height = round(total_height / number_of_students)
# print(f'The average height of students is : {average_height}')

#Exercise 2
"Calculate the highest score from a list of scores"
# print("Welcome To High Score calculation")
# students_scores = input("Input a list of student scores:\n ").split()

# for score in range(0, len(students_scores)):
#     students_scores[score] = int(students_scores[score])
# print(students_scores)

# highest_score = 0
# for score in students_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# highest_score = max(students_scores)
# print(highest_score)

# Exercise 3
"Calculate the even numbers between 1 to 100"
# print("Calculate Even Numbers between 1 to 100")

# even_number = 0
# for numbers in range(2, 101, 2):
#     even_number += numbers
#     # print(numbers)
# print(f'The final even number addition is: {even_number}')

# Exercise 4
print("Automatically print Solution to fizzbuzz")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)
    

