# import collections

file = open("wordlist.txt", "r+")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

# wordcount = collections.OrderedDict(sorted(wordcount.items()))

for k, v in sorted(wordcount.items()):
    print(k + ":" + v * "*")


# http://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
# http://stackoverflow.com/questions/21107505/python-word-count-from-a-txt-file-program