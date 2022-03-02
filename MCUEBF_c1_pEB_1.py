from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np 

m, q = 1, 1
v = 10
Ex, Ey, Ez = 0, 2, 0
Bx, By, Bz = 0, 3, 0

def dS_dt(S, t):
    x, y, z, vx, vy, vz = S
    dx_dt = vx
    dy_dt = vy
    dz_dt = vz
    dvx_dt = (q/m)*(Ex+vy*Bz-vz*By)
    dvy_dt = (q/m)*(Ey+vz*Bx-vx*Bz)
    dvz_dt = (q/m)*(Ez+vx*By-vy*Bx)
    return [dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt]

t = np.linspace(0, 20, 1001)
S0 = (0, 0, 0, 0, v, 0)
sol = odeint(dS_dt, S0, t)
x, y, z, vx, vy, vz = sol.T[0], sol.T[1], sol.T[2], sol.T[3], sol.T[4], sol.T[5]

fig = plt.figure()
ax1 = fig.add_subplot(121, projection="3d")
ax1.plot(x,y,z, color="red",label="Trajectory")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.grid(which="major")
ax1.grid(which="minor",linestyle="--")
ax1.minorticks_on()
ax1.legend()
ax2 = fig.add_subplot(122, projection="3d")
ax2.plot(vx,vy,vz, color="blue",label="Velocity")
ax2.set_xlabel("Vx")
ax2.set_ylabel("Vy")
ax2.set_zlabel("Vz")
ax2.grid(which="major")
ax2.grid(which="minor",linestyle="--")
ax2.minorticks_on()
ax2.legend()
fig.suptitle("For E || B: When v || E, V || B")
fig.tight_layout()
plt.show()