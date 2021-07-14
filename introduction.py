introString=input("enter sentence")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
      wordCount=wordCount+1
print("name of the word in sentence")
print(wordCount)
print("name of letters in sentence")
print(characterCount)
   