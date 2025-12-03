# Inputs
fName = input("Please enter your First name: ")
lName = input("Please enter your Last name: ")
date_string = input("Please enter your date of birth (MM/DD/YYYY): ")

# Variables
date_list = date_string.split('/')
month = date_list[0]
day = date_list[1]
year = date_list[2]

fName = fName.capitalize()
lName = lName.capitalize()
total_chars = len(fName + lName)

# Month Checker
if month == '01':
    month_name = 'January'
elif month == '02':
    month_name = 'February'
elif month == '03':
    month_name = 'March'
elif month == '04':
    month_name = 'April'
elif month == '05':
    month_name = 'May'
elif month == '06':
    month_name = 'June'
elif month == '07':
    month_name = 'July'
elif month == '08':
    month_name = 'August'
elif month == '09':
    month_name = 'September'
elif month == '10':
    month_name = 'October'
elif month == '11':
    month_name = 'November'
elif month == '12':
    month_name = 'December'
else:
    month_name = 'Invalid month'

# Print

print(f"{fName} {lName}, there are {total_chars} characters in your name and your date of birth is {month_name} {int(day)}, {year}.")
