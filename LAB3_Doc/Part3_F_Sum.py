# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:23:17 2018

@author: Abdoh Jabbari
"""
# lists of libraries that are we need to this code 
import re, collections
from nltk.tokenize import wordpunct_tokenize,sent_tokenize,word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

# adding function to define text read the text file and import the article 
def impo_file(text):

    return re.findall('[a-z]+', text.lower())
textl=[]
text_words = impo_file(open('article.txt').read())

#apply lemmatization on the words
Lemintize=WordNetLemmatizer()
for i in text_words:
    textl.append(Lemintize.lemmatize(i,pos='v'))

text3=[]
text2=pos_tag(textl)

counter=0
counter1=0
text4=[]
while counter<len(text2):
    if text2[counter][1]!='VB' or text2[counter][1]!='VBD' or text2[counter][1]!='VBG' or text2[counter][1]!='VBN' or text2[counter][1]!='VBP' or text2[counter][1]!='VBZ':
        text3.append(text2[counter])
    counter +=1
print (text3)
print ("========================")

#Calculate the word frequency 
#-	Choose top five bi-grams that has been repeated most
WORD_freq = collections.Counter(text3)
commn=WORD_freq.most_common(5) 

print ("the word frequency Calculatetion: \n", commn)
print ("========================")
while counter1<len(commn):
    text4.append(commn[counter1][0][0])
    counter1 +=1

print ("top five bi-grams that has been repeated most: \n", text4)
print ("========================")
#Finding all the sentences with those most repeated bi-grams
sentense = open('article.txt').read().lower()
w=sent_tokenize(sentense)

#Extract sentences and concatenate
text5=[]
for i in w:
    t=word_tokenize(i)
    for j in t:
        if j in text4:
            text5.append(i)
        break

print ("sentences and concatenate \n", text5)
print ("==========The End==============")
