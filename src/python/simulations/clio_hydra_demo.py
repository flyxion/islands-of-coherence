import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# CLIO-HYDRA Demo
n_agents = 3
kappa, beta = 1.0, 0.5
dt, steps = 0.05, 100

Phi = np.array([[0,0], [3,1], [-1,2]], dtype=float)
v = np.zeros_like(Phi)
history = [Phi.copy()]

for _ in range(steps):
    Phi_mean = Phi.mean(axis=0)
    dPhi = -kappa * (Phi - Phi_mean) - beta * v
    v -= dPhi * dt
    Phi += dPhi * dt
    history.append(Phi.copy())

history = np.array(history)

# Animation
fig, ax = plt.subplots()
scats = [ax.plot([], [], 'o', ms=12)[0] for _ in range(n_agents)]
lines = [ax.plot([], [], 'r--')[0] for _ in range(3)]

def update(frame):
    for i, s in enumerate(scats):
        s.set_data(history[frame, i])
    for i, line in enumerate(lines):
        a, b = (i, (i+1)%3)
        line.set_data([history[frame,a,0], history[frame,b,0]],
                      [history[frame,a,1], history[frame,b,1]])
    ax.set_title(f"Step {frame}")
    return scats + lines

ani = FuncAnimation(fig, update, frames=steps+1, interval=100)
output_dir = "../../output/figures"
os.makedirs(output_dir, exist_ok=True)
ani.save(f"{output_dir}/clio_hydra_demo.gif", writer='pillow', fps=15)
plt.show()
