import io, re

def filter_text(raw_text):
    return re.sub(r'\W', " ", raw_text).lower().split(" ")

def get_frequency(text):
    text_array = filter_text(text)
    word_counts = dict()
    for w in text_array:
        if w in word_counts:
            word_counts[w]["frequency"]+=1
        else:
            # first element is the frquency
            word_counts[w]= {"frequency" : 1,
                              "length" : len(w)} 
    return word_counts

def sort