#we have been using functions from Day 1:
#print(), type(), round(), str(), float(), int(), bool(), len()
len("Gauri") #number of elements in a string, or a sequence

#FUNCTION: It is like a machine, it does something. usually takes one or more inputs and usually returns a result
# print() <- #it takes any expression that we want to print, and it prints stuff to the user.
# str() <- #it takes any expression, and it turns it into a string, and returns it to the user.

#when we day RETURN something, 
#taking print as an example
print('1234')
my_content = print("1234")
my_content #my content is empty. print("1234") did not store anything in it. 
#this is because some functions(most) return something. think of them as a conveyor belt:
#they are going to take an object on one side, do things to it, and then RETURN the result of what
#it did on the other side of the machine.

#other functions are just doing stuff: think of them as an engine. you are going to put some gas into
#them, they are going to do something, but they are not going to hand you back anything.

#writing functions together to better understand this distinction
#we are going to write a function that takes a price, a rate, and returns the price updated wuth the rate

#to create a new function, we use this syntax
def print_total(price, rate): #def, followed by function name, parenthesis(arguments)
    #you will see that your cursor moved to the right: this defines the body of the function
    #every code inside is going to define what the function will do.
    total = price * (1+rate)
    print(total)

#we have created our functions, let's test it:\
print_total(10, .1) #let's run this, and practice tracing the code
#to store this result for later use
my_total = print_total(10, .1)
my_total #nothing inside my_total. this function does not return anything to me as a user. It is 
#just doing things. Engine, not converyor belt. 

#ANOTHER function to SOLVE this issue
def calculate_total(price, rate): #same structure as before
    total = price * (1+rate)
    return total # on the other side of the conveyor belt, spit out the total.

my_total = calculate_total(10, .1) 
print(my_total) #this contains the results I want because of the function
#this functions calculated something, RETURNED it back to me, and now i can store it into a variable

# if we do not store it then:
calculate_total(10, .1) #falls into the terminal and gets printed

#it is better to have functions that are returning something over printing something. gives more
#flexibility to the user.

#more vocabulary: the inputs of a function are called ARGUMENTS. Come in 2 flavors:
#1. 'Positional arguments' defined by the order in which you enter them
round(3.14, 1) #rounds the first number to the number of digits in the second number
round(1, 3.14) #we get an error because float object cannot read as an integer

calculate_total(10, .1)
calculate_total(.1, 10) #position arguments are expected in a certain order and given in a certain order

#some functions take a variable number of arguments
round(3.14) #here the second argument is not compulsory. it has a default, which is 0
print('ABC') #Print 'ABC'
print('ABC', 'DEF', 'GHI') #prints 'ABC DEF GHI'
#print is an example of a functions that takes an arbitrary number of arguments
#you can give as many as you want, and it is going to print them all.

#2. 'named' arguments or 'keyword' arguments - arguments added by specifying their name
print('A', 'B', 'C', 'D', sep="*") #Prints A*B*C*D
#here sep is a named arguments, and I give it the value of *
#Named arguments are not compulsory, and have a default value
#default argument for sep is a space
print('A', 'B', 'C', 'D', sep='-', ends='!') #prints A-B-C-D!

#final but important concept
def add_excitement(string):
    excited_string = string + "!!!!!!!!"
    return excited_string
    print("The function ran successfully") #added this after the return

python_is_fun = add_excitement("Python is fun")
python_is_fun

#once a function hits the return statment, the function is done. Anything added after a return will not do anything













