

import numpy as np
from umbrella_sampling.umbrella_potential import UmbrellaPotential
from numpy.testing import assert_almost_equal

def test_randomised_sanity_check():
    traj = np.random.rand(1000)
    center = np.mean(traj)
    spring_constant = 1.0 / np.var(traj, ddof=1)
    up = UmbrellaPotential(center, spring_constant)
    up.add_trajectory(traj)
    assert_almost_equal(up.effective_center, up.center, decimal=16)
    assert_almost_equal(up.effective_spring_constant, up.spring_constant, decimal=16)
    assert_almost_equal(up.center_correction, 0.0, decimal=16)
    assert_almost_equal(up.slope, 0.0, decimal=16)

