from word_classes import *
from functions import *

x = get_stats("data/input.txt", "ascending", "descending")
x.sort()
write_output("data/output.txt", x)

# out = open("data/output.txt", "w")
# out.write("works!")

