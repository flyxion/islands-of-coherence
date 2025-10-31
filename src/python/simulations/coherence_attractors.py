import matplotlib.pyplot as plt
from rsvp_core.fields import RSVPFields

params = {'c_phi': 0.5, 'lambda_v': 2.0, 'kappa': 1.0, 'beta': 0.5, 'gamma': 0.05}
fields = RSVPFields((100, 100), params)
lyap_history = []

for t in range(1000):
    fields.update(dt=0.01)
    lyap_history.append(fields.lyapunov())
    if t % 100 == 0:
        print(f"Step {t}: Lyapunov = {lyap_history[-1]:.4f}")

plt.plot(lyap_history)
plt.xlabel('Time Steps')
plt.ylabel('Lyapunov Functional')
plt.title('Coherence Attractor Convergence')
plt.savefig('../../docs/figures/lyapunov_convergence.png')
plt.show()
