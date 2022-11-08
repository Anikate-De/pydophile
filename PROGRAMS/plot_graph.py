
#Program to plot a scatter graph
import matplotlib.pyplot as plt
import numpy as np
X=np.random.randint(1,100, size=(100,))
Y=np.random.randint(1,100, size=(100,))
plt.scatter(X,Y,color='r')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()