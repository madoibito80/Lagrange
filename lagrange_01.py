from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = Axes3D(fig)

#target function
x = np.arange(-1, 1, 0.03)
y = np.arange(-1, 1, 0.03)
X, Y = np.meshgrid(x, y)
Z = 1 - X * X - Y * Y
ax.plot_surface(X, Y, Z, color="#FF0000", alpha=0.1)
ax.contour(X, Y, Z, offset=0)

#subject function
x = np.arange(-1, 2, 1)
y = np.arange(-1, 2, 1)
X, Y = np.meshgrid(x, y)
Z = X + Y - 1
ax.plot_surface(X, Y, Z, color="#0000FF", alpha=0.1)

#subject line
X = np.arange(0, 2, 1)
Y = - X + 1
ax.plot(X, Y, color="#FF00FF")

#gradient vector(subject)
ax.plot(np.array([0.5,0.75]),np.array([0.5,0.75]),np.array([0,0]),color="#0000FF")

#gradient vector(target)
ax.plot(np.array([0.5,0.25]),np.array([0.5,0.25]),np.array([0,0]),color="#FF0000")

plt.show()