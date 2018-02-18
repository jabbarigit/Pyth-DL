"""Using Numpy create random vector of size 15 having only Integers in the range 0 -20.
Write a program to find the most frequent item/value in the vector list.
Sample input:[1,2,16,14,6,5,9,9,20,19,18]
Sample output: Most frequent item in the list is 9"""

#importing numpy package
import numpy as np
# Numpy create random vector of size 15 having only Integers in the range 0 -20
y=np.random.randint(20, size=15)

print(" Random Numbers Are:")
# print the random numbers
print(y)
print("Most frequent # in the array is:")

# count the numbers and then find the most frequent number in the array
print(np.bincount(y).argmax())