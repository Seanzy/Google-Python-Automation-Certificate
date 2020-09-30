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
# from collections import Counter
# lst = [1, 2, 2, 3, 3, 3]
# print(Counter(lst))

# String Indexing
# word = "Apple"
# words = "  Lions and tigers and bears  "
# lst1 = ['word1', 'word2', 'word3', 'word4']
# print(word[:2]) #prints the left 2 letters
# print(word[2:]) #prints to the right of the left 2 letters
# print(word[2:5])#prints (5 - 2) letters to the right of the left 2 letters
# print(words.index("g"))
# print(words.index("bears"))
# print("tigers" in words)
# print(words.upper())
# print(words.lower())
# print(words.strip()) #removes tabs and newline chars
# print("lstrip", words.lstrip(), "end")  
# print("rstrip", words.rstrip(), "end") 
# print(words.count("tigers"))
# print(words.endswith("bears  "))
# print(("1234").isnumeric())
# print("-".join(lst1))
# print(','.join(words.split()))

# # Format method
# name = 'Joe'
# age = 55
# print("Hello {}, your age is {}".format(name, age))
# print("Hello {age}, your age is {name}".format(name=name, age=56))

# amount = 10.5
# with_tax = amount * 1.0925
# print("You owe ${:.2f} dollars".format(with_tax))
# print("You owe ${:>.2f} dollars".format(with_tax))


# def to_celsius(x):
#   return (x-32)*5/9

# for x in range(0, 101, 10): 
#   print("{:>1} F | {:>6.2f} C".format(x, to_celsius(x)))
# for x in range(0, 101, 10): 
#   print("{:>3} F | {:>1.2f} C".format(x, to_celsius(x)))
#   print("{:>3} F | {:>4.3f} C".format(x, to_celsius(x)))

# String operations

#     len(string) Returns the length of the string
#     for character in string Iterates over each character in the string
#     if substring in string Checks whether the substring is part of the string
#     string[i] Accesses the character at index i of the string, starting at zero
#     string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

# String methods

#     string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
#     string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
#     string.count(substring) Returns the number of times substring is present in the string
#     string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
#     string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
#     string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
#     string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
#     delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

# "{0} {1}".format(first, second)

# first = "apple"
# second = "banana"
# third = "carrot"

# formatted_string = "{0} {2} {1}".format(first, second, third)

# print(formatted_string[:0])

# Old string formatting (Optional)

# The format() method was introduced in Python 2.6. Before that, the % (modulo) operator could be used to get a similar result. While this method is no longer recommended for new code, you might come across it in someone else's code. This is what it looks like:

# "base string with %s placeholder" % variable

# The % (modulo) operator returns a copy of the string where the placeholders indicated by %  followed by a formatting expression are replaced by the variables after the operator.

# "base string with %d and %d placeholders" % (value1, value2)

# To replace more than one value, the values need to be written between parentheses. The formatting expression needs to match the value type.

# "%(var1) %(var2)" % {var1:value1, var2:value2}

# Variables can be replaced by name using a dictionary syntax (we’ll learn about dictionaries in an upcoming video).

# "Item: %s - Amount: %d - Price: %.2f" % (item, amount, price)

# The formatting expressions are mostly the same as those of the format() method. 

# Check out the official documentation for old string formatting.
# Formatted string literals (Optional)

# This feature was added in Python 3.6 and isn’t used a lot yet. Again, it's included here in case you run into it in the future, but it's not needed for this or any upcoming courses.

# A formatted string literal or f-string is a string that starts with 'f' or 'F' before the quotes. These strings might contain {} placeholders using expressions like the ones used for format method strings.

# The important difference with the format method is that it takes the value of the variables from the current context, instead of taking the values from parameters.

# Examples:

# >>> name = "Micah"

# >>> print(f'Hello {name}')

# Hello Micah

# >>> item = "Purple Cup"

# >>> amount = 5

# >>> price = amount * 3.25

# >>> print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')

# Item: Purple Cup - Amount: 5 - Price: 16.25

# Check out the official documentation for f-strings.

# word = "abdef"
# print(word[-1])

# def is_palindrome(input_string):
#   # We'll create two strings, to compare them
#   new_string = ""
#   reverse_string = ""
#   # Traverse through each letter of the input string
#   print(input_string.lower())
#   for letter in input_string.lower():
#     # Add any non-blank letters to the 
#     # end of one string, and to the front
#     # of the other string. 
#     if letter is not " ":
#       print(letter)
#       new_string += letter
#       reverse_string = letter + reverse_string
#   # Compare the strings
#   print(new_string)
#   print(reverse_string)
#   if new_string == reverse_string:
#     return True
#   return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

print("string1 string2 string3".rindex('string'))






