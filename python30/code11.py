#!/usr/bin/python3
#common elements btw two lists
word1=['3','4','6','8']
word2=['2','4','8','7']
word3=list(set(word1).intersection(word2))
print(word3)
