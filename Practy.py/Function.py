# 1. Write a Python function to find the maximum of three numbers.
# a = 5
# b = 10
# c = 15
# if a > b and a > c :
#     print(a)
# elif b > a and b > c:
#     print(b)
# else :
#     print(c)
#=========================
# 2. Write a Python function to sum all the numbers in a list.
# 	Sample List : (8, 2, 3, 0, 7)
# 	Expected Output : 20
# List = [8, 2, 3, 0, 7]
# total_sum = sum(List)
# print(total_sum)
#===========================================
# 3. Write a Python function to multiply all the numbers in a list.

# # 	Sample List : (8, 2, 3, -1, 7)
# # 	Expected Output : -336

# List = [8, 2, 3, -1, 7]
# product = 1
# for num in List :
#     product *= num
# print (product)

#======================
#  4. Write a Python function to reverse a string. 

# 	Sample String : "1234abcd"
# 	Expected Output : "dcba4321"

# Sample_String = "1234abcd"
# reversed_string = Sample_String[::-1]
# print (reversed_string)

#====================================
#5. Write a Python function to check whether a number falls within a given range.
# Sample function : check_range(5, 2, 7)      
# Expected Output : True

# check_range=(5, 2, 7) 
# def check_range(num, lower, upper):
#     return lower<= num<= upper 
# result = check_range(5,2,7)
# print(result)

#===========================================
 #6.Write a Python function that accepts a string and counts the number of upper and lower case letters.
	# Sample String : 'The quick Brow Fox'
	# Expected Output :
	# No. of Upper case characters : 3
	# No. of Lower case Characters : 12
# Sample_String = 'The quick Brow Fox'
# def count_case(s):
# 	upper = 0
# 	lower = 0
# 	for ch in s:
# 		if ch.isupper():
# 			upper += 1
# 		elif ch.islower():
# 			lower += 1
# 	print("No. of Upper case characters :", upper)
# 	print("No. of Lower case characters :", lower)

# count_case("The quick Brow Fox")
# ======
# Sample_String = 'The quick Brow Fox'


# def count_case(s):
#     upper = sum(1 for ch in s if ch.isupper())
#     lower = sum(1 for ch in s if ch.islower())

#     print("Upper:", upper)
#     print("Lower:", lower)

# ======================
# 7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# 	Sample List : [1,2,3,3,3,3,4,5]
# 	Unique List : [1, 2, 3, 4, 5]
# list = [1,2,3,3,3,3,4,5]
# def distinct_list(list):
# 	result = []
	
# 	for num in list:
# 		if num not in result:
# 			result.append(num)
# 	return result
# print (distinct_list(list))
# =============
# lst = [1,2,3,3,3,3,4,5]
# def distinct_list(lst):
# 	return list(set(lst))
# print (distinct_list(lst))
# =========================
# 8. Write a Python function that checks whether a passed string is a palindrome or not.

# 	Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# def is_palindrome(s):
# 	s=s.replace(" ","")					#remove space
# 	return s==s[::-1]
# print(is_palindrome("madam"))
# print (is_palindrome("nurses run"))

#9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically	
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

        




