class word:
    def __init__(self, text, frequency=1):
        self.text = text
        self.frequency = frequency
        self.length = len(text)
    
    def incr_frequency(self):
        self.frequency += 1

    def get_text(self):
        return self.text

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
    
    def __str__(self):
        return f"Word: {self.text}, Length: {self.length}, Frequency:{self.frequency}"
    

class word_array:
    def __init__(self):
        self.words = []

    def __getitem__(self, text:str) -> word: 
        for w in self.words:
            if w.get_text() == text:
                return w
        return None

    def append(self, w: word):
        self.words.append(w)

    def is_in(self, w: word):
        for x in self.words:
            if x == w:
                return True
        return False

    def display(self):
        for w in self.words:
            print(w)