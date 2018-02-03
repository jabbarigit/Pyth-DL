
"""to write a function that accepts a sentence of words from user and display the following:
a)	Middle word
b)	Longest word in the sentence
c)	Reverse all the words in sentence
"""

import math #import math library

text =input('Enter your sentence here')
SentToText = text.split() # split the sentence
Sentence_len=len(SentToText) #to measuring the list length
""" the first condition is to check if the sentence has odd or even number of words to find out the middle words. 
in the case even number the middle words will split into min and max and then print them both as the middle words"""
if Sentence_len % 2 == 0:
    Sentence_min=math.floor(Sentence_len/2)-1 #to Flooring the half of the list
    Sentence_max=Sentence_min+1
    S_min=SentToText[Sentence_min]
    S_max=SentToText[Sentence_max]
    print('middle words : ' + S_min +' ' + S_max)
""" the bellow condtion is the case of sentence of odd odd words"""
else:
    mid_word=Sentence_len/2
    Find_Mid_word=SentToText[math.floor(mid_word)] #rounding up to find the middle words
    print('Middle word: ' + Find_Mid_word)
print ('Longest Word: ' + max(text.split(), key=len)) # this part to find the longest words in the sentence
print('reversed sentence:', (text[::-1]))# this part to print the sentence in reversed

