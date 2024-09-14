# Function with Output

# first_name = input("Firstname: ").title()
# last_name = input("Lastname: ").title()

# def format_name(f_name, l_name):
#     return f_name + " " + l_name

# fullname = format_name(f_name=first_name, l_name=last_name)
# print(fullname)


# def format_name(l_name, f_name):
#     formated_l_name = l_name.title()
#     formated_f_name = f_name.title()

#     print(f'{formated_l_name} {formated_f_name}')


# format_name("oLaYoRI", "oluwaFEmi")



# # Multiple Returns statement
# def format_name(l_name, f_name):
"""Takes the first and lastname, and format it to return the title case version of it """
   
#     if l_name == "" or f_name == "":
#         return
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f'Result: {formated_f_name} {formated_l_name}'

# fullname = format_name(input("What is your first name: "), input("what is your last name: "))
# print(fullname)

# Exercise 1
# Check if a year is a leap year and show the number of days in the month


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# leap_year(2024)
# leap_year(2021)
# leap_year(2020)
# leap_year(2000)
# leap_year(2001)


def days_in_months(year, month):
    """ takes in year and month as a parameter """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]




check_year = int(input("Enter year: "))
check_month = int(input("Enter month: "))


print(days_in_months(year=check_year, month=check_month))
# days_in_months()

# Print vs Return
"""when a return keyword is used, the output can ne used 
as an input somewhere else,
when print is used, it cant not be used as an input somewhere """