import re
from .word_classes import *

 # remove non-alphnumeric characters and make all of them lowercase
def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower()

# creates a word array
def get_stats(input_path:str, lengthOrder: str, countOrder:str):
    w_array = word_array(lengthOrder, countOrder) #initialize

    # read file
    with open(input_path, "r") as input:
        # as long as the line isn't empty
        while (line:=input.readline()):
            text_array = filter_text(line).split()

            # update the word array for every word in the line
            for w in text_array:
                w_array.update(w)

    if w_array.len()<1:
        raise ValueError("No text given!")
    
    return w_array

def write_output(output_path:str, w_array:word_array):
    max_len, max_count = w_array.get_maxes() # to help with printing

    head_word = 4 # "Word" has 4 letters
    head_length = 6 
    head_count = 5

    with open(output_path, "w") as output:
        #default to the length of the header box unless some values exceed it
        header = (f"| {"Word":<{max_len if max_len>head_word else head_word}} |" + 
                    f" {"Length":<{len(str(max_len)) if len(str(max_len)) > head_length else head_length}} |" +
                    f" {"Count":<{len(str(max_count)) if len(str(max_count)) > head_count else head_count}} |\n")
        
        line = "-"*len(header) + "\n"
        output.write(line)
        output.write(header)
        output.write(line)
        for w in w_array:
            txt = (f"| {w.get_text():<{max_len if max_len>head_word else head_word}} |" + 
                    f" {w.get_len():<{len(str(max_len)) if len(str(max_len)) > head_length else head_length}} |" +
                    f" {w.get_count():<{len(str(max_count)) if len(str(max_count)) > head_count else head_count}} |\n")
            # output.write(f"| {w.get_text():<{max_len}} | {w.get_len():<{len(str(max_len))}} | {w.get_count():<{len(str(max_count))}} |\n")
            output.write(txt)
        output.write(line)

    print("Completed successfully!")



                



        


