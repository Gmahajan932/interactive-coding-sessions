#Collections are objects designed to hold other objects inside them. They are like bags of different kinds

#LISTS
#it is an ordered collection of items. It is created using square brackets. List is an object 
my_empty_list = [] #this is a list that does not contain anything
type(my_empty_list) 
#what do lists do? They contain other objects

my_favorite_numbers = [1,2,3,4,5]
print(my_favorite_numbers)

#lists can contain other elements
my_favorite_colors = ['red', 'blue', 'green'] #this is a list of strings
my_favorite_decimals = [3.14, 2.718, 1.618] #this is a list of floats
my_favorite_booleans = [False, True, False] #lists can contain repeated elements

#Lists can contain different elements of different kind
my_favorite_things = ["red", 3.14, 2, False]

#you can put anything you want into a list. Even other lists
my_mixed_list = [False, ["blue", 19], ["red", False], 3.14]
#do not be surprised lists are very flexible, you can put a lot of things in it

#lists are objects meaning they contain properties and methods.
#Methods of lists:
my_favorite_colors.append('yellow')  #["red", "blue", "green"] #using the append method, you can add more things within the object
#if you just run the line above, it will not print anything but when you print it then you will see it
print(my_favorite_colors) 

#append is super different from all the other methods that we saw before, on strings for instance. Because it CHANGED the object directly. It 
#'mutated' the original object. Let's refresh our memories!
my_string.upper() #I run this, it prints a string in the upper case
print(my_string) #the original string is still in lower case
#in technical terms, the method COPIES the original object, changes it, and returns the copy. The original NEVER changed
#the only way to make changes to a string is to create a new one with a different content.

#back to lists: let's see how methods affect them
my_favorite_colors #now contains ['red', 'blue', 'green', 'yellow]
print(my_favorite_colors) #running another append method to add another color pink
a = my_favorite_colors.append('pink') 
print(my_favorite_colors)
#this method mutated the original list. The content was changed directly by the method. but then what is inside of a? 
print(a) #when you are working with a method that mutates the original, it will typically not return the original. It will simply do something 
#on the original, and return None. 

#NOT ON THE EXAM
#we do not like the fact that every time we are adding things to my favorite colors, it changes the original
my_original_colors = ['pink', 'purple']
#I want to add a color to this list, but NOT modify the original
my_updated_colors = my_original_colors #i want this to be my backup
#now, I can add something to my_updated_colors, and my_original_colors will still exist somewhere
my_updated_colors.append('orange') #i add orange to my_updated_colors
print(my_updated_colors) #we added a color
print(my_original_colors) #it prints the list with orange in it! This is because lists are mutable, so when you give a list different name
#it still points to the same list, rather than creating a copy of the list. 
#if you do not want that, you need to use the copy() method to create a copy of the list

#back to the syllabus
#other methods with LISTS
my_favorite_colors #["red", "blue", "green", "yellow", "pink"]
#to REMOVE an element of the list you can use a method called 'pop'. Pop is going to remove the last element of the list and returns it to you
removed_color = my_favorite_colors.pop()
#what will be the content of my_favorite_colors? 
print(my_favorite_colors) #["red", "blue", "green", "yellow"]
print(removed_color) #pink
#if you re-run the command 
removed_color = my_favorite_colors.pop() #it will remove yellow from the list, returns it to us, and it will get assigned to remove_color

#something new with lists: if you run the same command multiple times, the behavior will change. the list is being mutated, so you are not going
#to get the same results.

#if you do not assign the popped color
my_favorite_colors.pop() #list not contains red, blue, green
#you will just get green in the answer, because if a function returns something and we don't catch it into a varibale, it 'falls' into the terminal

#lists are ordered meaning you can reach into them at a specific position and grab the content.
my_favorite_names = ['Quentin', 'Zoe', 'Mathila']
#I want to read what is at the beginning of the list
#if you want to get an element, you can use an operation called INDEXING. That is you put square brackets after the list, and use the index of the 
#element that you want to grab:
print(my_favorite_names[1]) #you will get zoe: R starts from 1, but in python 0 returns the first element, 1 is the second, 2 is third
print(my_favorite_names[0]) #quentin
print(my_favorite_names[2]) #Mathila

#if you index [3]: INDEX ERROR: list index is out of range, we are tring to grab an element that does not exist
print(my_favorite_names[3])

#Using NEGATIVE INDICES in INDEXING
print(my_favorite_names[-1]) #reads the last value
print(my_favorite_names[-2]) #second to last: Zoe

#we can also do something called SLICING to grab multiple values from a list
my_favorite_numbers = [1,2,3,4,5,6,7,8,9,10]
#indexing again first: 
my_favorite_numbers[2] #we get 3

#slicing: the syntax for slicing is [start:stop:step]. let's see what that means:
my_favorite_numbers[0:3:1] #this means the values between the first and the fourth (excluded), and all of them
#more examples:
my_favorite_numbers[1:6:1] #all values between the second and seventh (excluded)
my_favorite_numbers[3:8:1] #all values between the fourth and eight (or ninth excluded)
my_favorite_numbers[0:6:2] #all values between the first and the sixth (exluded), but we take every other value

#when you are slicing, you can omit some arguments:
my_favorite_numbers[0:3] #by default step is 1 (if omitted)
#this is equivalent to [0:3:1]

my_favorite_numbers[1:] #all of them starting from 1. Both end is omitted (so it defaukts to 'until the end') and step is omitted (so it defaults to 1)
my_favorite_numbers[:4] #omitting the start and the step, start defaults to 0, beginning, stop is 4 (meaning until 4th element, exluded), step 
#is omitted so 1: 
my_favorite_numbers[::2] #start is omitted (so 0), stop is omitted (so until the end), and step is 2; every other value is the entire list
my_favorite_numbers[::-1] #goes backwards because it is negative, so it reverses the list

my_name = 'Quentin André'
my_name_but_mirrored = my_name[::-1]
print(my_name_but_mirrored) #you can slice STRINGS because string is an ordered collection of characters
my_name[0:4] #just so you know you can slice strings too because they are ordered collection of characters!

#Summary of what we have learned so far about lists:
#1. Lists are MUTABLE, meaning we can modify their content using methods
#2. Lists are ITERABLE, meaning we can select a subset of their content using slices.

#putting these 2 points together:
my_favorite_names #["Quentin", "Zoe", "Mathila"]
#it is weird to have my own name as a favorite, let's replace it with 'Adam' in this list
my_favorite_names[0] = 'Adams' #we are reaching into the first position of the list, and in that position we are replacing it with adam
#we are indexing the first element of the list, and assigned the value 'adam' at that position. 
print(my_favorite_names) #we have selected an index and mutated the list/changed the content

#now doing the same thing with slices:
my_favorite_names[1:] #this is slicing ['Zoe', 'Mathilda']
my_favorite_names[1:] = ['Eve', 'Joshua']
my_favorite_names #we can use slicing and indexing to read or update the content of a list

#bonus question: Can we use indexing or slicing to update the content of a string?
my_name[0] = "Z" #nope, this does not work. strings are not mutable!
#if you want a new string, you need to create a new string!

#back to a few LIST METHODS
my_favorite_names.pop() #removes the last element of a list
my_favorite_names.append('Joshua') #add this element at the end of the list
#pop can take an additional argument: The position
my_favorite_names.pop(0) #pop the first element of the list which is adam
my_favorite_names.append() #can onyl append to the end of the list unless we use insert
my_favorite_names.insert(0, 'Adam')
print(my_favorite_names) #inserts adam at the first position
#All these methods are modifying the ORIGINAL list, not returning a copy of the list

my_favorite_names.reverse() #returns NOTHING, it will just change the order of the original list, but not return a new list
print(my_favorite_names)

#figure out which objects are mutable and which are not

#LISTS are collection of ordered items. DICTIONARIES are collections of key:value pairs
my_friends_age = {'Nick': 40, 'Sam': 35, 'Juan': 37} #this is a dictionary
#note the syntax: curly brackets, containing key:value pairs, separated by commas.

#Dictionaries can have different kinds of values:
my_information = {'name': 'Quentin', 'age': 39, 'hobbies':["coding", "skiing", "birding"]}
#here, you have the key "name" that contains a string value
#the key 'age' that contains an int value, the key 'hobbies' contains a list value

#KEYS in the DICTIONARY: they are typically int or str. the most important rules:
#1. they have the be UNIQUE (only one key must have a given name)
#2. they have to be IMMUTABLE

#how do you use dictionaries:
#we can also reach inside them to see the values, that is again called: INDEXING
#For a list, it is ordered, so we index with numbers
#we index with keys? when you have a dictionary
my_friends_age["Nick"] #how do I get Nick's age? I use square brackets to index, and I give the key for which I want to see the value

my_information['hobbies'] 

#Dictionaries like lists are mutable, we can update them!
#let's say my friend nick just celebrated his birthday, to update his age in our dictionary:
my_friends_age["Nick"] = 41 #we have now updated the dictionary, but we still need to print it!
print(my_friends_age) #you reach into the dictionary at the desired key and you assign a new value to it

#changing my name to my full name 
my_information['name'] = 'Quentin Andre' #we put name which is the KEY
print(my_information)

#We can add new keys to a dictionary: I want to add my job to my information
my_information['job title'] = 'marketing prof'
print(my_information)

#we can use indexing to:
# 1. Read the value of an existing key
# 2. Update the value of an existing key
# 3. Create a key with a given value

#since dictionaries are OBJECTS they have METHODS

# 1. first useful method: get()
#if you index a dictionary with a value that does not exist, what happens?
my_information['address']
#if you accidentaly check for a value that does not exist, you will get a Keyerror
#errors are not great when you are writing code, because they will stop your code
#a better way to check if a key exists is to use the method get()
quentin_adress = my_information.get("address")
print(quentin_adress) #this will print None, .get() returns None when the key is not found

#three other useful methods: 
#2. rather than blindly checking if a key exists, sometimes you want to see all the keys that exist in a dictionary
my_information.keys() #this will check all the keys in the dictionary
# you can do the same thing to see all the values with values()
my_information.values() #this will check all the values in the dictionary
#the only part missing is you do not have the mapping between the key and value, which key is linked with which value/coresspond
my_information.items() #going to give us all the key;values pairs in the data

#reminder: the keys of dictionaries must be str or int
#the values can be anything: so far we have seen str values, int values, list values

#Something very common is to have dictionaries as values, to store more complex information. here is an example
my_friends_info = {
    "Nick": { #one key: Nick, one value: his dictionary.
        "age": 41, #inside that dictionary, other keys (his information) and values (what they are)
        "city": "Boulder",
        "hobbies": ["skiing", "cooking"]
    },
    "Sam": {
        "age": 35,
        "hobbies": ["hiking", "coffee"],
        "job": 'professor'
    } #another key: sam, one value: his dictionary of information
}

#to use the dictionary like this: how would you get your friend nick's age




