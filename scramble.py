import random
import string
import re

def scramble(word):             #if word length is 1, return as it is.
    if(len(word)==1 or len(word)==2):
        return word

    if(re.search(r"'",word)):   #if word has apostrope, preserve the order.
       foo = list(word[1:-2])
       random.shuffle(foo)
       return word[0] + ''.join(foo) + word[-2] + word[-1]

    if(word[-1]!=',' and word[-1]!='.' and word[-1]!='?' and word[-1]!=';' and word[-1]!='!'):
        foo = list(word[1:-1])
        random.shuffle(foo)
        return word[0] + ''.join(foo) + word[-1]
    
    else:                       #if word has punctuation, preserve order.
        foo = list(word[1:-1])
        random.shuffle(foo)
        return word[0] + ''.join(foo) + word[-2] + word[-1]

f = open("input.txt", "r")
fo = open("output.txt", "w")
scentence = f.read()
words = scentence.split()
msgstr=""

for i in words:
    msgstr+=scramble(i)         #call scramble() for all the words
    msgstr+=' '
fo.write(msgstr)

f.close()
fo.close()


