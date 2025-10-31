import numpy as np
import matplotlib.pyplot as plt
from rsvp_core.solitons import Monopole
import os

mono = Monopole(R_max=12, N=120)
r = mono.r
H, K = mono.H, mono.K

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(r, H, 'b-', label='$H(r)$ — Higgs')
ax1.plot(r, K, 'r-', label='$K(r)$ — Gauge')
ax1.set_xlabel('Radius $r$')
ax1.set_ylabel('Profile')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_title('Monopole Core')

ax2.plot(r, (1 - K)/r**2, 'k-', lw=2)
ax2.set_xlabel('Radius $r$')
ax2.set_ylabel('$B \\sim 1/r^2$')
ax2.set_title('Magnetic Field')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
output_dir = "../../output/figures"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f"{output_dir}/monopole_profile.png", dpi=300)
plt.show()
