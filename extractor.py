f = open("raw-output-numbers.txt", "r")
n = open("raw-output-numbers-minute.txt", "a")

i = 0
for s in f.readlines():
    if i % 60 == 0:
        n.write(s)
    i += 1

f.close()
n.close()
