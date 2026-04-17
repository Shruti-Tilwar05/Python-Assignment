# # 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# import math

# class Circle:
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * math.pi * self.radius


# # Create object
# c = Circle(5)

# print("Area:", c.area())
# print("Perimeter:", c.perimeter())

# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
# from datetime import date

# class Person:
    
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob   # date of birth (YYYY, MM, DD)
    
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.dob.year
        
#         # adjust if birthday hasn't come yet this year
#         if (today.month, today.day) < (self.dob.month, self.dob.day):
#             age -= 1
        
#         return age


# # Create object
# p1 = Person("Shruti", "India", date(2001, 8, 3))

# print("Name:", p1.name)
# print("Country:", p1.country)
# print("Age:", p1.calculate_age())

# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# class Calculator:

#     def __init__(self):
#         self.result = 0

#     def add(self, x, y):
#         self.result = x + y
#         return self.result

#     def subtract(self, x, y):
#         self.result = x - y
#         return self.result

#     def multiply(self, x, y):
#         self.result = x * y
#         return self.result

#     def divide(self, x, y):
#         if y == 0:
#             raise ValueError("Denominator cannot be zero.")
#         self.result = x / y
#         return self.result

# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
# import math

# class Shape:
#     def area(self):
#         pass
    
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2
    
#     def perimeter(self):
#         return 4 * self.side

# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def perimeter(self):
#         return self.a + self.b + self.c
    
#     def area(self):
#         # Heron's formula
#         s = self.perimeter() / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# # Create objects
# c = Circle(5)
# s = Square(4)
# t = Triangle(3, 4, 5)

# print("Circle Area:", c.area())
# print("Circle Perimeter:", c.perimeter())

# print("Square Area:", s.area())
# print("Square Perimeter:", s.perimeter())

# print("Triangle Area:", t.area())
# print("Triangle Perimeter:", t.perimeter())

# 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
