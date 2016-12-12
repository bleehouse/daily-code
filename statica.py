import random
import string
from string import punctuation


def selectMemberByList(newlist, memberlist, length):
    while length > 0:
        newlist.append(memberlist[random.randrange(0, len(memberlist))])
        length = length - 1
        return newlist

specialcharlist = list(punctuation)
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
charlist = list(string.ascii_lowercase)

totalChar2 = int(input("How many special characters?"))
numChar = int(input("How many special characters?"))
specialChar = int(input("How many special characters?"))

totalChar = totalChar2 - numChar - specialChar

finalStr = ""
newlist = []
newlist = selectMemberByList(newlist, specialcharlist, specialChar)
newlist = selectMemberByList(newlist, numberlist, numChar)
newlist = selectMemberByList(newlist, charlist, totalChar)

print(newlist)

cnt = len(newlist)

while cnt > 0:
    finalStr += str(newlist.pop(random.randrange(0, len(newlist))))
    cnt = cnt - 1

print(finalStr)


