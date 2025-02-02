
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 15
#%%

# Ploteo de curvas de nivel de f: R2-->R
fx = -0.1
fy = -0.1
f = lambda x,y: -np.log(-x**2+y**2)
f_ = '$-log(y^2 - x^2)$'

x = np.linspace(-0.2, 1., 1000)
y = np.linspace(0.2, 1.2, 1000)

xx, yy = np.meshgrid(x, y)

z = f(xx, yy)

z[np.isnan(z)] = 1000


levels = np.sort(np.append(np.linspace(-3, 3, 30),0))

plt.figure(figsize=(10,10))
plt.title(f'Curvas de nivel de f = {f_}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
contours = plt.contour(xx, yy, z, levels, linewidths=2, color='black')
plt.clabel(contours, inline=True, fontsize=8)



#%%

# Ploteo de region a partir de restricciones
# No me gusta mucho el plot

r1 = lambda x,y:x**2+y**2<=1
r2 = lambda x,y:2*x-y<=0
r3 = lambda x,y:y>=1/2
r4 = lambda x,y:x>=0

r = [r1, r2, r3, r4]


z = True
for rs in r:
    z &= rs(xx,yy)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.imshow(z, cmap='Greys', origin='lower',
           extent=(xx.min(),xx.max(),yy.min(),yy.max()), alpha=0.7)
