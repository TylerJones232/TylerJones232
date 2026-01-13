# Name: Tyler Jones
# Course: CS 1160 
# Assignment: Project 01 
# Filename: Project01.py 
# Brief Description: Validating Calendar Dates

date  = input('Enter date as month/day/year (e.g. 04/19/2022):') 
month = int(date[0:2])  # get month from string positions 0,1 
day   = int(date[3:5])  # get day from string positions 3,4 
year  = int(date[6:10]) # get year from string positions 6,7,8,9

is_valid_date = True

def leap_year(year):    # this is the function to calculate if the date entered is a leap year                                     
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_months (month, year):  # this function makes sure that if the month is 2 it checks for a leap year, and also makes sure each months has the days its supposed to have
    if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 0


if month <= 12 and month >= 1: # this function makes sure that they month entered is between 1 and 12
    is_valid_date = True
else:
    is_valid_date = False
    
    
max_days = get_days_in_months (month, year)  # this sets max to the previous function

if day < 1 or day > max_days: #This function makes sure the user enters the correct amount of days depending on the get_days_in_months function
    is_valid_date = False

    
if is_valid_date == True:     #this if statement prints if it is a valid date or not.
    print(f'{date} is a valid date.')
    
elif is_valid_date == False:  #this if statement prints if it is a valid date or not.
    print(f'{date} is not a valid date.')
    
if leap_year(year):       #this if statement prints if it is a leap year or not
    print(f'{year} is a leap year.')
else:                      #this if statement prints if it is a leap year or not
    print(f'{year} is not a leap year.')









   
    