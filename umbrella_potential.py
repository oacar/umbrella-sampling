import numpy as _np

class UmbrellaPotential(object):
    def __init__(self, center, spring_constant):
        self.center = center
        self.spring_constant = spring_constant
        self.effective_center = None
        self.effective_spring_constant = None
    def add_trajectory(self, trajectory):
        self.effective_center = _np.mean(trajectory)
        self.effective_spring_constant = 1.0 / _np.var(trajectory, ddof=1)
    @property
    def center_correction(self):
        if self.effective_center is None:
            return None
        return self.center - self.effective_center
    @property
    def slope(self):
        if self.effective_center is None:
            return None
        return self.spring_constant * self.center_correction
