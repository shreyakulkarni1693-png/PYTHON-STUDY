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


