import matplotlib.pyplot as plt
import numpy as np

#load data
f = open("raw-output-3-24-20.txt","r")

#initialize all values 
ys = []
time = 0
xs = []
minute_xs = []
minute_ys = []
exit_xs= []
exit_ys = []
counter = 0 
entry = 0
stocks = 0
exits = []
#main loop
for p in f.readlines():
    ys.append(float(p))
    xs.append(time)

    if counter % 60 == 0:
    	minute_ys.append(float(p))
    	minute_xs.append(time)
    	entry = float(p)
    	stocks = 1
    elif counter % 1  == 0 and stocks == 1 and float(p) < entry:
        stocks = 0
        exit_ys.append(float(p))
        exit_xs.append(time)
        
    #end loop
    time += 1
    counter += 1


plt.plot(xs, ys)
plt.plot(minute_xs, minute_ys,'ro')
plt.plot(exit_xs, exit_ys,'g^')
print(str(len(exit_ys)))
print(str(len(exit_xs)))
plt.ylabel('price')
plt.xlabel('time')
plt.show() 