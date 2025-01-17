import io, re, sys
from word_classes import *

def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower()

def get_stats(path:str, lengthOrder: str, frequencyOrder:str):
    w_array = word_array(lengthOrder, frequencyOrder)

    with open(path, "r") as file:
        while (line:=file.readline()):
            text_array = filter_text(line).split()

            for w in text_array:
                w_array.update(w)

    return w_array


                



        


