import sympy as sp

class Lagrangian:
    """Symbolic RSVP Lagrangian with gauge extension."""
    def __init__(self):
        self.t, self.x, self.y = sp.symbols('t x y')
        self.Phi = sp.Function('Phi')(self.x, self.y, self.t)
        self.vx = sp.Function('v_x')(self.x, self.y, self.t)
        self.vy = sp.Function('v_y')(self.x, self.y, self.t)
        self.S = sp.Function('S')(self.x, self.y, self.t)
        self.A0 = sp.Function('A_0')(self.x, self.y, self.t)
        self.Ax = sp.Function('A_x')(self.x, self.y, self.t)
        self.Ay = sp.Function('A_y')(self.x, self.y, self.t)

        self.c_phi, self.lambda_v = sp.symbols('c_phi lambda_v')
        self.kappa, self.beta, self.gamma = sp.symbols('kappa beta gamma')

    def unitary(self):
        L = (
            0.5 * sp.diff(self.Phi, self.t)**2 -
            0.5 * self.c_phi**2 * (sp.diff(self.Phi, self.x)**2 + sp.diff(self.Phi, self.y)**2) +
            0.5 * self.lambda_v * (self.vx**2 + self.vy**2) -
            0.5 * self.gamma * self.S**2 -
            self.kappa * self.Phi * (sp.diff(self.vx, self.x) + sp.diff(self.vy, self.y)) +
            self.beta * self.S * (sp.diff(self.vx, self.x) + sp.diff(self.vy, self.y))
        )
        return L

    def gauge_invariant(self):
        g = sp.symbols('g')
        D_t = sp.diff(self.Phi, self.t) - sp.I * g * self.A0 * self.Phi
        D_x = sp.diff(self.Phi, self.x) - sp.I * g * self.Ax * self.Phi
        D_y = sp.diff(self.Phi, self.y) - sp.I * g * self.Ay * self.Phi
        F_xy = sp.diff(self.Ay, self.x) - sp.diff(self.Ax, self.y)

        L = (
            sp.conjugate(D_t) * D_t -
            0.5 * self.c_phi**2 * (sp.conjugate(D_x)*D_x + sp.conjugate(D_y)*D_y) +
            0.5 * self.lambda_v * ((self.vx - self.Ax/self.lambda_v)**2 + (self.vy - self.Ay/self.lambda_v)**2) -
            0.5 * self.gamma * self.S**2 -
            0.25 * F_xy**2
        )
        return L.simplify()
