# simple calculater


num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
op= input("enter operator:")

if op=="+":
    print("result :", num1+num2)

elif op=="-":
      print("result :", num1-num2)

elif op=="*":
     print("result :",num1*num2)

elif op=="/":
     print("result :",num1/num2)

else:
     print("invalid operator")     