import numpy as np
import matplotlib.pyplot as plt

INTERVAL = 0.5

x = np.arange(-5,5,INTERVAL)
y = np.arange(-5,5,INTERVAL)

X, Y = np.meshgrid(x,y)
print(Y)

# Functions. CHange these
# In the form of dy/dx = f(x)/g(x).
# For dx/dy = -y -sin(x), f(x)=-y-sinx, g(x)=1

dy = -Y - np.sin(X)
dx = np.ones(dy.shape)

plt.quiver(X,Y,dx,dy)
plt.title("Direction Field")
plt.show()