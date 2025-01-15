from word_frequency import *

inp = open("data/input.txt", "r").read()
print(inp)
print("NEW TEXT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print(get_frequency(inp))

out = open("data/output.txt", "w")
out.write("works!")

