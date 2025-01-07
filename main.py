import sys
import string
import os.path
fname=input("ENter the filename:")

if not os.path.isfile(fname):
    print("File",fname,"doesn't exist")
    sys.exit(0)
infile=open(fname,"r")
file_contents=' '
for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            file_contents=file_contents+ch
        else:
            file_contents=file_contents+''
WordFreq={}
wordlist=file_contents.split()
for word in wordlist:
    if word not in WordFreq.keys():
        WordFreq[word]=1
    else:
        WordFreq[word]+=1
SortedWordFreq=sorted(WordFreq.items(),key=lambda x:x[1],reverse=True)
for i in range(11):
    print(SortedWordFreq[i][0],"occurs",SortedWordFreq[i][1],"times")
    