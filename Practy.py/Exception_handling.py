# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
# try:
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
    

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
# try:
#     user_input = input("Enter an integer: ")
#     num = int(user_input)
#     print("You entered:", num)
# except ValueError:
#     print("Error: Invalid input! Please enter a valid integer.")

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# try:
#     file_name = input("Enter the file name to open: ")
#     with open(file_name, 'r') as file:
#         content = file.read()
#         print("File content:\n", content)
# except FileNotFoundError:
#     print("Error: File not found! Please check the file name and try again.")


# # 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
# try:
#     num1 = input("Enter the first number: ")
#     num2 = input("Enter the second number: ")
#     result = float(num1) + float(num2)
#     print("The sum is:", result)
# except ValueError:
#     print("Error: Invalid input! Please enter numerical values.")

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
# try:
#     file_name = input("Enter the file name to open: ")
#     with open(file_name, 'r') as file:
#         content = file.read()
#         print("File content:\n", content)
# except PermissionError:
#     print("Error: Permission denied! You do not have permission to access this file.")

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
# try:
#     my_list = [1, 2, 3, 4, 5]
#     index = int(input("Enter the index to access: "))
#     print("Element at index", index, "is:", my_list[index])
# except IndexError:
#     print("Error: Index out of range! Please enter a valid index between 0 and", len(my_list)-1)

# 7. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
# try:
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ArithmeticError:
#     print("Error: An arithmetic error occurred! Please check your inputs and try again.")


a=10
b=2

try:
    c = a/b
    str = None
    print("length of String: ", len(str))
    print("resourcce started...")
except ZeroDivisionError as e:
    print("Exception: " , e)
except TypeError as e:
    print("This is operation on None String error: " , e)
except Exception as e:
    print("General exception", e)
finally :
    print("resourse closed")
    
print("important code")




