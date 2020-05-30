#talib playground
import talib as ta
import numpy as np 
import matplotlib.pyplot as plt

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array([ 2.0, 5, 7])
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

a = np.array([1.0, 2.0, 5, 7, 11, 13.5, 16])
ax = np.array([0,1,2,3,4,5,6])
aslope = ta.LINEARREG_SLOPE(a, 7)[-1]
aint = ta.LINEARREG_INTERCEPT(a, 7)[-1]

print(aslope)
print(aint)


b = [1.0, 2.0, 5.0, 7.0, 11.0, 13.5, 16.0]
bx = [0.0,1.0,2.0,3.0,4.0,5.0,6.0]
# bslope = ta.LINEARREG_SLOPE(b, 7)
# bint = ta.LINEARREG_INTERCEPT(b, 7)

plt.plot(bx, b, 'b.')
plt.ylabel('price')
plt.xlabel('time')

abline(aslope, aint)

plt.show()
