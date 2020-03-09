import timeit 

f = open("raw-output-3-9-20.txt","r")

nums = []

for s in f.readlines():
    nums.append(float(s))

#start
buys = []
stocks = 0
entry = 0
exits = [] 
profits = 0

def buy(x):
    global stocks
    global profits
    profits -= x
    stocks += 1

def sell(x):    
    global stocks
    global profits 
    profits += x
    stocks -= 1

def sma(a, b):
    global nums
    return sum(nums[a:b+1])/(b-a)

for i in range(23000):
    if i % 60 == 0:
        if stocks == 1:        
            sell(nums[i])
        entry = nums[i]
        buy(nums[i]) 
    elif i % 1  == 0 and nums[i] < entry and stocks == 1:
        sell(entry)
        exits.append([entry, nums[i], nums[i+1], nums[i+2],nums[i+3]])
        #sell(nums[i])
        
if stocks == 1:
    sell(nums[len(nums)-1])

print(exits)
print("Profit: " + str(profits))
print("finished")
