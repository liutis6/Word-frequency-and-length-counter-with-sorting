import io, re, sys

def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower().split()

def get_stats(text):
    text_array = filter_text(text)
    word_dict = dict()

    for w in text_array:
        if w in word_dict:
            word_dict[w]["frequency"]+=1
        else:
            word_dict[w]= {"frequency" : 1,
                              "length" : len(w)}
    return word_dict

def sort(word_dict, lengthOrder, frequencyOrder):
    words_sorted = {}
    lengthOrder = re.sub(r'\W', " ", lengthOrder).lower()
    frequencyOrder = re.sub(r'\W', " ", frequencyOrder).lower()

    temp = {}

    while len(word_dict)>0:
        temp = sort_length(word_dict, lengthOrder)
        temp2 = sort_frequency(temp, frequencyOrder)

        for k, v in temp2.items():
            # print(f"!{k}!")
            words_sorted.update({k:v})
            del word_dict[k]
            
    return words_sorted

def sort_length(word_dict, lengthOrder):
    if lengthOrder == "descending":
        max_len = -1
        for k, v in word_dict.items():
            # add to temp list if lengths are equal
            if v["length"] == max_len:
                temp.update({k: v})
            # make new list if new max len is found
            if v["length"] > max_len:
                temp = {}
                temp.update({k: v})
                max_len=v["length"]

    if lengthOrder == "ascending":
        min_len = sys.maxsize
        for k, v in word_dict.items():
            # add to temp list if lengths are equal
            if v["length"] == min_len:
                temp.update({k: v})
            # make new list if new max len is found
            if v["length"] < min_len:
                temp = {}
                temp.update({k: v})
                max_len=v["length"]
    return temp


def sort_frequency(word_dict, frequencyOrder):
    if frequencyOrder == "descending":
        max_freq = -1
        for k, v in word_dict.items():
            # add to temp list if lengths are equal
            if v["frequency"] == max_freq:
                temp.update({k: v})
            # make new list if new max len is found
            if v["frequency"] > max_freq:
                temp = {}
                temp.update({k: v})
                max_freq=v["frequency"]

    if frequencyOrder == "ascending":
        min_freq = sys.maxsize
        for k, v in word_dict.items():
            # add to temp list if lengths are equal
            if v["frequency"] == min_freq:
                temp.update({k: v})
            # make new list if new max len is found
            if v["frequency"] < min_freq:
                temp = {}
                temp.update({k: v})
                min_freq=v["frequency"]
    return temp

def display(word_dict):
    for k, v in word_dict.items():
        print(f"Word: {k}           length: {v["length"]} frequency: {v["frequency"]}")



                



        


