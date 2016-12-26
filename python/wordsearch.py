
def wordsearchintext(text, word, wordcount):

    if text.find(word) > -1:
        # print(text.find(word))
        text = text[(text.find(word)+1):]
        wordcount = wordcount + 1
        # print(text)
        return wordsearchintext(text, word, wordcount)
    else:
        return wordcount


number = wordsearchintext("textaaaaaaaaaaaaaaaabbbbaaaaatextaaaaatext", "a", 0)

print(number)


# s = "Happy Birthday"
# s2 = "py"

# print(s.find(s2))
# print(s[(s.find(s2)+1):])

