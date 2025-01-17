import io, re, sys, classes

def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower()

def get_stats(text, w_array: word_array):
    text_array = filter_text(text).split()

    for w in text_array:
        if w_array.is_in(w):
            w.incr_frequency()
        else:
            w_array.append()
    return w_array


def sort(path, lengthOrder, frequencyOrder):
    words_sorted = []
    lengthOrder = filter_text(lengthOrder)
    frequencyOrder = filter_text(frequencyOrder)

    word_arra = word_array()
    temp = []

    with open(path, "r") as file:
        while (line:=file.readline()):
            word_array = get_stats(line, word_array)
    
    return words_sorted

def get_stats(text, w_array: word_array):
    text_array = filter_text(text).split()

    for w in text_array:
        if w_array.is_in(w):
            w.incr_frequency()
        else:
            w_array.append()
    return w_array

def display(word_dict):
    for k, v in word_dict.items():
        print(f"Word: {k}  length: {v["length"]} frequency: {v["frequency"]}")



                



        


