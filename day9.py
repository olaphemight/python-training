# # Dictionary

# programming_dictionary = {
#     "Bug": "An error in a programme that prevent the programme from running as expected",
#     "Function": "A piece of code that you can easily call over and over again"
   
# }

# # How To retrieve an item from dictionary,
# # Dictionaries are identified by there key
# print(programming_dictionary["Bug"])

# # Adding new entry in Dictionary
# programming_dictionary["loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# # It can be really helpful to start with an empty dictionary
# # How to create an empty dictionary
# empty_dictionary = {}

# # Looping through a Dictionary
# for key in programming_dictionary:
#     # print(key)
#     print(programming_dictionary[key])


# How To wipe a dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# Exercise
# Write aprogramme that convert the students score to grade
""" scores 91-100, Grade= 'outstanding' 
    scores 81-90, Grade= 'exceed expectation'
    scores 71-80, Grade = 'acceptable'
    score <= 70, Grade = 'fail """
# student_scores = {
#     "Harry":81,
#     "Rone": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# students_grade = {}

# for key in student_scores:
#     # print(student_scores[key])
#     if student_scores[key] > 90 and student_scores[key] <= 100:
#         students_grade[key] = "Outstanding"
#     elif student_scores[key] > 80 and student_scores[key] <= 90:
#         students_grade[key] = "Exceed Expectation"
#     elif student_scores[key] > 70 and student_scores[key] <= 80:
#         students_grade[key] = "Acceptable"
#     else:
#         students_grade[key] = "Fail"
# print(students_grade)


# # Nesting a dictionary

# nigeria = {
#     "south_west": {"states": ["Ondo", "Akure","Osun", "Oyo", "Edo", "Ogun", "Lagos"], "total": 7},
#     "south_east": {"states": ["Abia", "Anambra", "Enugun", "Imo", "Ebonyin"], "total": 5},
#     "south_south": {"states": ["Akwa-ibom", "Bayelsa", "Edo", "Rivers", "CrossRiver", "Delta"], "total": 4}

# }

# Nesting dictionary in a list

# Exercise
"Write a function to add new country to the list below"

travel_log = [
    {"country": "France",
    "visit": 12,
    "cities": ["Paris", "Lille", "Djion"]
    },

   {"country": "Germany",
    "visit": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visit, cities):
    travel_log.append({"country":country, "visit":visit, "cities":cities})


add_new_country("Russia", 2, ["Moscow", "Saint Peter'sburg"])

print(travel_log)


# Docstrings
"""Docstrings tells what a function will do
The Docstrings has to go the firstline after our declaration"""