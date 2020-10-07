9/29/20 Practicing
Learned about using the Counter to get a mini histogram dictionary from a list. 
Worked on strings

9/30/20 - Today was really hot but I don't want to turn on my air conditioning because of the fires in California. My room will fill with smoke if I do, so I am studying in the heat. 

Tuples
Passing Practice Quiz: Lists
Passing Practice Quiz: Dictionaries

10/1/20
Object oriented programming
Classes


In addition to learning about classes, I learned you can use a tuple to swap or change var values without having to declare a new variable

I learned you can use comprehensions on dictionaries 

I learned about f-strings

10/2/20
Learned about constructors, __init__ and __str__, docstrings, help(), completed and passed my first Jupyter Notebook (Class Elevator) 
Week 5 was a good week. I learned to always initialize mutable attributes in the constructor. I learned when to initialize attributes in the constructor instead of in the class. We initialize attributes in the constructor when we want each instance of the class to have its own unique/independent attribute instead of all instances sharing a single attribute

Learned about modules and importance of pandas and numpy modules in finance

10/4/20
Writing a script from the ground up
Learned about sort() and sorted(), sort modifies the existing list it's called on, and sorted returns a new list 

Passing module 6

10/5/20 Almost done with Final Project
Learned about str.translate and str.maketrans

10/6/20
Learned an easy way to remove punctuation from a string:
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for letter in words:  
  if letter in punc:  
    words = words.replace(letter, "")

Key takeaways from this final project:
Why was it better to first remove all punctuation before splitting into words? Initially, I tried to split the given string into words, then lowered the words, then tried to remove punctuation from each word. But I faced some challenges, namely, the immutability of strings and space requirements of making new variables for each new word. Each word potentially has different punctuation in a different spot. It was way easier to remove all punctuation first using replace(). I didn't know I could simply reassign the string I am iterating through as I am doing the replacements, even though strings are immutable. I guess the builting python functions are pretty optimized. 
Also, removing punctuation before checking for uninteresting words was important because the uninteresting words lacked punctuation. They were also lowercase so it was better to remove punctuation and lower the original string, then split it up to find uninteresting words. It was best to plan all this and keep things simple, but have a deep understanding of how each function words. I immediately thought to use replace when removing punctuation, so I should have researched replace extensively if I could not immediately know how to use it to perform the replacement. Initially, because I was trying to replace the punctuation from each word rather than going one letter at a time, I faced challenges. 