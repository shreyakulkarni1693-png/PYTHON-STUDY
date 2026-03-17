#Data types in python
#variables can store data of different types, and different types can do different things.
# to get type of variable type() function is used.

x="shreya"    # string (text type)

x=2           # integer  (numeric type)
x=3.14        # float  
x=1j          # complex number

x=[1,2,3]     # list (collection of items)
x=(1,2,3)     # tuple 
x=range(3)

x= {"name": "shreya", "age": 32}   #dict (mapping type)

x={"apple", "banana","kiwi"}       #set  (collection type)
x=frozenset({"apple", "banana","kiwi"})  # frozenset (immutable set)

x=True       # bool  (boolean type)

x=b"hello"   # bytes (binary data)
x=bytearray(4)   #bytearray
x=memoryview(bytes(5))   #memoryview

x=None   #None type


#python Numbers 

x= 5      # int
y= 5.2    # float
z=1j      # complex number

print(type(x))
print(type(y))
print(type(z))

#integer is whole number, positive or negative,
#  without decimals, of unlimited length.

x=3
y=145624789963221456622
z=-4561236654456

print(type(x))
print(type(y))
print(type(z))

#float is a number, positive or negative, containing one or more decimals.

x=3.42
y=-3.32

print(type(x))
print(type(y))

#float can also be scientific numbers with an "e" to indicate the power of 10.
x=4E2
y=3e3
z=-34.7e100

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)    
print(z)

#complex numbers are written with a "j" as the imaginary part.

x=4+6j
y=8j
z= -3j

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)    
print(z)

#type conversion
#you can convert from one type to another 

x= 1      #int
y= 2.3    #float
z= 3j     #complex

#convertfrom int to float 

a=float(x)
print(a)
print(type(a))

b=complex(x)
print(b)    
print(type(b))

#convert from float to int

c=int(y)
print(c)
print(type(c))

d=complex(y)
print(d)
print(type(d))


# can not convert complex to int and float


# Random number
#python has a built-in module called random that can be used to generate random numbers.

#example
#import the random module

import random

print(random.randrange(1,10))



