# string methods in python

#capitalize() convers first charactor to upper case
a= " hello world "
print(a.capitalize())

#casefold( ) converts string to lower case
a= " HELLO WORLD "
print(a.casefold())

#center() returns centered string
a= "hello world is greate program to start"
print(a.center(9))

#count( ) returns no fo count occurs in string
a= "hello world"
print(a.count("l"))

#encode() returns encoded version of the string
a= "hello world "
print(a.encode())

#endswith() returns true if string ends with specified value
a="hello world"
print(a.endswith("r"))

#find() returns the index of first occurence of specified value
a= "hllo world"
print(a.find("w"))
print(a.find("l"))


#expandtabs() sets the tab size of the string
a= "hello world"
print(a.expandtabs())

#format() formats specified values in a string
a="Hello, my dog is cute and his name is {}"
print(a.format("tommy"))

#index() returns the index of first occurence of specified value
a= "hello world"
print(a.index("w"))

#isalnum() returns true if all characters in the string are alphanumeric
a="hello world 123456"
print(a.isalnum())

#boolean

a=200
b=100
if a<b:
 print("true")
else:
 print("false") 


 print(10==9)

 print(bool("shreya"))
 print(bool(23))
 print(bool())
 print(bool(0))

class myclass():
  def _len_(self):
   return 0
  
myobj= myclass()
print(bool(myobj))  


def myfunction():
 return False

print(myfunction())

def myFunction():
 return True
if myFunction():
 print("YES !")
else:
 print("NO !")
 
x=200
print(isinstance(x,str))