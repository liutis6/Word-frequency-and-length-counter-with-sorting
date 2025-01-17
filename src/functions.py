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
    return w_array

def write_output(output_path:str, w_array:word_array):
    with open(output_path, "w") as output:
        for w in w_array:
            output.write(f"{str(w)}\n")



                



        


