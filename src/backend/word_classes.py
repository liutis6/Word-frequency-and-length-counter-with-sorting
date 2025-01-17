class word:
    def __init__(self, text, frequency=1):
        self.text = text
        self.frequency = frequency
        self.length = len(text)
    
    def incr_frequency(self):
        self.frequency += 1

    def compare(self, other, lengthOrder="descending", frequencyOrder="descending"):
        if lengthOrder == "descending":
            if self.length < other.length:

                if frequencyOrder == "descending":
                    if self.frequency < other.frequency:
                        return True
                    else:
                        return False
                    
                if frequencyOrder == "ascending":
                    if self.frequency < other.frequency:
                        return False
                    else:
                        return True
            else:
                return False
                    
        if lengthOrder == "ascending":
            if self.length > other.length:

                if frequencyOrder == "descending":
                    if self.frequency > other.frequency:
                        return True
                    else:
                        return False
                    
                if frequencyOrder == "ascending":
                    if self.frequency > other.frequency:
                        return False
                    else:
                        return True
            else:
                return False
    
    def __eq__(self, other):
        return self.text == other.text
    

class word_array:
    def __init__(self):
        self.words = []

    def append(self, w):
        self.words.append(w)

    def is_in(self, w):
        for x in self.words:
            if x == w:
                return True
        return False