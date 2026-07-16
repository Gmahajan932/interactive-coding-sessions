print("Hello world")
print(2+2)
#Here, nothing gets executed when I press enter
#how can I run this code? #2 ways
# 1. you can put the caret on a line and press shift + enter > it is going to send the line to a repl and run it
print("Hello world")
#2. "Run" the file > send the entire content of the file in python, and all the lines will be executed in the sequence
# press the run button at the top right of the central panel > you will want to do this once you've finished writing the script

#Reminder 1: we can create variables in python and assign a content to them:
my_name = "Gauri Mahajan"
print(my_name) #this is printing the content of the variable
#let's send line 12 (print) to the REPL.
# If I only run that line, then i get a NameError: Normal, I have not defined this variable in the REPL yet.

#4 big types of data in python
this_is_an_integer = 10 #anything that doesn't have a decimal
this_is_a_float = 3.14 #decimal
this_is_a_string = "Hello world!" #words
this_is_a_boolean = True 

# Print using the print function
print(this_is_an_integer)
print(this_is_a_float)
print(this_is_a_string, this_is_a_boolean) # we can print multiple things at once, separated by a comma

#print() is something called a function. A function is something that takes between 0 and many arguments, and that has 
#a specific behavior. It is an "action"

#You can print: 
# 1. A value
print(3.14)
print("Hello World")

#2. A variable
print(my_name)

#3. An expression, something that has not been calculated yet, 
print(2+2) #reminder: expressions are calculated 'inside out'
#SKILL: when reading code try to always understand what is going to happen and in which order
#tracing the code: understanding the steps the machine is taking to arrive at a result 

print(this_is_an_integer)
print(this_is_an_integer +5) #can you trace this?
# 1. Read the value contained inside the variable 'this_is_an_integer'
# 2. Do the operation, here, a sum, between this_is_an_integer (10) and 5
# 3. Print the result of the operation

#how do you figure out the type of a variable:
what_is_this = type(this_is_an_integer)
print(what_is_this)
# we can also see that by typing the name of the variable we created
what_is_this
what_is_that = type(3.12)
print(what_is_that)

#Calculations:
print(2 +3)
print(2+ 3*5)
print((2+3)*5) #PEMDAS

print(1+2)
print((1+2) == 3) #double equal: a logical comparison, checking if the elements on the right 
#and on the left have the same value
# logical comparisons always return a boolean. True or False
print(0.1 + 0.2) #wait what
print((0.1 + 0.2) == 0.3) #floating point error - do not expect float operations to be exact
#what can you do
my_rounded_addition = round((0.1 +0.2), 1) #This is a function that takes 2 arguments:
# the element to be rounded
# the digits of precision required
print(my_rounded_addition) #the way to deal with floating point error is to round
round(3.14) #functions can have non-complusory arguments, default arguments. For round, ndigit is equal to 0 if not specified.

#logical comparisons
print(3 == 5) #equality comparison
print(3 != 5) #not equal, different
print(3 > 5) #greater
print(3 < 5) #less
print(3 <= 5) #less or equal
print( 3 >= 5) #more or equal

#you can combine logical comparisons using AND and OR
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False

print(condition_1 and condition_2) # True
print(condition_1 and condition_3) #False
#and only returns True when all the conditions are true

print(condition_1 or condition_2) #True
print(condition_1 or condition_3) #True
print(condition_3 or condition_4) #False
#or returns True as soon as at least one condition is true

#Let's do a few more calculations:
print(True+True) # true are 1, false are 0
print(True == 1)
print(False == 0)
print(True * 5) #this is 5, because for python, true is 1 and false is 0
print(10/0) #cannot divide by 0
print(10 / False) #false is 0

#let's do some string manipulation
#'Calculations with strings'

greetings = "Hello" + "World"
print(greetings) #when used with strings, + is interpreted as a 'concantenation operator', technical 
#word for putting things next to each other

laugh = "ha" * 3
print(laugh) #for strings, the multiplication sign is interpreted as a repeat operation

weird_laugh = "ha" * 3.12
#this gives us a type error because it has to be an integer number
#be careful with mixing up different types, sometimes tolerated, but often rejected... and always confusing
print(very_complicated_laugh) = "ha" * ('hello' == 'hello') * 3
print(very_complicated_laugh)
#keep things simple

#how do we make thinhs simple? we make sure to convert variables before working with them
number = 42
is_this_a_number = "42"
print(number + 10)
print(is_this_a_number + 10) 
#to solve this, create a new variable
now_this_is_a_number = str(is_this_a_number) 
#str() turns something that is not a string into a string
#int() turns into something that is not a number into a number
print(now_this_is_a_number)

int("15") == 15
int("fifteen") #you get an error, cannot convert that into a number
int(False) #we will get 0, this one works

#eg 2:
my_age = 39
my_intro = "Hello, my name is Gauri and I am " + my_age
#How to fix this
my_intro_corrected = "Hello, my is Gauri and I am " + str(my_age)
print(my_intro_corrected)
#str(), float(), int() and bool() are functions
#that can turn an input into the desired type... assuming this is possible

