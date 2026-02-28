#!/usr/bin/python3
num = input("Enter numbers: ")
num_list=list(map(int, num.split()))
unique=set(num_list)
blah=sorted(unique)
print(blah[-2])

