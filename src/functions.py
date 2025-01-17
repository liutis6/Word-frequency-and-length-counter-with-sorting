import re
from .word_classes import *

def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower()

def get_stats(input_path:str, lengthOrder: str, countOrder:str):
    w_array = word_array(lengthOrder, countOrder)

    with open(input_path, "r") as input:
        while (line:=input.readline()):
            text_array = filter_text(line).split()

            for w in text_array:
                w_array.update(w)

    if w_array.len()<1:
        raise ValueError("No text given!")
    
    return w_array

def write_output(output_path:str, w_array:word_array):
    max_len, max_count = w_array.get_maxes()

    head_word = 4 # "Word" has 4 letters
    head_length = 6 
    head_count = 5


    with open(output_path, "w") as output:
        
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



                



        


