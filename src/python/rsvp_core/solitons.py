import numpy as np

class AbelianVortex:
    def __init__(self, grid_size=200, L=20, v0=1.0, g=1.0, xi=1.0):
        self.N = grid_size
        self.L = L
        r = np.linspace(0.1, L, grid_size)
        phi = np.linspace(0, 2*np.pi, grid_size)
        self.R, self.Phi = np.meshgrid(r, phi)
        self.X = self.R * np.cos(self.Phi)
        self.Y = self.R * np.sin(self.Phi)

        self.v0, self.g, self.xi = v0, g, xi
        self.f = lambda r: 1 - np.exp(-r/xi)
        self.h = lambda r: np.exp(-r/xi)

    def build(self):
        Phi_mag = self.v0 * self.f(self.R)
        Phi_phase = self.Phi
        Phi_complex = Phi_mag * np.exp(1j * Phi_phase)

        A_phi = (1 - self.h(self.R)) / (self.g * self.R + 1e-12)
        A_x = -A_phi * np.sin(self.Phi)
        A_y = A_phi * np.cos(self.Phi)

        return Phi_complex, (A_x, A_y), Phi_mag

class Monopole:
    def __init__(self, R_max=15, N=100):
        self.r = np.linspace(0.1, R_max, N)
        self.H = 1 - np.exp(-self.r)
        self.K = np.exp(-self.r)
