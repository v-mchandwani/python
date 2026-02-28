#!/usr/bin/python3
# to check if given string is palindrome
number= input("Enter number ")
if number == number[::-1]:
    print("This num is a palindrome")
else:
    print("This num is not palindrome")
