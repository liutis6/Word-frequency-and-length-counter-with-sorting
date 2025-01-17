from word_classes import *
from functions import *

x = get_stats("data/input.txt", "ascending", "descending")
x.sort()
x.display()

# out = open("data/output.txt", "w")
# out.write("works!")

