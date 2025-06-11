
# Raise

# raise Exceptiontype("custom error message")
# Exceptiontype - any builtin or custom Exception
# custom error message-optional-message Explaining the Error

# try:
#     age=int(input("enter your age:"))
#     if age<0:
#         raise ValueError("age cannot be negative")
#     else:
#         print("your age is",age)
# except ValueError as msg:
#     print(msg)

# try:
#     num=int(input("enter a no"))
#     if num==0:
#         raise ZeroDivisionError("u cannot divided by 0")
#     print("valid",num)
# except ZeroDivisionError as e:
#     print(e)

##################################################

#assert condition error message

# x=10
# assert x>5,"k is too small"
# print("assertion passed")


# try:
#     x=int(input("enter a no"))
#     assert x>5,"x is too small"
#     print("assertion passed")
# except AssertionError as msg:
#     print(msg)

###########################################################################################################################

# ######################  raise   ####################

# 1. Write a function safe_divide(a, b) that divides two numbers. If the denominator is zero, raise a ZeroDivisionError 
# with the message "Cannot divide by zero".

# def safe_divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return a / b
# try:
#     result = safe_divide(10, 0)
# except ZeroDivisionError as e:
#     print(e)



# 2. ⁠Write a function check_password(password) that raises a ValueError if the password is less than 6 characters.


# def check_password(password):
#     if len(password) < 6:
#         raise ValueError("Password must be at least 6 characters long.")
# try:
#     check_password("123")
# except ValueError as e:
#     print(e)  

# 3. ⁠Write a function validate_marks(marks) that raises a ValueError if marks are less than 0 or greater than 100.

# def validate_marks(marks):
#     if marks < 0 or marks > 100:
#         raise ValueError("Marks must be between 0 and 100.")
# try:
#     validate_marks(105)
# except ValueError as e:
#     print(e) 



# 4. ⁠Write a function withdraw(amount, balance) that raises a RuntimeError if the withdrawal amount is greater than the balance.

# def withdraw(amount, balance):
#     if amount > balance:
#         raise RuntimeError("Withdrawal amount exceeds available balance.")
#     else:
#         balance -= amount
#         print(f"Withdrawal successful. Remaining balance: ₹{balance}")
#     return balance

# try:
#     current_balance = 1000
#     current_balance = withdraw(1200, current_balance)
# except RuntimeError as e:
#     print(e)





#assertion

# 1. Write a function check_positive(num) that asserts the number must be greater than 0.

# def check_positive(num):
#     assert num > 0, "Number must be greater than 0."
# try:
#     check_positive(-5)
# except AssertionError as e:
#     print(e)  

# 2. ⁠validate_password(password) that asserts the password must be at least 6 characters long.

# def validate_password(password):
#     assert len(password) >= 6, "Password must be at least 6 characters long."
# try:
#     validate_password("123")
# except AssertionError as e:
#     print(e) 


# 3. ⁠Write a function validate_list(lst) that asserts the list must not be empty.

def validate_list(lst):
    assert len(lst) > 0, "List must not be empty."


try:
    validate_list([])  
except AssertionError as e:
    print(e)

try:
    validate_list([1, 2, 3])  
    print("List is valid.")
except AssertionError as e:
    print(e)


# 4. ⁠Write a function check_voting_eligibility(age) that asserts the person must be 18 or older.

# def check_voting_eligibility(age):
#     assert age >= 18, "Person must be at least 18 years old to vote."

# try:
#     check_voting_eligibility(16)
# except AssertionError as e:
#     print(e) 

# 5. ⁠Write a function validate_email(email) that asserts the email must contain '@'.

# def validate_email(email):
#     assert email, "Person must be at least 18 years old to vote."

# try:
#     check_voting_eligibility(16)
# except AssertionError as e:
#     print(e)

######################################################################

# #custom exceptiom
# in python you can create custom exception by defining a new class that inherit from exception
#  this allows u to create specific error msgs and handle exceptions in a structured way

# class CustomError(Exception):
#     pass
# raise CustomError("this is a custom error")

# class NegativeNumberError(Exception):
#     pass

# def check_positive(num):
#     if num<0:
#         raise NegativeNumberError("number cannot be negative")
#     else:
#         print("it is valid")

# try:
#     num=int(input("enter a positive number"))
#     check_positive(num)
# except NegativeNumberError as e:
#     print(e)

#########################################################


# class MarkTooLowError(Exception):
#     pass
# class MarkTooHighError(Exception):
#     pass

# def check_mark(marks):
#     if marks<0:
#         raise MarkTooLowError("mark cannot be negative")
#     elif marks>100:
#         raise MarkTooHighError("mark cannot be exceed 100")
#     else:
#         print(f"valid marks:{marks}")

# try:
#     marks=int(input("enter marks: "))
#     check_mark(marks)
# except MarkTooLowError as e:
#     print("error: ",e)
# except MarkTooHighError as e:
#     print("error: ",e)






# Custom Exception
# 1. Write a function validate_password(password) that raises a WeakPasswordError if the password length is less than 6.
# class WeakPasswordError(Exception):
#     def __init__(self, message="Password is too weak. It must be at least 6 characters long."):
#         self.message = message
#         super().__init__(self.message)

# def validate_password(password):
#     if len(password) < 6:
#         raise WeakPasswordError()
#     return "Password is strong enough."

# try:
#     validate_password("12345")
# except WeakPasswordError as e:
#     print(f"Error: {e}")

# 2. ⁠Write a function withdraw_money(balance, amount) that raises an InsufficientBalanceError if the amount is greater than the balance.

# class InsufficientBalanceError(Exception):
#     def __init__(self, message="Insufficient balance in the account"):
#         self.message = message
#         super().__init__(self.message)

# def withdraw_money(balance, amount):
#     if amount > balance:
#         raise InsufficientBalanceError(f"Withdrawal amount {amount} exceeds available balance {balance}")
#     balance -= amount
#     return balance

# try:
#     current_balance = 500
#     withdraw_amount = 600
#     new_balance = withdraw_money(current_balance, withdraw_amount)
#     print(f"Transaction successful! New balance: {new_balance}")
# except InsufficientBalanceError as e:
#     print(f"Error: {e}")


# 3. ⁠Write a function validate_salary(salary) that raises a LowSalaryError if the salary is below 10,000.

# class LowSalaryError(Exception):
#     def __init__(self, salary, message="Salary is too low! It must be at least 10,000."):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)

# def validate_salary(salary):
#     if salary < 10000:
#         raise LowSalaryError(salary)
#     return f"Salary {salary} is valid."

# try:
#     salary = int(input("Enter salary: "))
#     print(validate_salary(salary))
# except LowSalaryError as e:
#     print(f"Error: {e}")
