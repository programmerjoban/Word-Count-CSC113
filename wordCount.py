import argparse
import string

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

#when the script runs it will excecute the main function
if __name__ == "__main__":
    main()
