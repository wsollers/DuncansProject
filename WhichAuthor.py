#import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

import nltk.data
from nltk.tokenize import word_tokenize
import codecs
import os


print ("Hello World")
print ("Hello World")
print ("Hello World")



#2.
#Open and Read one of the Authors files into a dictionary.
#The key to the dictionary will be the word the value will be the count
#For example this sentence "A cat is a bat"
#Will have a dictionary entry for A with the value of 2

#
#3 print out this dictionary
#



stopwords = {}
with open("smallwords/StopWords.txt") as f:
    for line in f:
        line2 = line.replace('\n','')
        stopwords[line2] = line2


#for k in stopwords.items():
   # print(k)

authorwords = {}
with open("authors/dickens/ChristmasCarol/Charles-Dickens-Christmas-Carol") as f:
    for line in f:
        line2 = line.replace('\n','')
        authorwords[line2] = line2
#V prints out dictionary V
#for k in authorwords.items():
#    print(k)

#doc = codecs.open('authors/dickens/ChristmasCarol/Charles-Dickens-Christmas-Carol', 'r', 'utf-8')
#doc = codecs.open('authors/dickens/OliverTwist/OliverTwistCharlesDickens.txt', 'r', 'utf-8')
doc = codecs.open('authors/Austen/Pride-And-Predjudice-Jane-Austen.txt', 'r', 'utf-8')
content = doc.read()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = tokenizer.tokenize(content)

wordcount = 0

#
#Step 3.
#
mesuredwords = {}
totalwords = 0
avgwordcount = []
#process each sentecne in a book
for sentence in sentences:
    #print ("#\n"+sentence+"\n#")
    #words per Sentence
    #most common words, but not small
    wordlist = word_tokenize(sentence)
    wordcount = 0
    #process each word in a sentence
    for word in wordlist:
        word = word.lower()
        totalwords = totalwords + 1
        wordcount = wordcount + 1
        if (not word in stopwords and word.isalpha()):
            if (not word in mesuredwords):
                mesuredwords[word] = 1
            else:
                mesuredwords[word] = mesuredwords[word] + 1
            #print("\n"+word+"\n")
    avgwordcount.append(wordcount)
wordspersentence = sum(avgwordcount) / float(len(avgwordcount))
print ("Average sentence Length\t" + str(wordspersentence))
print ("Total Words\t" + str(totalwords))

#print dict sorted by key VVV
for word in sorted(mesuredwords, key=mesuredwords.get, reverse=True):
    if (mesuredwords[word] > 40):
        print(word + "\t" + str(mesuredwords[word])+"\t"+ str(100 * mesuredwords[word]/totalwords))