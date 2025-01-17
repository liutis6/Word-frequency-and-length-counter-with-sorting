class word:
    def __init__(self, text, count=1):
        self.text = text
        self.count = count
        self.length = len(text)
    
    def incr_count(self):
        self.count += 1

    def get_text(self):
        return self.text

    def compare(self, other, lengthOrder="descending", countOrder="descending"):
        if lengthOrder == "ascending":
            if self.length > other.length:
                # swap so that the left value becomes the right
                return True
            
            elif self.length == other.length:
                return self.sort_secondary(other, countOrder)
            
            else:
                return False
    
        if lengthOrder == "descending":
            if self.length > other.length:
                # DON'T SWAP
                return False

            elif self.length == other.length:
                return self.sort_secondary(other, countOrder) 
            else:
                return True
    
    def sort_secondary(self, other, countOrder):
        if countOrder == "ascending":
            if self.count > other.count:
                # swap so that the left value becomes the right
                return True
            else:
                return False

        if countOrder == "descending":
            if self.count > other.count:
                # DON't swap so that
                # the left value stays as the lower one
                return False
            else:
                return True
    
    def __eq__(self, other):
        return self.text == other.text
    
    def __str__(self):
        return f"Word: {self.text}, Length: {self.length}, count:{self.count}"
    

class word_array:
    def __init__(self, lengthOrder, countOrder):
        self.words = []
        self.lengthOrder = lengthOrder
        self.countOrder = countOrder

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
            self[w].incr_count()
        else:
            x = word(w)
            self.append(x) 

    # bubble sort to use less memory as the array it self can be quite large
    def sort(self):
        n = len(self.words)
        for i in range(n):
            for j in (range(0, n - i -1)):
                if self.words[j].compare(self.words[j+1], self.lengthOrder, self.countOrder):
                    #print(f"{self.words[j].get_text()} -> {self.words[j+1].get_text()}")
                    temp = self.words[j]
                    self.words[j] = self.words[j+1]
                    self.words[j+1] = temp
