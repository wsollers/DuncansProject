

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


for k in stopwords.items():
    print(k)

authorwords = {}
with open("authors/dickens/ChristmasCarol/Charles-Dickens-Christmas-Carol.txt") as f:
    for line in f:
        line2 = line.replace('\n','')
        authorwords[line2] = line2

for k in authorwords.items():
    print(k)

