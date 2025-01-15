# Word frequency and length counter (with settings)

## Description:
Word frequency and length counter that ignores semantic context as well as case sensitivity.

The following parameters are controlled through the settings file:
* Path to text file
* Path for result
* Sort order

Additional requirements:
* No punctuation marks

## TODO:
* Read file + text
    * Filter text by removing punctuation and making it all lower case.
    * Create a dictionary that would count each words frequency
* Make bubble sort
    * Implement easily changable parameters that could be changed in a different file
* Display the words 
    * show their length and frequency

* Overengineering thoughts:
    * Implement GUI
        * Can pick file
        * Choose sort direction
        * Display bar graph
