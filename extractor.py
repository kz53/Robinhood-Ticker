f = open("raw-output.txt", "r")
n = open("raw-output-numbers.txt", "a")

i = 0
for s in f.readlines:
    if i % 3 = 1:
        n.write(s+"/n")
    i += 1

f.close()
n.close()