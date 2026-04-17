# swap
# str1 = "chetan"
# str2 = "Shruti"
# print("str1 before: " + str1 + " ; " + "str2 before:"+ str2)
# temp = str1             #temp = chetan, str1 = chetan
# str1 = str2             #str1 = Shruti  ,str2 =shruti , temp = chetan
# str2 = temp             #str2 =chetan , temp = chetan str1 = shruti
# print ("str1 after:" + str1 + " ; " + "str2 after:" + str2)


# find the highest number among three numbers
# a = 5
# b = 10
# c = 15
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# list of numbers
# numbers = [8, 2, 3, 0, 7] calculate the sum of numbers in the list
# numbers = [8, 2, 3, 0, 7]
# total_sum = sum(numbers)
# print(total_sum)

# list of numbers
# numbers = [8, 2, 3, 0, 7] calculate the sum of numbers in the list by using loop
# numbers = [8, 2, 3, 0, 7]
# total_sum = 0
# for num in range(len(numbers)):          #num=0,1,2,3,4 
#     print(numbers[num])


# 4. Write a Python function to reverse a string. 

# 	Sample String : "1234abcd"
# 	Expected Output : "dcba4321"

#====================================================================
# Guessing game:

# import random

# randomNumber = random.randint(1, 100)
# userNumber = int(input("Enter your number: "))
# count=0
# attempt=1;
# while (attempt<5):
#     if userNumber == randomNumber:
#         print("You guessed the number: " , randomNumber , ". You Guessed the number in ", count)
#     if userNumber<randomNumber:
#         print("Guess higher...")
#         attempt+=1
#     else:
#         print("Guess Lower...")
#         attempt+=1
#     count+=1
#     userNumber=int(input("Enter your number again: "))
# print("You could not guess the number")

#====================================================================
#star patter;
# rows=int(input("Enter the no of lines: "))
# for i in range(1, rows+1):
#     for j in range(0, i):
#         print("*", end="")
#     print()

#====================================================================

# rows=int(input("Enter the no of lines: "))

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()

#====================================================================
# Find maximum of three numbers
# def find_max (a,b,c) :
#  return max (a,b,c)
# print (find_max(10,20,22))

# ====================
# Check even or odd

# num = int(input("Enter a number :"))

# if num %2 ==0 :
#  print ("Even")
# else :
#  print ("Odd")
#=================
# Reverse a string
# s = "python"
# print(s[::-1])
 #====================
# Check palindrome

# s = "madam"
# if s==s[::-1]:
#     print("Palindrome")
# else:
#     print ("Not palindrome")

#====================================
# Count vowels in string
# a= 10
# b = 5
# a,b = b,a
# print(a)
# print("a")

#=====================================
# arr = [12,4,20]
# print(max(arr))

# ============


# words = ["26","06","2020"]
# result = "-".join(words)
# print (result)

#=======================
# snum = int(input("Enter a number: "))
# fnum = int(input("Enter another number: "))
# add = sum([snum + fnum])
# print(add)
# ========================
# find the sum of digits in a 3 digit number entered by user

# num =int(input("Enter 3 digit number: "))
# a = num%10
# num = num //10
# b = num % 10
# num=num //10
# c= num %10
# num = num //10
# print (a + b + c)

# menu  driven calculator
# fnum =int(input("Enter first number: "))
# snum = int(input("Enter second number: "))
# op = input("enter the operation ")
# if op =='+':
#     print (fnum + snum)
# elif op == '-':
#     print (fnum - snum)
# elif op == '*':
#     print (fnum * snum)
# elif op == '/':
#     if snum != 0:
#         print (fnum / snum)
#     else:
#         print("Division not possible (cannot divide by zero)")
# table = int(input('Enter a number'))
# for i in range (1,11):
#     print (table, "X", i, "=", table*i)
# =====================
# Guessing Game
# Genrate random number
# import random
# SecretNumber = random.randint(1,10)
# # Take input from user
# Guess = int(input("Enter a guessing number between 1 & 10:"))
# # check condition
# if Guess==SecretNumber:
#     print("Congratulations! You guessed the number.")
# else :
#     print("Sorry! The correct number was", SecretNumber)


#=================================================
# List and set
# list1 = [1,1,2,3,4,5,5]
# names = ["Karan","Arjun","Bhima","Nakul"]
# print(list1)
# print(names);
# list1 = [1,1,2,3,4,5,5]
# result = [x*2 for x in list1]
# print(result)

# names = ["Karan","Arjun","Bhima","Nakul"]
# result = []
# for name in names :
#     result.append(name + "ji")
# print (result)

#==================================================

# list1 = [1,1,2,3,4,5,5]
# listConvertedToSet = set(list1)
# # setDemo = {1,1,2,3,4,5,5}
# # print(setDemo)
# print (list1)
# print(listConvertedToSet)

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = [7,8,9]
# result = set(list1 + list2 + list3)
# print(result)