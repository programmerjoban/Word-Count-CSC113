

file="test.txt"

def read_file():
    f = open(file, "r")

def Open(fileName):
	if (file name ends with “.txt”):
return open(fileName, "r")
else:
	print(“not a txt file”)
    exit(1)
    

def Write():
g = open(file, "w")
return g.write(Read())

 def createListOfWords(fileObject):
	# empty list
wordList = [ ]
#loop through all the lines in the file
for line in fileObject:
	# in each line split at space which will give the word
	for word in line.split():
		#add the word to the word list
		wordList.append(word)
return wordList
