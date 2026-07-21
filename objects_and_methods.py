this_is_an_integer = 10
this_is_a_string = "Gauri"
type(this_is_an_integer)
type(this_is_a_string)

#after creating a variable in python, you can check all the things that are contained in that variable using 
# . dot in VScode . After you press the dot, it will reveal a list of things contained in the object
#these things come in 2 flavors: 
#1. PROPERTIES: signalled by the wrench icon, contains information, data.
#2. METHODS: Described by a purple box. Described all the actions that can be performed by the object
print(this_is_an_integer.numerator) #10
print(this_is_an_integer.denominator) #1
#properties are describing the state of the object that we created. 
another_integer = 5
print(another_integer.numerator)
#can we check some properties of the string now
print(this_is_a_string) #NO properties in there 

#what is really useful are methods - allow us to do stuff with the objects that we created
#they are like a function, in that they can do things, but they are specifically attached (we say 'bound') to the objects

#let's check out some methods of this is a string:
this_is_a_string.upper() # a method requires parenthesis because they are actions, they are like a function 
#so you need to call them. All strings will have tis method. All objects of a given type share the same method.

this_is_a_string.lower() #everything in lower case
this_is_a_string #methods do not necessarily modify the functions/variables?

#we can store the result of that somehow:
my_upper_name = this_is_a_string.upper()
my_upper_name

another_integer.denominator #white wrenches are properties of the object
another_integer.numerator #we do not put parenthesis
#properties are only meant to be read. they do not do anything, they just exist
#if something does not require any calculation to be given to you, and does not do anything, it is 
#probably a property. but to be sure look at the icon

#strings contain a lot of methods because there are a lot of things that we can do with them
#we have already seen upper(), lower(), title() (capitalizing the first letter of each word)
my_sentence = "hello my name is gauri"
my_sentence.title()

#we have also seen endswith(), here are a few more:
lots_of_white_space = "       gauri  "
lots_of_white_space.strip() #removes all the white space before and after the string

#Practical example of why functions are useful
entry = "  gauri.mahajan@colorado.edu " #this could be something someone entered into a form
#check if this person has a .edu email address
is_it_edu = entry.endswith("edu")
print(is_it_edu) #this would be false because of the white space at the end

stripped_entry = entry.strip()
is_it_edu_for_real = stripped_entry.endswith('edu')
is_it_edu_for_real #since strip removed all the white space for us, we are going to get true this time

#Final thing: we could write is_it_edu_for_real more cleanly:
#here we have created a new variable with strip and then used the endswith method on this new variable
#but we can skip this step:
is_it_edu_for_real = entry.strip().endswith('edu') #entry strip will give us a string so we can put endwith at the end
#this is called chaining. you call methods on an object that is returned by another method

#Common errors with methods and properties

entry.shout() #this gives us an attribute error, no attribute shout() - method does not exist on the object

price = 12
price.numerator() #typeerror: int object is not callable - we call functions in python
#price contains an integer, which is 12 then why are we still getting this error?
#an integer does not do anything, it is not a method or a function so it is not callable
#the error is attempting to call a property, you can only call a method inside an object

price.is_integer() #this is a method: purple box, and it is an action that we are doing
#if we do not put the parenthesis, we are basically not performing the action, we have only called it

#CREATING NEW OBJECT: DECIMAL
# 4 big types of objects: str, float, int, bool. in python you are often going to create objects
from decimal import Decimal #new type we willlearn about in the future
#decimal is a factory for manufacturing a new kind of objects: decimal objects 
#to create a str, you only needed to put quotes around something
#to create a boolean, you need to type True or False, or have a logical comparison
#to create a float or int, you need to type a float or int

#to create decimal objects, we are going to use the decimal thingie we just imported
a = Decimal(".1")
type(a)
b = Decimal(".2")
type(b)
print(.1 + .2) #we get a floating point error, this is because python represents floats with a limited 
#number of zeroes
print(a+b) #we get the right answer or the exact representation

a. #if you reach into a decimal object with the dot, you are going to see a lot of new methods and properties



