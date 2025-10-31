import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# CLIO-HYDRA Demo
n_agents = 3
kappa, beta = 1.0, 0.5
dt, steps = 0.05, 50

Phi = np.array([[0,0], [3,1], [-1,2]], dtype=float)
history = [Phi.copy()]

for _ in range(steps):
    Phi_mean = Phi.mean(axis=0)
    dPhi = -kappa * (Phi - Phi_mean)
    Phi += dPhi * dt
    history.append(Phi.copy())

history = np.array(history)

# Setup plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-4, 4)
ax.set_ylim(-2, 4)
scats = [ax.plot([], [], 'o', ms=12)[0] for _ in range(n_agents)]
lines = [ax.plot([], [], 'r--')[0] for _ in range(3)]

def init():
    for s in scats:
        s.set_data([], [])
    for l in lines:
        l.set_data([], [])
    return scats + lines

def update(frame):
    for i, s in enumerate(scats):
        s.set_data([history[frame, i, 0]], [history[frame, i, 1]])
    for i, l in enumerate(lines):
        a, b = i, (i+1)%3
        l.set_data(
            [history[frame, a, 0], history[frame, b, 0]],
            [history[frame, a, 1], history[frame, b, 1]]
        )
    ax.set_title(f"Step {frame}")
    return scats + lines

ani = FuncAnimation(fig, update, frames=len(history), init_func=init, interval=200, blit=True)

output_dir = "../../output/figures"
os.makedirs(output_dir, exist_ok=True)
ani.save(f"{output_dir}/clio_hydra_demo.gif", writer='pillow', fps=10)
plt.close()
print("Saved: clio_hydra_demo.gif")
