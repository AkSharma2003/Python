import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x

plt.plot(x, y)
plt.show()

p=x**2
plt.plot(x,p)
plt.show()

y=np.sin(x)

plt.plot(x,y)
plt.show()

y=x*np.log(x)
plt.plot(x,y)
plt.show()