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

10/9/20 - A couple weeks ago, I had difficulty solving a problem with Javascript. After taking the Google Python course, I retried the problem and solved it in 15 minutes. I am going to keep going until I become a data scientist. 

10/11/20 - Using Python to Interact with the Operating System
Becoming a software engineer/data scientist day 14

10/13/20 - Learning python scripting
10/14/20 - Enrolled in Springboard, all the Python work I've done up to this point is already paying off
Success! I remember learning about rfind() to find the last occurrence of a character in a string. 

10/15/20 - started the Springboard prep-work and did another code warriors problem, still need to lookup how to do the matching parentheses problem from yesterday

for least_larger() I solidified my understanding of list comprehensions and enumerate a little more. Also, an empty list in python is falsy, and a list that contains values is truthy. Neither type of list is actually equal to True or False, but 1 and 0 are == to True and False. I also learned about lambda functions and how they take only 1 expression and are kind of like an anonymous function, a quick and dirty way to make a function without formally using def to define one

10/16/20 Becoming a software engineer/data scientist day 19
Copying lists: if x is a list, then y = x refers to the same list in memory and changing a value in either x or y affects the one list they both refer to. 
To truly copy the values of a list and make an entirely new list in memory, use y = list(x) or y = x[:]

Learned how to import packages and rename them:
from scipy.linalg import inv as my_inv

Learning about numpy which is pretty cool! Numpy subsetting is useful

10/19/20 - began reading "Introduction to Algorithms a Creative Approach" by Udi Manber learned about inductive proofs and how to show that the sum of n consecutive integers from 1 to n = (n)(n+1) / 2

Basically, we assume what were are trying to prove, the theorem is that s(n) = n(n+1) / 2 where s(n) is the sum of consecutive integers from 1 to n. 

We show the base case which is trivial where n = 1 is true. s(1) = 1 (2) / 2 = 1. 

Then we show that s(n+1) = (n+1)(n+2) / 2 which is the inductive step that makes it true for all integers from 1 to n. 

But if s(n) = n(n+1) / 2 then s(n+1) = n(n+1)/2 + n+1. 

For example, if s(4) = 1+2+3+4 = 10, then s(5) = s(4) + n+1 where n = 4 = 15, so s(5) = 15. 

so factoring above, n(n+1)/2 + 2(n+1)/2 = (n+1)(n+2)/2, which is exactly what we were trying to prove. I think that's the gist of it.  
started learning about basic plots with matplotlib

10/20/20 started reading about data structures

10/21/10 learning matplotlib and histograms. Learned about trees, heaps, and sorting lists. 

10/23/20 - preparing for Apple interview. Completed the Apple interview questions, cannot post here. 

10/24/20 - completed repeats function, last night of vacation

10/29/20 - making good progress. Haven't missed a day to upload to Git. Yesterday I learned about numpy, data frames, matplotlib, and Pandas modules. Really good stuff. 

Today I learned how to get Sublime working with Anaconda. I kept receiving ModuleNotFound error when I tried to import certain modules, even though I had installed them. The fix was to install the conda package in Sublime and then build with that, instead of building with pythonREPL. 

Then, I had to download another package (buildview) to make the build window appear on the side instead of on the bottom. 

I also learned I have to use ctrl+shift+p and search for conda then activate my testenv directory for Python.

I installed buildview package then restarted Sublime the reactived my testenv and now my output is displaying on the right side of the screen and in only 1 tab instead of creating a new tab every single time, which is what REPL build was doing. So I killed two birds with one stone! 

Started using Anaconda Navigator. Need to see why PyCharms isn't showing up in it. Done. Had to reinstall PyCharms in the default directory and reopen Anaconda Nav. 

Also started refactoring my trading programs with python, and it's way easier than using Javascript to use APIs and perform calculations. 

#
Experimenting with Jupyter Notebooks

##
10/29/20

*Let's see if this works

Learned that you can use ! for bash commands or 
!pip list or %lsmagic

you can use %matplotlib inline 

I can start experimenting / practicing with Jupyter notebooks instead of in my editor

import numpy as np
import matplotlib.pyplot as plt

n = 50 
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = np.pi * (15*np.random.rand(n))**2

plt.scatter(x,y,s=area,c=colors,alpha=.5)
plt.show()



Wow the Jupyter notebooks are way versatile. 

10/30/20 Halloween today. My fav holiday. Working on codewars and Springboard classes
