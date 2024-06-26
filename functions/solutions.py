# # Q.1 

# def square(number):
#     return number ** 2

# print(square(4))

# # Q.2

# def add(num1, num2): 
#     return num1 + num2

# print(add(2, 3))

# # Q.3

# def multiply(a, b):
#     return a * b

# print(multiply(2, 3))
# print(multiply(2, "Mitva"))

# # Q.4
# import math

# def circle_stats(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# a, c = circle_stats(5)

# print(round(a, 2), round(c, 2)) 

# # Q.5

# def greet(name = "User"):
#     return name + " Hello"

# print(greet())

# # Q.6

# cube = lambda x: x ** 3

# print(cube(3))
        
# # Q.7

# # name = "a"

# # if not name:
# #     print("Name not provided")
# # else: print("Provided")

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 4, 5))

# # Q.8

# def print_kwarg(**kwargs): 
#     for key, value in kwargs.items():
#         print(key, ":", value)
        
# print_kwarg(name="Naruto", power="kamehame", enemey= "Madara")

# Q.9

# learn yield again

# Q.10

def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)
    
print(factorial(5))