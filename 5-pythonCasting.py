#specifying data type
# int() constructs an integer

# Example

a= int(10)                # a will be 10 
b=int(3.14)               # b will be 3  
c=int("6")                # c will be 6

print(a)
print(b)
print(c)
print(type(c))

#float() constructs a float

# Example

x=float(2)                # x will be 2.0           # y will be 3.14      
y=float(3.33)             # y will be 3.33
z=float("9.99")           # z will be 9.99
p=float("4")              # p will be 4.0


print(x)
print(y)
print(z)
print(p)
print(type(p))


# str() constructs a string

# Example

e=str("S1")               # e will be S1 
f=str(2.5)                # f will be 2.5
g=str(10)                 # g will be 10

print(e)
print(f)
print(g)
print(type(g))



# String in python
# 'hello' is same as "hello"

print("hello")
print('hello')

#we can use quotes inside quotes

print("it's ok")                    # it's ok
print('say hello to "shreya"')       # say hello to "shreya"
print("hello,'good morning'")        # hello,'good morning'


#assigning string to a variable

a= "hello"
print(a)

#multiline string 
# we can use """  or '''

a="""lorem20ipsum is simply dummy text of the printing and typesetting industry."""
print(a)

# strings are arrays in python
#Example

print(a[3])          # e
print(a[0])          # l


# looping through a string
# we can loop caracters in string with a "for" loop

for x in "shreya":
    print(x)


# to gte length of string len() function is used  
 
a="hello hello"
print(len(a))


#check string
#to check if a certain phrase or character is present in a string we can use the keyword "in"

txt=" hello world is best program to start with python"
print("program" in txt)

# use it in if statement

txt=" hello world is best program to start with python"
if "hello" in txt:
    print("yes, 'hello' is present in the txt"  )


# check if not    

txt="the best things in life are free" 
print("hello" not in txt)

# use in if statement
txt="the best things in life are free"
if "expensive" not in txt:
    print("no , not present")

#  Slice string
# we can return a range of characters by using the slicing operator (colon)
# specofy where to start the slicing, where to end and step

#example

a= "hello world"
print(a[2:8])    # will get characters from position 2 to 7 (8 is not included)
                 # first charactor has position 0


# Slice to the end 
a= "hello world"
print(a[3:])     # from 3 to end


#Negative slicing
a= "hello world"

print(a[-7:-1])


#modify string
# uppercase  upper() method returns the string in upper case

a= "hello world"
print(a.upper())

# lowercase  lower() method returns the string in lower case

a= "HELLO WORLD"
print(a.lower())


# remove whitespace  strip() method removes any whitespace from the beginning or the end
a="   hello world           "
print(a.strip)


#replace() method to replace a string with another string

a= "hello world"
print(a.replace("l", "q"))

#split() method to split sring into a list

a= "hello my name is shreya"
print(a.split("my"))