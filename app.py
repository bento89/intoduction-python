




# # ---------PACKAGE ---------------
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
#

# from ecommerce import  shipping
# shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()
# calc_shipping()

# # ---------MODULE ---------------
# import utils
# from utils import find_max
#
# numbers = [2, 5, 1, 6, 8, 3]
# print(find_max(numbers))


# # ---------INHERITANCE ---------------
# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     pass
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1 = Dog()
# dog1.walk()



# # ---------CONSTRUCTOR ---------------
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point = Point(10, 20)
# point.x = 30
# print(point.x)


# # ---------CLASS ---------------
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point1 = Point()
# point1.draw()


# ---------EXCEPTION ---------------
# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:
#     print(f"Invalid Value")


# ---------RETURN PARAMETERS ---------------
# def square(number):
#     return number * number
#
# print(square(3))


# ---------PARAMETERS ---------------
# def greet_user(fname, lname):
#     print(f'Hi {fname} {lname}!')
#     print("Welcome aboard")
#
# greet_user("Bento", "Dias")
# greet_user(lname="Fuas", fname="Bento") # keyword argument
# greet_user("Bento", lname="Carvalho") # position argument

# ---------FUNCTION ---------------
# def greet_user():
#     print('Hi there!')
#     print("Welcome aboard")
#
#
# greet_user()


# ---------DICTIONARIES ---------------
# customer ={
#     "name": "Bento Dias",
#     "age": "32",
#     "phone": "6456456",
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("age"))

# phone = input("Phone: ")
# digits_maping ={
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output=""
# for ch in phone:
#     output += digits_maping.get(ch, "!")
# print(output)


# ---------UNPACKING ---------------
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x, y, z)


# ---------TUPLES ---------------
# numbers = (1, 2, 3, 4)
# print(numbers[0])


# ---------List Method ---------------
# numbers = [4,3, 2,7,3,6]
# numbers.append(12)
# numbers.insert(0, 10)
# # numbers.remove(3)
# print(2 in numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print("-"*10)
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)



# ---------2 Dimension list ---------------
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)





# ---------LIST ---------------
# name = ['John', 'Marry', 'Bob']
# print(name[:-1])
#
# numbers = [3, 2, 5, 3, 6, 7, 1]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# # # ---------NESTED FOR LOOPS ---------------
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# # # --------- FOR LOOPS ---------------
# for item in ['Bento', 'Dias']:
#     print(item)
#
# for i in range(5, 10):
#     print(i)
#
#
# for i in range(5, 10, 2):
#     print(i)
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# # ---------WHILE LOOPS ---------------
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print("Done")



# # ---------WEIGHT CONVERTER ---------------
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")


# # ---------COMPARISON OPERATOR ---------------
# name = "Bento dias"
#
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# temperature = 30

# if temperature >= 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")





#  -------- LOGICAL OPERATOR ---------------
# has_high_income = True
# has_good_credit = False
# has_criminal_record = False
#
# # if has_high_income or has_high_income:
# #     print("Eligible for loan")
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")


# AND: both
# OR: at least one
# NOT


# -------- IF STATEMENT ---------------
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Drink plenty of water")
# else:
#     print("It's lovely day")
#
# print("Enjoy your day")



# ----------- FUNCTION MATH ------------------
# import  math
# print(math.ceil(2.5))

# x = 2.9
# print(round(x))
# print(abs(-2.8))



# ----------- OPERATOR PRECEDENCE ------------------
# x = 10 + 3 * 2 ** 2
# y = (2 + 3) * 10 + 3
# print(x)
# print(y)



# ----------- ARITHMETICS OPERATIONS ------------------
# print(10 * 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
#
# x = 10
# print(x + 2)
# x += 3
# print(x)
# y = 2
# y -= 3
# print(y)



# ---------- STRING METHOD ---------------------
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('P'))
# print(course.replace('Beginners', 'Absolute beginners'))
# print('Python' in course)
# print(course.title())


# ---------FORMAT STRING --------------------
# first = 'Bento'
# last = 'Fuas'
#
# message = first + ' [' +last+'] is programmer!'
# msg = f'{first} [{last}] is a developer'
# print(message)
# print(msg)



# -------INDEX =---------------
# course = 'Python for beginners '
# print(course[-2])
# print(course[0:3])
# print(course[0:])
# another = course[:]
# print(another)
# name = 'Bento Dias'
# print(name[1:-1])


# --------------QUOTES --------------------
# text1 = 'This is single "quote" '
# text2 = "This is double 'quote'"
# text3 = '''
#     This is
#     multi line
#     in python
#
# '''
# print(text1)
# print(text2)
# print(text3)


# --------------INPUT --------------------
# birth_year = input("Birth Year: ")
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(age)


# ----------Getting Input ---------------------
# name = input('What is your name? ')
# color = input("Favorite color? ")
# print("Hi "+name+", you like "+ color)


# ------Variables ----------------------
# price = 10
# rating = 4.8
# name = "Bento Dias"
# is_published = True
# print(price)


# ----------------Hello World----------------------------------
# print('Hello world')
# print('o----')
# print('||||')
# print('*' * 10)

# https://www.youtube.com/watch?v=_uQrJ0TkZlc