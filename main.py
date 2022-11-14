def createsSetOfUniqueWords(wordList):
    return set(wordList)


def countFrequency(wordList, setOfWords):
    for words in setOfWords:
        print(words+":"+str(wordList.count(words)))
