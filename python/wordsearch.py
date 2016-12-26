
def wordsearchintext(text, word, wordcount):

    if text.find(word) > -1:
        text = text[(text.find(word)+1):]
        wordcount = wordcount + 1
        return wordsearchintext(text, word, wordcount)
    else:
        return wordcount


number = wordsearchintext("textaaaaaaaaaaaaaaaabbbbaaaaatextaaaaatext", "a", 0)

print(number)


# s = "Happy Birthday"
# s2 = "py"

# print(s.find(s2))
# print(s[(s.find(s2)+1):])

# http://programminghistorian.org/lessons/counting-frequencies
# http://stackoverflow.com/questions/21107505/python-word-count-from-a-txt-file-program
