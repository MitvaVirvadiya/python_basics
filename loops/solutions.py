# # Q.1

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# count = 0

# for num in numbers:
#     if(num > 0):
#         count+=1

# print(count)

# # Q.2
# num = int(input("Enter n: "))

# sum_even = 0

# for i in range(1, num + 1):
#     if i % 2 == 0:
#         sum_even += i

# print(sum_even)

# # Q.3

# num = int(input("Enter n: "))

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(num, "X", i, "=", num * i)

# # Q.4 

# input_str = input("enter string: ")
# reverse_str = ""

# for char in input_str:
#     reverse_str = char + reverse_str 
    
# print(reverse_str)

# # Q.5

# input_str = input("enter string: ")

# for char in input_str: 
#     if input_str.count(char) == 1:
#         print(char)
#         break

# # Q.6

# input_num = int(input("Enter number: "))
# factorial_num = 1

# while input_num > 0:
#     factorial_num *= input_num
#     input_num-=1

# print(factorial_num)

# # Q.7

# while True:
#     num = int(input("Enter num; "))
#     if 1 <= num <= 10:
#         print("Valid input")
#         exit()
#     else:
#         print("Pls, enter valid input")

# # Q.8

# input_num = int(input("enter nul: "))

# is_prime = True

# if input_num > 1:
#     for i in range(2, input_num):
#         if input_num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")

# # Q.9

# items = ["apple", "banana", "orange", "apple", "mango"]

# unique_item_list = set()

# for item in items: 
#     if item in unique_item_list:
#         print("Duplicate: ", item)
#         break
#     unique_item_list.add(item)

# # Q.10
# import time

# wait_time = 1
# attempts = 0
# max_retries = 5

# while attempts < max_retries:
#     print("Attempt", attempts + 1, "- wait time", wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1
