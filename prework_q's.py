#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    '''Print statement'''
    print(f"Hello {user_name.upper()}, you got this in the bag! :)")

user_name = input("Please type your USERNAME ")
hello_name(user_name)
hello_name('USERNAME')


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

#Create a function with a no parameters. 
def first_odds():
    """Print odd numbers from 1-100"""
    start = -1
    while True:
         #Print odd numbers from start untill 100
        if start < 99: 
            start += 2
            print(start)
        else:
        # break loop after 99
            break

first_odds()

#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list.  

#Create a function with a parameter whose argument will be a list.
def max_num_in_list(numbers_list):
    """Print sorted list"""
    #Sort in ascending order. 
    numbers_list.sort()
    #Print last number on the list.
    print(numbers_list[-1])
    
numbers_list = [1,2,3,4,11,6,7,8,10]
max_num_in_list(numbers_list)

numbers_list = [22,44,67,33,99,2,5]
max_num_in_list(numbers_list)

#Question 4:
#Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

#Create a function with a parameter whose argument will be an integer recived by input. 
def get_leap_year(leap_year):
    #Use modulo operator to see if the year is divisible by 400, 100, and 4, using an if statement.
    #If it has a remainder it will be false. 
    """Print true if no remainder. Print false if remainder"""
    if leap_year % 400 == 0:
        print(bool(1))  
    elif leap_year % 100 == 0:
        print(bool(1))
    elif leap_year % 4 == 0:
        print(bool(1))  
    else:
        print(bool(0))

#Use the input function to ask for a date and convert it to an integer. 
leap_year = input("Please input leap year here: ")
leap_year = int(leap_year)
get_leap_year(leap_year)

#Queston 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.
 
#Create a function with a parameter whose argument will be a list. 
def check_numbers_numbers(numbers):
    """check if list is consecuitve order"""
    #Find the length of the list and set it to a new variable. 
    length_numbers= len(numbers)
    #Use a for loop with range function to loop through the list now that you have the length.
    #Make sure to subtract the list length by one since range starts at 0.
    for i in range(length_numbers - 1):
        #Add 1 to value of the number being pulled. Subtract that from same value being pulled. 
        #If it does not == 1 it’s False.
        if numbers[i + 1] - numbers[i] != 1:
            print("False")
        #If it == 1 its True.
        else:
            print("True")


numbers1 = [1,2,3,4,5,6]
numbers2 = [2,4,6,8,10]
check_numbers_numbers(numbers1)
check_numbers_numbers(numbers2)