# Description

This is a collection of concepts that I have learned using Python.  These concepts are being used to increase my knowledge of the Python language which will make me a more complete programmer now and in the future.

## Classes 

I have included some practice using basic ways that we can use classes.  I was hoping to show how classes can be used to create objects and assign attributes to them.
I use the __init__() function that is usually necessary for classes to initiated.  The __init__() function is also what is needed to assign properties, and other operation necessary for the object we are making.


## Challenge classes

Entry Point
1.  use a isPalindrome function and call it in main()
2.  As a reminder: Declare a function called is_palindrome. Your function should take in a String
and return True/False depending on whether the given String is a palindrome. (Remember built-in
String methods)
3.  Instantiate two strings in the main() function and run the is_palindrome function.
Classes
1.  Create a Rectangle class with height and width fields
2.  Create getters & setters for the fields. Create a method get_area()
3.  Instantiate a rectangle in the main function and print its area
OOP
1.  Create a Vehicle parent class with fields and a method
2.  Create a Car child class with extra fields and override the parent method
3.  Instantiate both in the main function and call their methods

## Tuples

The files including Tuples are me using basic concepts of tuples.  Tuples can be used to store multiple items in a single variable,  I view them as very similar to arrays
but the difference is tuples can not be changed but do allow duplicate values.  It is sometimes necessary to use Tuples to access certain methods that might make the application
you are running work smoother.  

## Tuples Challenge

This challenege was me using tuples in a real world problem and how I decided to solve the problem.

Stationary Store
1.  You own a stationery store and you want an app to organise pens
2.  Create a namedtuple Pen class with attributes: size(int), inkcolour(string), and beveled(bool)
3.  Instantiate three different kinds of pens with different attributes
4.  Print your namedtuple class instances in the following format Standard Pen: size = 2, ink = "black",
isbeveled = True
Slope of a Line
1.  You have the following two points: (2,1), (4,7)
2.  Instantiate the points as a Point namedtuple class
3.  Create a function to calculate the slope based on the two points
4.  Print the result in the following format: '(p2.y - p1.y) / (p2.x - p1.x) = slope

## Pandas and CSV

"Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.  Pandas allows us to analyze big data and make conclusions based on statistical theories.  
Pandas can clean messy data sets, and make them readable and relevant.  Relevant data is very important in data science." - W3Schools

## Pandas and CSV Challenege

This challenege was done using pandas and csv to read a file iteratively the application includes random states and randomly generated populations and then generate a csv file.

1. Open your file
2. Loop through the file to read each line iteratively
3. Print the line number and the amount of words in each line
CSV
1. Read the following CSV about the United States
2. Add a new header "Capital" and add the capital city for each state
3. Write to the same CSV file
4. Extra fun: calculate the total population of these US states
