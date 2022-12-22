import argparse
import time
import string
import os
from itertools import islice

# break the large files into small files of 30000 lines
size = 30000

# This function breaks large txt file into small txt file
# The input is a file name
def createSmallFiles(inputFile):
    # counter for the number subfile created
    counter = 0
    with open(inputFile,"r",encoding="utf8") as txtfile:
        while True:
            # list of 30000 lines
            nextLines = list(islice(txtfile, size))

            # small file number increase
            counter += 1

            # if there are no nextlines break the loop
            if not nextLines:
                break

            # if nextlines exist write the small file
            # small file name format = filename_smallFileNumber.txt
            with open(inputFile.replace(".txt","_{}.txt".format(counter)), 'w', encoding="utf8") as outputFile:
                outputFile.writelines(nextLines)

def main():
    
    #instantiate the object for parsing command line strings into Python objects.
    parser = argparse.ArgumentParser( description = "Count the frequency of words in a text file")

    #attach the require arguments from user: file name and number of processors
    parser.add_argument("fileName", help="Enter the text file name")
    parser.add_argument("numProcessors", type= int, help="Enter the number Processors you would like to use")

    # runs the parser and extract the data from command line
    args = parser.parse_args()

    #the extracted file name that the user entered with extention .txt
    inputFile = args.fileName
    #the file name without the extention
    inputFileName = args.fileName.replace(".txt","")   

    #pool size is the number processor the user entered
    poolSize = args.numProcessors


    # Check if the file entered is a text file. If not exit the program
    if(not(inputFile.endswith(".txt"))): 
        print("not a textFile")
        exit()
        
    # start timestamp to calculate execution time
    t1 = time.time()

    # divide the large text file into small files
    createSmallFiles(inputFile)

    #store the path of small files
    smallFiles = []

    #add the path to each small files to array smallFiles
    for files in os.listdir('.'):
        if files.startswith(inputFileName+"_"):
            smallFiles.append(os.path.join('.',files))

#when the script runs it will excecute the main function
if __name__ == "__main__":
    main()
