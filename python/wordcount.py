
def readInChunks(fileObj, chunkSize=2048):
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

file = open("wordlist.txt", "r+")
wordcount = {}

for wordlist in readInChunks(file):
    for word in wordlist.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

for k, v in sorted(wordcount.items()):
    print(k + ":" + v * "*")


# http://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
# http://stackoverflow.com/questions/21107505/python-word-count-from-a-txt-file-program
# http://stackoverflow.com/questions/8009882/how-to-read-large-file-line-by-line-in-python