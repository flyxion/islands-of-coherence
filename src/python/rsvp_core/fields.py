import numpy as np
from scipy.ndimage import laplace

class RSVPFields:
    def __init__(self, shape=(100, 100), params=None):
        self.shape = shape
        self.Phi = np.random.randn(*shape) * 0.1
        self.v = np.zeros((*shape, 2))  # 2D vector field
        self.S = np.ones(shape) * 0.5
        self.p = params or {
            'c_phi': 0.5, 'lambda_v': 2.0, 'kappa': 1.0,
            'beta': 0.5, 'gamma': 0.05
        }

    def laplacian(self, field):
        return laplace(field, mode='nearest')

    def gradient(self, field):
        gy, gx = np.gradient(field)
        return np.stack([gx, gy], axis=-1)  # (H, W, 2)

    def divergence(self, vec_field):
        # vec_field: (H, W, 2)
        div_x = np.gradient(vec_field[..., 0], axis=0)
        div_y = np.gradient(vec_field[..., 1], axis=1)
        return div_x + div_y  # (H, W)

    def update(self, dt=0.01):
        lap_Phi = self.laplacian(self.Phi)           # (H, W)
        div_v = self.divergence(self.v)              # (H, W)
        grad_Phi = self.gradient(self.Phi)           # (H, W, 2)
        grad_S = self.gradient(self.S)               # (H, W, 2)

        # Update Phi (scalar)
        self.Phi += dt * (self.p['c_phi']**2 * lap_Phi + self.p['kappa'] * div_v)

        # Update v (vector)
        force = grad_Phi + self.p['beta'] * grad_S
        self.v -= dt * force / self.p['lambda_v']

        # Update S (scalar)
        self.S += dt * (self.p['beta'] * div_v - self.p['gamma'] * self.S**2)

    def lyapunov(self):
        grad_Phi = self.gradient(self.Phi)
        grad_norm = np.sum(grad_Phi**2, axis=-1)
        return (
            0.5 * np.sum(grad_norm) +
            0.5 * self.p['lambda_v'] * np.sum(self.v**2) +
            0.5 * self.p['gamma'] * np.mean(self.S**2)
        )
