# Word frequency and length counter with sorting

## Description:
Word frequency and length counter that ignores semantic context as well as case sensitivity.

The following parameters are controlled through the settings file:
* Path to text file
* Path for result
* Sort order by:
    1) Length of the word
    2) Count

## Instructions
- Run "main.py"
    - Change "settings.json" if needed

## Structure
- main.py - blunt method to run the entire program
- settings.json - holds the settings for the program to accomodate
- data - holds the input and output files
- src - holds all of the files to make the program work
- tests - stores test cases for different sorting variations

## TODO:
* Read file
    * Filter text by removing punctuation and making it all lower case.
    * ~~Create a dictionary that would count each words frequency~~ ->
    * Create classes for word and word array
* Make bubble sort
* Implement changable parameters gotten from settings.json
* Print the sorted list
    * Show the length and frequency of the words
    * Tabulate and auto space the words and numbers in the table
* Add safeties
* Create simple test cases
* Add comments
