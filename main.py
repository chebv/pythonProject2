import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def func(x):
    return  x**2

X = np.arange(0, 60000, dtype = float)
Y = func(X)

fig = plt.figure(figsize=(8,4))
plt.scatter(X, Y)
plt.show()


print("2222")