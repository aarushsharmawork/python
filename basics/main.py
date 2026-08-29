
# import a library that can tell us jokes
import pyjokes
import random

# print a simple message to the screen
print("hello world")

# ask the pyjokes library for a joke and save it into the variable joke
joke = pyjokes.get_joke()

# print a small poem using triple quotes so the text can span multiple lines
print('''Beneath a sky of Bangalore blue,
       Where ancient banyans whisper too,
       ''')

# store a name in a string variable and print it
# A string is text inside quotes.
a = "aarush"
print(a)
t = type(a)  # used to identify the variable type
print (t)

# examples of other variable types
b = 30      # an integer (whole number)

c = 30.445  # a float (decimal number)
t2 = type(c)  # used to identify the variable type
print (t2) 

d = True # a boolean data type which states true or false
t3 = type(d)  # used to identify the variable type
print (t3)

e = None # none variable type
t4 = type(e)  # used to identify the variable type
print (t4)

# So now lets convert one data type of variable to another
f = "33.45" # now it is considered as a string type variable
g = float (f) # now we are getting the value from the variable f and copying it to g in the for of float
t5 = type(g)  # used to identify the variable type
print (t5)

# Error and Resoving the errors:
# h = input ("Enter the No1.")
# i = input ("Enter the No2.")
# print ("input no1 is :", h)
# print ("input no1 is :", i)
# print ("sum is :", h + i)
# # error
# # 1. so here as you can see instead of giving the straight up sum it would give the just combine both the string
# # 2. even we can write characters in it and it still give us the sum

# # So instead we have to convert the variables to either string or float
# j = float(h)
# k = float(i)
# print ("sum is :", j + k )

# more easy way
H = float (input ("Enter the No1."))
I = float (input ("Enter the No2."))
print ("input no1 is :", H)
print ("input no1 is :", I)
print ("sum is :", H + I)

# A variable can start with letters or _ 
# we can use letter no and underscore after the fist letter or _
# Capital and small letters are considered diffrent variables

# print the joke we got from the library
print(joke)
# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc. 
# 4. Logical operators: and, or, not.
# eg 7 + 4=11 in which 7 and 4 are operants and + is Arithmetic operators where 11 is result

#Arithmetic operators:

AO = 12
AO2 = 34
AO3 = AO + AO2
print (AO3)

# finding remainder 
AO4 = 34
AO5 = 5
print("remainder of the product is: ", AO4 % AO5)

# Assignment operator:
ASO = 4-2  # Assignment operator
ASO2 = 6
ASO2 += 3 # Increase the value of ASO2 by 3 and then assign it to be where we can use +-*/
print (ASO)
print (ASO2)

#Comparison operators 
CO = 12
CO2 = random.randint(1,6)
CO3 = CO + CO2
CO4 = CO3<16
CO5 = CO3>=15
print (CO + CO2)
print (CO4)
print (CO5)
CO6 = 5!=7 # Here != means is not equal to
CO7 = 5!=5
CO8 = 5 == 5 # == is used to check wether 2 values are equal to each other or That means is 5 equals to 5 on the other side
print (CO6)
print (CO7)
print (CO8)

# Logical Operators :
# Table for or
# True or False is True
# True or True is True
# False or True is True
# False or False is False

# Table for and
# True and False is False
# True and True is True
# False and True is False
# False and False is False

# Table for not
# not True is False
# not False is True

# String
"""String are non editable only the things that edit are changed during execution in the particular action or 
fn rather than string
"""
string1 = "abcdefghijklm nopqrstuvwzyz"
print (len(string1)) # for calculating the total length 
#string spilting 
print(string1.split()) # used for spltting string which has gap
print(string1[0]) #used for priniting the first letter of the string
print (string1 [0:8]) #  so here we are printing particular strings from the above string1
# and the rules are very simple string start with 0 and end using : and the last digit while last digit string is not considered in the print
# last rule we can aso use -1 if we want to start from backward
print (string1 [1 :5 : 2] ) 
# so here we are taking the values btw 1 amd 5 ie b-e so b will be printed first and than the next 2 value will be printed btw 1-5
# so it will print the second value btw bcde
# string other cmds
print (string1.endswith("yz"))  # detect wether ends with the letter given will give result in boolean
print (string1.startswith("ab")) # detect wether start with the letter given will give result in boolean
print (string1.capitalize()) # used for capitalising first letter of the alphabet
print(string1.lower()) # used for lowering the case of all the 
print(string1.upper()) # used for uping the case of all the 
print(string1.replace("efgh", "abdc")) # used for replacing  words from string
print(string1.find("b")) # used for finding string position and will return -1 if not found
print(string1.count("a")) # used for counting how many of those words are present
# backslash uses \
print("aarush run's very fast \n and is very athletic \"physique\" ")
# so here as we can see we can also use \n for new line and \"physique\" for preventing py to cause confustion
print("aarush\t19") # give spacing like tab
print("C:\\Users\\Aarush") # with single \ you will get error use two \ to print 1
print('It\'s Python') # used for preventing errors
string2 = input ("Enter your name: ")
print(f"Good Afternoon {string2}") 
# f is used to fetch the stored value of string
#if we dont use f here then py will simply paste {string2} instead of given value
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "aarush").replace("<|Date|", "24 September 2050"))
#here we use replace 2 time first time for the name second time for the date it is called chaining
