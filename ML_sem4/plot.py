import matplotlib.pyplot as plt
import numpy as np 

x=np.arange(5)
y=[20,10,30,40,15]
# plt.bar(x,y)
plt.scatter(x,y)
# plt.show()
plt.bar(x,y)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plotting random stuffs")
plt.savefig(".\\new.jpg")        #saving the plotted fig as new.jpg in current working dir.
plt.show()
