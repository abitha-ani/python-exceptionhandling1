'''Exception ''' #An exception in python is a type of error that occur during program excecution.
# unlike syntax error which prevent the code from running exception  occur when the code is syntactically 
# correct, but encounters an issue during execution
#exeption is an  unusual or unexpected event that occurs during program execution disrupting the normal flow of the program

'''exeption handling ''' #is a way to manage run time errors in python using the try except block, it prevents
# program from crashing when unexpected errors occur and allow developers to handle them carefully . without exeption handling an
#  error will stop the program execution

# age=int(input("enter a value"))
# print(age)

'''
# try-block = defines the blk of code that may raise an exception (we place try blk where is the chance to occur error)
# except = catches and handle exception that occur inside the try blk (where we handle error)
#finally = execute the code regardless of whether an exception occurs or not (execute if error occured or not)
#else = execute only if no exception occurs in the  try blk ((if no error)  '''


# try:
#     age=int(input("enter a age:"))
#     print(age)
# except:
#     print("invalid input: please enter a valid number")
# else:
#     print("age is",age)
# finally:
#     print("it always execute")
# print("hii")

#######################################

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# def div(x,y):
#     try:
#         z=x/y
#     except:
#         print("cant divided by zero")
#     else:
#         print("output is ",z)
#     finally:
#         print("always")
# div(a,b)

############################################
#in one try we can give multiple except

# try:
#     print(a)
# except NameError:
#     print("it is not defined")
# except:
#     print("it is not possible")

############################################
'''multiple except'''

# in python we can use multiple except to handle diff types of exception separately,
#  this helps in providing specific error msgs and handling erroprs more effectively

# try:
#     print(a)
#     print(10/0)
# except ZeroDivisionError:
#     print("cant divided by zero")
# except NameError:
#     print("it is not defined")
# except:
#     print("it is not possible")

################################################
# questions using try
######################################
# Exception handling
# 1. Write a program to read a file. Handle the exception if the file does not exist.

# 2. ⁠Write a program that takes an index from the user and prints the element from a predefined list. 
# Handle the case when the user enters an out-of-range index.


# elements = ['apple', 'banana', 'cherry', 'date', 'blueberry']

# try:
#     index = int(input("Enter an index: "))
#     print(f"Element at index {index}: {elements[index]}")
# except IndexError:
#     print("Error: Index is out of range.")
# except ValueError:
#     print("Error: Please enter a valid integer index.")

# 3. ⁠Write a program to get a value from a dictionary by asking the user for a key. Handle the case when the key does not exist.


# data = {
#     "name": "Abitha",
#     "age": 25,
#     "city": "Kochi",
#     "profession": "Developer"
# }

# key = input("Enter the key to search: ")

# try:
#     value = data[key]
#     print(f"Value for '{key}': {value}")
# except KeyError:
#     print(f"Error: The key '{key}' does not exist in the dictionary.")

# 4. ⁠Write a program to take two numbers from the user and divide them. Handle zero division, invalid input, and unexpected errors.

# try:
#     num1 = float(input("Enter the numerator: "))
#     num2 = float(input("Enter the denominator: "))
    
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Please enter valid numeric values.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# else:
#     print(f"Result: {num1} / {num2} = {result}")
