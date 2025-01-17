
class word:
    """
    Used for storing the text, length and count of a word gotten from a text.
    Implements methods for storing the mentioned values and editing them,
    as well as a compare method for sorting.
    """

    def __init__(self, text:str, count=1):
        self.text = text
        self.count = count
        self.length = len(text)
    
    def incr_count(self):
        self.count += 1

    def get_text(self)->str:
        return self.text

    # First sort by length
    def compare(self, other, lengthOrder:str="descending", countOrder:str="descending")->bool:
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
    
    # If lengths match, sort by count
    def sort_secondary(self, other, countOrder:str) -> bool:
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
    
    def __eq__(self, other) -> bool:
        return self.text == other.text
    
    # Simple display for testing
    def __str__(self) -> str:
        return f"Word: {self.text:<20}, Length: {self.length:<5}, count:{self.count:<5}"
    
    def get_len(self) -> int:
        return len(self.text)
    
    def get_count(self) -> int:
        return self.count
    

class word_array:
    """
    Used for storing an array of words.
    Implements iteration, sorting, updating and getting other values.
    """

    def __init__(self, lengthOrder, countOrder):
        self.words = []
        self.lengthOrder = lengthOrder
        self.countOrder = countOrder

    def __getitem__(self, key):
        #get element by its index in the array
        if isinstance(key, int):
            return self.words[key]

        # get element by its text
        elif isinstance(key, str):
            for w in self.words:
                if w.get_text() == key:
                    return w
        else:
            raise KeyError("Incorrect Key")

    def append(self, w: word):
        self.words.append(w)

    def is_in(self, w: word) -> bool:
        for x in self.words:
            if x == w:
                return True
        return False

    def simple_display(self):
        for w in self.words:
            print(w)

    # makes a new word instance if none exist,
    # other wise increases the count of the existing one
    def update(self, w: str):
        if x:=self[w]:
            self[w].incr_count() 
        else:
            x = word(w)
            self.append(x) 

    # I chose bubble sort to use less memory as the array it self can already be large
    def sort(self):
        n = len(self.words)
        for i in range(n):
            for j in (range(0, n - i -1)):
                if self.words[j].compare(self.words[j+1], self.lengthOrder, self.countOrder):
                    temp = self.words[j]
                    self.words[j] = self.words[j+1]
                    self.words[j+1] = temp

    def get_maxes(self) -> tuple[int, int]:
        max_len = -1
        max_count = -1
        for w in self.words:
            if w.get_len() > max_len:
                max_len = w.get_len()
            if w.get_count() > max_count:
                max_count = w.get_count()
        return (max_len, max_count)
    
    def len(self)->int:
        count = 0
        for w in self.words:
            count+=1
        return count