import numpy as np
import matplotlib.pyplot as plt
import math

# Define the functions
def y1(z):
    return np.tan(z)

def y2(z):
    return np.tan(z - math.pi/2)

def y3(z, z0):
    return np.sqrt((z0/z)**2 - 1)

# Values
z = np.linspace(0.1, 4, 400)  # Avoiding z=0 because it's a singularity for the second function
z0_values = [1.0, 2.0, 3.0, 4.0]

# Plot
plt.figure(figsize=(10, 6))

# Plotting y=tan(z)
plt.plot(z, y1(z), label=r'$y=\tan(z)$', color='black')

# Plotting y=cot(z)=tan(z-pi/2)
plt.plot(z, y2(z), label=r'$y=\tan\left(z-\frac{\pi}{2}\right)$', color='blue')

# Plotting y3 for various z0
colors = ['red', 'green', 'purple', 'orange']
for z0, color in zip(z0_values, colors):
    plt.plot(z, y3(z, z0), color=color)

plt.title('Graphical solution of the transcendental equations for allowed energy in a finite square well')

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='black', label=r'$y=\tan(z)$'),
                   Line2D([0], [0], color='blue', label=r'$y=\tan\left(z-\frac{\pi}{2}\right)$'),
                   Line2D([0], [0], color='white', label=r'$y=\sqrt{\left(\frac{z_0}{z}\right)^2 - 1}$'),
                   Line2D([0], [0], color='red', label=r'    $z_0=1.0$'),
                   Line2D([0], [0], color='green', label=r'    $z_0=2.0$'),
                   Line2D([0], [0], color='purple', label=r'    $z_0=3.0$'),
                   Line2D([0], [0], color='orange', label=r'    $z_0=4.0$')]

plt.legend(handles=legend_elements)

# Setting xticks to multiples of pi/2
xticks_values = [i * np.pi/2 for i in range(4)]  # Creating values for xticks
xticks_labels = [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$"]  # Labels for xticks

plt.xticks(ticks=xticks_values, labels=xticks_labels)

plt.ylim([-10, 10])  # Limit y-axis to view better. tan(z) will have asymptotes that can scale the plot otherwise.
plt.xlabel(r'$z$')
plt.ylabel(r'$y$')
plt.grid(True)
plt.show()
