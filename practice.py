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

# print("string1 string2 string3".rindex('string'))

fruits = ['apple', 'pear', 'banana']
# fruits.append('kiwi')
# print(fruits)
# fruits.insert(2, 'plum')
# print(fruits)
# fruits.remove('plum')
# print(fruits)
# print(fruits.pop(3))
# print(fruits)

# newList = []
# i = 0
# for fruit in fruits:
#   if i % 2 == 0: 
#     newlist.append(fruit)
#     i += 1
# print(newList)


# def skip_elements(elements):
#   # Initialize variables
#   new_list = []
#   i = 0

#   # Iterate through the list
#   for el in elements:
#     # Does this element belong in the resulting list?
#     if i % 2 == 0:  
#       # Add this element to the resulting list
#       new_list.append(el)
#     # Increment i
#     i += 1

#   return new_list

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# 9/30/20
# Tuples are sequences of elements of any type that are immutable and are made by a comma. They are good when you don't want the data to be modified, or where each position has meaning, like (firstname, mid initial, last name). We use it to keep data together that has more than one value

# Using enumerate to copy above function
# def skip_elements(elements):
#   new_list = []

#   for i, el in enumerate(elements):
#     if i % 2 == 0:
#       new_list.append(el)

#   return new_list

# print(skip_elements(fruits))

# List comprehension "listcomps" is brackets with an expression followed by for or if statements
# lst2 = []
# for x in range(1,11):
#   lst2.append(x*7)

# print(lst2)

# multiples = [x*7 for x in range(1,11)]
# print(multiples)


# #################################
# Lists and Tuples Operations Cheat Sheet
# Lists and Tuples Operations Cheat Sheet

# Lists and tuples are both sequences, so they share a number of sequence operations. But, because lists are mutable, there are also a number of methods specific just to lists. This cheat sheet gives you a run down of the common operations first, and the list-specific operations second.
# Common sequence operations

#     len(sequence) Returns the length of the sequence
#     for element in sequence Iterates over each element in the sequence
#     if element in sequence Checks whether the element is part of the sequence
#     sequence[i] Accesses the element at index i of the sequence, starting at zero
#     sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
#     for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time

# Check out the official documentation for sequence operations.
# List-specific operations and methods

#     list[i] = x Replaces the element at index i with x
#     list.append(x) Inserts x at the end of the list
#     list.insert(i, x) Inserts x at index i
#     list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
#     list.remove(x) Removes the first occurrence of x in the list
#     list.sort() Sorts the items in the list
#     list.reverse() Reverses the order of items of the list
#     list.clear() Removes all the items of the list
#     list.copy() Creates a copy of the list
#     list.extend(other_list) Appends all the elements of other_list at the end of list

# Most of these methods come from the fact that lists are mutable sequences. For more info, see the official documentation for mutable sequences and the list specific documentation.
# List comprehension

#     [expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.

#     [expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true. 
#     ###################################

# rep = 'string1string2'

# print(rep.replace('string1','string2'))

# Practice Quiz: Lists
# 3.
# Question 3

# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. For example: 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format. 

# def octal_to_string(octal):
#   result = ""
#   value_letters = [(4,'r'), (2,'w'), (1,'x')]

#   for digit in [int(num) for num in str(octal)]:
#     for value, letter in value_letters:
#       print(value, letter)
#       if digit >= value: 
#         digit -= value
#         result += letter
#       else:
#         result += '-'
#   return result
# #   answer = [num for num in str(octal)]
# #   for digit in [num for num in str(octal)]:
# #     print(digit)
# #   print(answer)

# print(octal_to_string(755))
# print(octal_to_string(644))
# print(octal_to_string(640))

# files = {'jpg': 10, 'csv': 5, 'png': 25}
# print(files)
# print(files.keys())
# print(files.values())
# print(files.items())

# Use dictionaries when you plan on searching for a specific element
# for...in automatically goes through a dictionary's keys

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for item, colors in wardrobe.items():
#   # for color in wardrobe.items():
#     # print("{} {}".format(item))
#     print(item)
#     print(colors)

# output should be: 
# "red shirt"
# "blue shirt"
# "white shirt"
# "blue jeans"

# Dictionary Methods Cheat Sheet

# Definition

# x = {key1:value1, key2:value2}

# Operations

#     len(dictionary) - Returns the number of items in the dictionary
#     for key in dictionary - Iterates over each key in the dictionary
#     for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
#     if key in dictionary - Checks whether the key is in the dictionary
#     dictionary[key] - Accesses the item with key key of the dictionary
#     dictionary[key] = value - Sets the value associated with key
#     del dictionary[key] - Removes the item with key key from the dictionary

# Methods

#     dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
#     dict.keys() - Returns a sequence containing the keys in the dictionary
#     dict.values() - Returns a sequence containing the values in the dictionary
#     dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
#     dict.clear() - Removes all the items of the dictionary


# Question 2

# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

# def groups_per_user(group_dictionary):
#   user_groups = {}
#   # Go through group_dictionary
#   for group, users in group_dictionary.items():
#     # Now go through the users in the group
#     for user in users:
#       # Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary
#       if user not in user_groups:
#         user_groups[user] = []
#         user_groups[user].append(group)
#         print(user_groups)
#       # if user not in user_groups:
#       #   user_groups[user] = []
#       #   user_groups[user].append(group)
#       #   print(user_groups)
#       else:
#         user_groups[user].append(group)
#         print('else',user_groups)
#   return(user_groups)

# print(groups_per_user(
#   {"local":          ["admin", "userA"],
#    "public":         ["admin", "userB"],
#    "administrator":  ["admin"] }))


# 7.
# Question 7
# Refactor this using list comprehensions

# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. 

# def count_letters(text):
#   result = {}
#   text = text.lower()
#   # print(text);
#   # Go through each letter in the text
#   for letter in text:
#     # Check if the letter needs to be counted or not
#     if letter.isalpha():
#     # Add or increment the value in the dictionary
#       if letter not in result:
#         result[letter] = 1
#       else: 
#         result[letter] += 1
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# def highlight_word(sentence, word):
#   # return((' ').join([piece.upper() in sentence if piece == word]))
#   print([piece.upper() for piece in sentence.split() if piece == word])

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

# Module 4

# 2.
# Question 2

# The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line? 

# def highlight_word(sentence, word):
#   # return((' ').join([piece.upper() for piece in sentence if piece == word]))
#   print(sentence.split().index(word))

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


# 9.
# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")

# print(colors)


# 3.
# Question 3

# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

# def combine_lists(list1, list2):
#   # Generate a new list containing the elements of list2
#   list3 = list2
#   # Followed by the elements of list1 in reverse order
#   # list4 = [list3.append(el) for el in list1]
#   print(list(reversed(list1)))
#   print(list3 + list(reversed(list1)))
  
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))


# 6.Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

# def combine_guests(guests1, guests2):
#   result = {}
#   # Combine both dictionaries into one, with each key listed 
#   # only once, and the value from guests1 taking precedence
#   guests2.update(guests1)
#   # print(guests2)
#   return guests2
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

# print(combine_guests(Rorys_guests, Taylors_guests))



# Python code to merge dict using a single  
# expression 
# def Merge(dict1, dict2): 
#     res = {**dict1, **dict2} 
#     return res 
      
# # Driver code 
# dict1 = {'a': 10, 'b': 8} 
# dict2 = {'a': 6, 'c': 4} 
# dict3 = Merge(dict1, dict2) 
# print(dict3) 


# def Merge(dict1, dict2): 
#     return(dict1.update(dict2)) 
      
# # Driver code 
# dict1 = {'a': 10, 'b': 8} 
# dict2 = {'d': 6, 'c': 4} 
  
# # This return None 
# print(Merge(dict1, dict2)) 
  
# # changes made in dict2 
# print(dict1)
# print(dict2) 

# 9/30/30 Object Oriented Programming

# print(dir(""))
# print(dir(list))
# help(str)

# a = 1
# b = 2

# print(a,b)

# a,b = a+b, a+b
# print(a,b)

# dic1 = {'a':1, 'b':2}
# dic2 = {'c':3, 'd':4}

# heights = {'Sean': 75, 'Dad': 72, 'John': 68}
# tall = {name:inches for (name, inches) in heights.items() if inches >= 70}
# tall2 = {name for (name) in heights.items()}
# print(tall)
# print(tall2)

# heights = {'John': 175, 'Jane': 150, 'Jim': 155, 'Matt': 170}

# tall = {key:value for (key, value) in heights.items() if value >= 170}

# print(tall)

# name = 'Joe'
# age = 55

# print(f"Hi {name}, you are {age} years old")

# class Dog():
#   name = ''
#   age = 7

#   def bark(self):
#     print('woof woof my name is {}'.format(self.name))

# spot = Dog()
# spot.name = 'sean'
# spot.bark() 
# print(spot.name, spot.age)

# 10/2/20 Constructors and __init__

# class Apple:
#   """Creates an Apple instance with 2 params, color and flavor"""
#   def __init__(self, color, flavor):
#     self.color = color
#     self.flavor = flavor
#   def __str__(self):
#     return "I am a {} apple".format(self.color)

# gala = Apple('red', 'sweet')
# print(gala)

# print(gala.color, gala.flavor)

# help(Apple)

# Classes and Methods cheat sheat
# Classes and Instances

#     Classes define the behavior of all instances of a specific class.
#     Each variable of a specific class is an instance or object.
#     Objects can have attributes, which store information about the object.
#     You can make objects do work by calling their methods.
#     The first parameter of the methods (self) represents the current instance.
#     Methods are just like functions, but they can only be used through a class.

# Special methods

#     Special methods start and end with __.
#     Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.

# Documenting classes, methods and functions

#     You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:

# dog = 'dog'

# print('cat', dog)

# class Clothing:
#   material: ""
#   def __init__(self, name):
#     self.name = name
#   # def __str__(self):
#   #   return f"This {self.name} is made of {self.material}"
#   def checkmaterial(self):
#     print (f"This {self.name} is made of {self.material}")

# class Shirt(Clothing):
#   material = "cotton"

# polo = Shirt("Polo")

# print(polo.checkmaterial())

# class Clothing:
#   material = ""
#   def __init__(self,name):
#     self.name = name
#   def checkmaterial(self):
#     print("This {} is made of {}".format(self.name,self.material))
      
# class Shirt(Clothing):
#   material="Cotton"

# polo = Shirt("Polo")
# polo.checkmaterial()

# class Clothing:
#   stock={ 'name': [],'material' :[], 'amount':[]}
#   def __init__(self,name):
#     material = ""
#     self.name = name
#   def add_item(self, name, material, amount):
#     Clothing.stock['name'].append(self.name)
#     Clothing.stock['material'].append(self.material)
#     Clothing.stock['amount'].append(amount)
#   def Stock_by_Material(self, material):
#     count=0
#     n=0
#     for item in Clothing.stock['material']:
#       if item == material:
#         count += Clothing.stock['amount'][n]
#         print(Clothing.stock['amount'])
#         n+=1
#     return count

# class shirt(Clothing):
#   material="Cotton"
# class pants(Clothing):
#   material="Cotton"
  
# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)

# # Why do we need n=0 and n+=1? Ah, because the amounts are in a list format, so each time add_item() is called, the amount of that item is added to the list, and we use n to keep track of where 

import random
import datetime

print(random.randint(1,10))
now = datetime.datetime.now()

print(now)

help(datetime.datetime)

print(now + datetime.timedelta(28))