# Word-Count-CSC113
This is a repo for CSC113's final project.
Due: Dec 23, 2022

Team Mates:
Kevin Pechersky, Shamia Shanaha, Jobanpreet Singh


The following python code is a word frequency counter using multiprocssing. 
It breaks a large text file into small files and then maps the small files to 
the different number of processes specified by the user. 

Repo includes:
1. wordCount.py 

    This is the python script that counts the word frequency.

2. HarryPotterSeriesTestFile.txt

    We have provided a sample text file which includes over million words for you to test the script.
    This text file is combination of all harry potter series. The series were downloaded and merged into 
    one from this github. https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter

3. readme.md

    The readme includes information on how to run the program.

To Run the Program:

  Step 1: save the repsotiory to your machine

  Step 2: Open terminal

  Step 3: The command accepts these arguments: python wordCount.py [file name] [number of processes to use]

        Example: run word count on HarryPotterSeriesTestFile.txt with 5 processes
        python wordCount.py HarryPotterSeriesTestFile.txt 5
        
        
        Example: run word count on HarryPotterSeriesTestFile.txt with 8 processes
        python wordCount.py HarryPotterSeriesTestFile.txt 8


Note: The terminal may not show the entire output because there is a limit on how many line the terminal can show. Please configure your terminal to show more line of the output so that you can get all of the output.
