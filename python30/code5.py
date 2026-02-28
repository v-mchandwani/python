#!/usr/bin/python3
letters=input("Give name ")
vowels=[]
consonents=[]
for i in letters:
    if i in ['a','e','i','o','u']:
        vowels.append(i)
    else:
        consonents.append(i)
print("The consonents are" , consonents)
print("The vowels are ", vowels)
