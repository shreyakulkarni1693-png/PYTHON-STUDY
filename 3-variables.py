# variables are used to store data in a program. 
# They are like containers that hold values. 
# In Python, you can create a variable by assigning a value to it.

# Example of creating a variable
x = 5
y= "Hello, World!"

print(type(x))   # integer
print(type(y))   # string

x= 4 
x= "Python"
print(x)   # takes last assigned value


#type casting
a=int(3)     #
b=float(3)
c=str(3)

print(a)  
print(b)   
print(c)   



# type() fuction is used to find the data type of a variable
x= 5
y="john"
print(type(x))   # integer
print(type(y))   # string


#variables are case sensitive,

A= 10 
a= 20
print(A)   # 10    
print(a)   # 20

#python - variable names

# variable names must start with a letter or the underscore character
#contains only (A-z, 0-9, and _ )
# names are case-sensitive (age, Age and AGE are three different variables)
#name cannot be python keywords (like if, else, while, etc.)


myvar="shreya"   # valid variable name

my_var= "shreya"  # valid variable name

_myvar ="shreya"  # valid variable name

#1myvar = "shreya"   # invalid variable name

Myvar ="shreya"

#my@var = "shreya"   # invalid variable name


#Multi words variable names

myFullName= "shreya kulkarni"  # camel case

MyFullName = "shreya kulkarni"  # pascal case

my_variable_name = "shreya kulkarni" # snake case



#we can assign multiple values to multiple variables in one line
x,y,z = "orange" , "banana", "kiwi"

print(x)   # orange
print(y)   # banana 
print(z)   # kiwi

#one value to multiple variables

x=y=z= "school"
print(x)   # school
print(y)   # schoo
print(z)   # school


# unpacking of collections

numbers = [1,2,3]
a,b,c =numbers

print(a)   # 1
print(b)   # 2
print(c)   # 3


#output varibales

#print() is used to output variables

x= "python is easy language"
print(x)   # python is easy language

#in print()function we can output multiple variables 

x= "python"
y=  "is"
z= "easy"
print(x,y,z) # python is easy


# + operator can be used to output multiple variables in print() function

x="india"
y="is my"
z="country"

print(x+y+z) # indiais my country

#space is not added between variables when we use + operator in print() function, so we need to add space in the variable itself 
x="india "
y="is my "  
z="country"

print(x+y+z) # india is my country


#but for numbers + ooperator works as mathamatical operator

a=2
b=3

print(a+b)  #5

#if we try to add string and integer it gives error

x= 10
y="shreya"
# print(x+y)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'


#Global variables 

#variable that created outside fuctions
# global varibales can be used by everyone, both inside and outside of functions

x="global variable "

def myfunc():
    print("used anywhere " + x )

myfunc()   # used anywhere global variable


x= 10  # global variable

def mynumber():
    x=5      # local variable
    print(x)

mynumber()


#if i want to use global variable inside a function i can use global keyword

x= 10

def myglobal():
    global  x 
    x=0
    print(x)   #0
myglobal()
print(x) #0


