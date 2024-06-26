# # Q.1

# age = int(input("Enter your age:"))
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")

# # Q.2
# import datetime

# today = datetime.date.today()
# day = today.strftime("%A")

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     price -= 2

# print("Price of ticket is ₹", price)

# # Q.3
# marks = int(input("enter your marks: "))

# if marks > 100:
#     print("invalid marks")
#     exit()

# if marks >= 90 and marks <=100:
#     grade = "A"
# elif marks <= 80:
#     grade = "B"
# elif marks <= 70:
#     grade = "C"
# elif marks <= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ", grade)

# # Q.4
# fruit = "banana"
# color = input("Fruit color: ")

# if fruit == "banana":
#     if color == "Green":
#         print("Unripe")
#     if color == "Yellow":
#         print("Ripe")
#     if color == "Brown":
#         print("Overripe")

# # Q.5

# weather = input("Enter the weather: ")

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"

# print(activity)

# # Q.6

# distance = int(input("Enter distance to be Covered(in Km): "))

# if distance < 3:
#     transport = "Walk"
# elif distance <= 15:
#     transport = "Bike"
# else: 
#     transport = "Car"

# print(transport)

# # Q.7

# order_size = "Small"
# extra = True

# if extra: 
#     coffee = order_size + " coffee with extra shot"

# print(coffee)

# # Q.8

# password = input("Enter your password: ")

# if len(password) < 6:
#     strength = "weak"
# elif len(password) < 10:
#     strength = "medium"
# else:
#     strength = "strong"

# print("password strength is", strength)

# # Q.9

# year = int(input("Enter year: "))

# if year%4 == 0 and year%100 != 0:
#     print(year, "is a leap year")
# elif year%100 == 0 and year%400 == 0:
#     print(year, "is a leap year")
# else: 
#     print(year, "is not a leap year")

# # Q.10

# animal = input("Animal: ").lower()
# age = int(input("Animals Age: "))

# if animal == "cat" :
#     if age < 5:
#         print("Junior cat food")
#     else:
#         print("Senior cat food")
# if animal == "dog" :
#     if age < 2:
#         print("Junior dog food")
#     else:
#         print("Senior dog food")
