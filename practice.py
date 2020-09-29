# def format_name(first_name, last_name):
#   if first_name and last_name:
#     string = last_name + ", " + first_name
#   # elif first_name == "" and last_name == True
#   #   string = last_name
#   # elif first_name and last_name == ""
#   #   string = first_name
#   # else
#   #   string = ""
  
#   return string 

# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"

# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"

# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"

# print(format_name("", ""))
# # Should return an empty string
#***********************************************
# 9/28/20
#Recursion Practice Quiz 

# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     return False
#     # If number is equal to 1, it's a power (base**0).
#   if number == 1:
#     return True
#   # Recursive case: keep dividing number by base.
#   return is_power_of(number / base, base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False


# Question 3

# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.

# def is_power_of(number, base):
#   print(number, base)
#   # Base case: when number is smaller than base.
#   if number == 1:
#     return True
#   if number < base:
#     return False
#     # If number is equal to 1, it's a power (base**0).
#   # Recursive case: keep dividing number by base.
#   return is_power_of(number / base, base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

# 4.
# Question 4

# The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?

# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     count += 1
#     if is_group(member):
#       count += count_users(member)
#   return count

# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18


#5. Question 5

# Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

# def sum_positive_numbers(n):
#   sum = n
#   if n < 1:
#     return 0
#   return sum + sum_positive_numbers(n - 1)

# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# Assessment
# 8.
# for x in range(1, 10, 3):
#     print(x)

# 9.
# for x in range(10):
#     for y in range(x):
#         print(y)


# x = "banana"

# # x = txt.strip()

# print("of all fruits", x, "is my favorite")

# def even_numbers(maximum):
#   return_string = ""
#   for x in range(2, maximum+1, 2):
#     return_string += str(x) + " "
#   return return_string.strip()

# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10)) # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed

# 9/29/20 Practice -
from collections import Counter
lst = [1, 2, 2, 3, 3, 3]
print(Counter(lst))