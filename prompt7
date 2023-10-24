import matplotlib.pyplot as plt
import numpy as np
#declaring variables
x = []
num = 0.0
#setting up x and its 100 steps between 0,1
for i in range(101):
    x.append(num)
    num += 0.01
#definition of the function 
def e(x):
    return np.exp(x)

#plotting 
y = e(x)
plt.plot(x,y)
plt.xlabel('Time [milliseconds]')
plt.ylabel('Awesomeness')
plt.title('Awesomeness over Time')
plt.savefig('awesomeness_plot.pdf', format='pdf')
