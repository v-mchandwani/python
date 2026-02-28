#!/usr/bin/python3
num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
operation=input("Enter operation ")
if operation == "add":
    print(num1+num2)
elif operation== "subtract":
    print(num1-num2)
elif operation=="divide":
    print(num1/num2)
elif operation== "multiply":
    print(num1*num2)
else:
    print("Specify correct operation")
