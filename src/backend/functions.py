import io, re, sys
from word_classes import *

def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower()

def get_stats(text: str, w_array: word_array):
    text_array = filter_text(text).split()

    for w in text_array:
        if x:=w_array[w]:
            w_array[w].incr_frequency()
        else:
            x = word(w)
            w_array.append(x) 

    return w_array


def sort(path: str, lengthOrder: str, frequencyOrder:str):
    words_sorted = []
    lengthOrder = filter_text(lengthOrder)
    frequencyOrder = filter_text(frequencyOrder)

    w_array = word_array()

    with open(path, "r") as file:
        while (line:=file.readline()):
            w_array = get_stats(line, w_array)
    
    w_array.display()

    return None



                



        


