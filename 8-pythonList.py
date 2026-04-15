# list - used to store multipal items in single variable 
# list store collection of data
# list created by using [] brackets 

fruits=["banana", "kiwi", "apple"]
print(type(fruits))
print(fruits)

#list items are "ordered", "changeable","allow duplicate value"

'''ordered ===== items have defined order and cannot change 
                 new item added at the end of the list '''

'''changeable====  after creating list we can add remove items'''

'''Allow Duplicates==== list are indexed , can have items with same value '''

fruits=["banana","kiwi","apple","cherry","kiwi"]
print(fruits)

print(len(fruits))   # determins length of items in list

list1=["banana","kiwi","apple","cherry","kiwi"] # string
list2=[1,2,3,4,5,6,7,8]                         # integer
list3=[True, False, True ]                      # boolean

print(list1)
print(list2)
print(list3)


mixed=["shreya", 2, 3.14, True , "Female"]
print(mixed)


# list by using list() constructor 

mylist=list(("shreya", 2, 3.14, True , "Female"))
print(mylist)


# Access list items 

thislists=["banana","kiwi","apple","banana","cherry" ,"melon", "mango"]
print(thislists[2])
print(thislists[2:5])
print(thislists[1:3])
print(thislists[-2])
print(len(thislists))
print(thislists[:6])
print(thislists[3:])
print(thislists[-4:-1])

# in keyword 

list=["banana","kiwi","apple"]
if "apple"in list:
    print("yes, 'apple' is present in list")


#change item value

list=["banana","kiwi","apple","banana","cherry" ,"melon", "mango"]
list[4]="kiwi"
print(list)

list[1:4]=[1,2,3]
print(list)

list[1:2]=["spinach","pumkin"]
print(list)

list=["spinach","pumkin","chilli"]
list[1:3]=["brinjal"]
print(list)


# insert() method to insret items on specified index

num=[1,2,3,4,5,6]
num.insert(3,"watermelon")
print(num)

mylist=['apple','banana', 'chreey']
mylist[0]='kiwi'
print(mylist[1])


# append ( )   : add list items at the end 

num=[1,2,3,4]
num.append(2)
print(num)

# extend list = to append new list in current list
num1=[1,2,3]
num2=[4,5,6]
num1.extend(num2)
print(num1)         #elements are added at the end of list


#Add any iterable( tuples , set , dictionaries)
num1=[1,2,3]
tup1=(9,8,7)
num1.extend(tup1)
print(num1)

# Remove( ) removes specified item

num=[1,2,3,4]
num.remove(2)
print(num)

# if thereis duplicate in list removes first occurance

num=[1,2,2,3 ]
num.remove(2)
print(num)      #removed 1st 2 from list

# pop( )  removes the specified index

fruits=["banana","kiwi","apple","mango"]
fruits.pop(1)
print(fruits)

fruits.pop()
print(fruits)

# del keyword

num=[1,2,3,4,5]
del num[3]
print(num) # 4 gets deteted

#clear() method = empties list 

num=[1,2,3,4,5,6,7,8,9]
num.clear()
print(num)        # output [] list with no content


#loop list

num=[1,2,3,4 ,4,6]
for x in num:
    print(x) 

# loop through index number use range() and len()

num=[1,2,3,4]
for x in range(len(num)):
    print(num[x])    

# using while loop
# use len()function   

#print all items using while loop to go through all index number

thislist=["apple","kiwi","banana"]
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1 

# looping using list comprehension

fruits=["apple","kiwi","banana","mango"]
newfruits=[]

for x in fruits:
    if "a" in x:
        newfruits.append(x)
print(newfruits)        

#same we can do with list comprehension
fruits=["apple","kiwi","banana","mango"]
newfruit=[x for x in fruits if "a"in x]

print(newfruit)


#newlist = [expression for item in iterable if condition == True]

#eg. accept fruits that are not apple

fruits=["apple","kiwi","banana","mango"]
newlist=[ x for x in fruits if x != "apple"]

print(newlist)

# eg. with no if statement
fruits=["apple","kiwi","banana","mango"]
newlist=[ x for x in fruits]

print(newlist)


# we can use range() to create an iterable

newlist=[ x for x in range(10)]
print(newlist)

newlist=[x for x in range(10)if x < 5]
print(newlist)

fruits=["apple","kiwi","banana","mango"]
newlist=[x.upper() for x in fruits ]

print(newlist)

# we can set all value to "hello"
fruits=["apple","kiwi","banana","mango"]
newlist=["hello" for x in fruits ]
print(newlist)

fruits=["apple","kiwi","banana","mango"]
newlist=[x if x!= "banana"else "orange" for x in fruits]

print(newlist)


fruits=["apple","banana","mango"]
newlist=[x for x in fruits if x=="banana"]
print(newlist)



# Sort list alphanumerically use sort() method


newlist=["apple","kiwi","banana","mango"]
newlist.sort()
print(newlist)


num=[100, 46 , 23, 1, -3, 67]
num.sort()
print(num)

# sorting in decending order
num=[100, 46 , 23, 1, -3, 67]
num.sort(reverse=True)
print(num)


#customize sort using key= function

def myfunc(n):
    return abs(n-50)
thislist=[100, 50,65, 82,23]
thislist.sort(key=myfunc)
print(thislist)


# case sensitive sort 
#sort()is case sensitive all capital letters sorted first


fruits=["Banana","kiwi","Mango","apple"]
fruits.sort()
print(fruits)   #['Banana', 'Mango', 'apple', 'kiwi']

# if you want a case-insensitive sort function, use str.lower as a key function:


fruits=["Banana","kiwi","Mango","apple"]
fruits.sort(key=str.lower)
print(fruits)      #['apple', 'Banana', 'kiwi', 'Mango']


# reverse()

fruits=["Banana","kiwi","Mango","apple"]
fruits.reverse()
print(fruits)  #['apple', 'Mango', 'kiwi', 'Banana']


# reverse()

fruits=["Banana","kiwi","Mango","apple"]
fruits.reverse()
print(fruits)  #['apple', 'Mango', 'kiwi', 'Banana']

# reverse()

fruits=["Banana","kiwi","Mango","apple"]
fruits.reverse()
print(fruits)  #['apple', 'Mango', 'kiwi', 'Banana']

