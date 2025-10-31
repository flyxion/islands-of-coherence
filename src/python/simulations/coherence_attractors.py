import numpy as np
import matplotlib.pyplot as plt
import os
from rsvp_core.fields import RSVPFields  # Now works!

# Setup
params = {'c_phi': 0.5, 'lambda_v': 2.0, 'kappa': 1.0, 'beta': 0.5, 'gamma': 0.05}
fields = RSVPFields((100, 100), params)
lyap_history = []

print("Running coherence attractor simulation...")
for t in range(1000):
    fields.update(dt=0.01)
    lyap_history.append(fields.lyapunov())
    if t % 200 == 0:
        print(f"Step {t}: Lyapunov = {lyap_history[-1]:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(lyap_history, 'k-', linewidth=2)
plt.title('Coherence Attractor Convergence')
plt.xlabel('Time Steps')
plt.ylabel('Lyapunov Functional $\\mathcal{V}$')
plt.grid(True, alpha=0.3)

os.makedirs('../../output/figures', exist_ok=True)
plt.savefig('../../output/figures/lyapunov_convergence.png', dpi=300)
plt.close()
print("Saved: lyapunov_convergence.png")
