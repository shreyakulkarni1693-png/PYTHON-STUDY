# Python Operators

print(10+3)

sum1= 200+300
sum2=sum1+ 300
print(sum2)

# Arithmatic Operators

a=10
b=5

print(a+b)      # addition      15
print(a-b)      # subtraction     5
print(a*b)      # multiplication 50
print(a/b)      # dividion        2
print(a%b)      # modulus         2 
print(a**b)     # exponentiation
print(a//b)     # floor division


x=34
y=4

print(x/y)      # division   8.5
print(x//y)     # floor division 8



#Assignment Operators



x=3         # x=3                   
print(x)                        #3
x+=3        # x=x+3
print(x)                        #6
x-=3        # x=x-3
print(x)                        #3
x*=3        # x=x*3
print(x)                        #9
x/=3        # x=x/3
print(x)                        #1.0
x%=3        # x=x%3
print(x)                        #1
x//=3       # x=x//3
print(x)                        #1
x**=3       # x=x**3
print(x)                        #27



#Walrus operator (  :=  )

num=[1,2,3,4,5,6,7]
if(count:=len(num))>4:
    print(f"list has {count} elements")



#comparison Operators

x=3 
y=4

print(x==y)         #equal           false
print(x!=y)         #not equal       true
print(x>y)          #greater than    false
print(x<y)          #less than       true

            
if x>=y:            # greater tahn or equal to
    print("false")    # false
else:
    print("true") 


if x<=y:            # less tahn or equal to
    print("false")    
else:
    print("true")     #true



# Chaining comaprision Operator

x=5
print(1<x<10)
print(1<x and x<10)



#Logical Operator used to combine conditional statements 

x=5
print(x<5 or x >10)
print(0< x  and x<10)

print(not(x> 3 and x<10))


# Identity operator   ( is  ,   is not)

x=3
z=3

print( x is z) #both obj points to same obj menmory
print(y==z)     #compare values

print(x is not z)


# Membership operator ( in , not in)

lst=["banana","kiwi","orange"]

print("banana"in lst)

print("pineapple" not in lst)


txt="Hello world"
print("h" in txt)         # false
print("world"in txt)      # true
print("hello"not in txt)  # true


# Bitwise Operators (& and , | or , ^ xor , ~not , << zero fill left , >>signed right shift)

print (6&3)   #(1 & 1 = 1) otherwise 0

print(6|3)
print(6^3)


#operator precedence 
print(100 + 3 * 5)