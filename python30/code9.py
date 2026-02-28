#!/usr/bin/python3
words=open('file.txt', 'r')
content=words.read()
count=0
for i in content.split():
    if i == "mahima":
        count+=1
print(count)
