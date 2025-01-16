from functions import *

inp = open("data/input.txt", "r").read()
x = sort(get_stats(inp), "descending", "descending")

display(x)

out = open("data/output.txt", "w")
out.write("works!")

