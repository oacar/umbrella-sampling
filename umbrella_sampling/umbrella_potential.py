import numpy as _np
r"""UmbrellaPotential object has these attributes:
center: This is the center of umbrella potential. It should be defined while creating object
spring_constant: This is the spring constant of umbrella potential. It should be defined while creating object
effective_center: Mean value of the US trajectory.
effective_spring_constant: This is calculated with variance of the US trajectory
In order to define last two attributes an US trajectory should be given"""
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
    ##Slope of the point where the umbrella center is located
    def slope(self):
        if self.effective_center is None:
            return None
        return self.spring_constant * self.center_correction
