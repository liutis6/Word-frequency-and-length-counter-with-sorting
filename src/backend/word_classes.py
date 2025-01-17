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
        if lengthOrder == "ascending":
            if self.length > other.length:
                # swap so that the left value becomes the right
                return True
            
            elif self.length == other.length:
                return self.sort_secondary(other, frequencyOrder)
            
            else:
                return False
    
        if lengthOrder == "descending":
            if self.length > other.length:
                # DON'T SWAP
                return False

            elif self.length == other.length:
                return self.sort_secondary(other, frequencyOrder) 
            else:
                return True
    
    def sort_secondary(self, other, frequencyOrder):
        if frequencyOrder == "ascending":
            if self.frequency > other.frequency:
                # swap so that the left value becomes the right
                return True
            else:
                return False

        if frequencyOrder == "descending":
            if self.frequency > other.frequency:
                # DON't swap so that
                # the left value stays as the lower one
                return False
            else:
                return True
    
    def __eq__(self, other):
        return self.text == other.text
    
    def __str__(self):
        return f"Word: {self.text}, Length: {self.length}, Frequency:{self.frequency}"
    

class word_array:
    def __init__(self, lengthOrder, frequencyOrder):
        self.words = []
        self.lengthOrder = lengthOrder
        self.frequencyOrder = frequencyOrder

    def __getitem__(self, key): 

        if isinstance(key, int):
            return self.words[key]

        elif isinstance(key, str):
            for w in self.words:
                if w.get_text() == key:
                    return w

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

    def update(self, w: str):
        if x:=self[w]:
            self[w].incr_frequency()
        else:
            x = word(w)
            self.append(x) 

    # bubble sort to use less memory as the array it self can be quite large
    def sort(self):
        n = len(self.words)
        for i in range(n):
            for j in (range(0, n - i -1)):
                if self.words[j].compare(self.words[j+1], self.lengthOrder, self.frequencyOrder):
                    #print(f"{self.words[j].get_text()} -> {self.words[j+1].get_text()}")
                    temp = self.words[j]
                    self.words[j] = self.words[j+1]
                    self.words[j+1] = temp
