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

## TODO:
* Read file
    * Filter text by removing punctuation and making it all lower case.
    * ~~Create a dictionary that would count each words frequency~~ ->
    * Create classes for word and word array
* Make bubble sort
* Implement changable parameters gotten from settings.json
* Print the sorted list
    * Show the length and frequency of the words
    * Tabulate
