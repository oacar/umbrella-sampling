

import numpy as np
from umbrella_sampling.umbrella_potential import UmbrellaPotential
from numpy.testing import assert_almost_equal
from umbrella_sampling.umbrella_iterator import UmbrellaIterator

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

def test_new_center_pos():
    givencenter=np.random.random()
    spring_const=np.random.randint(1,10)
    traj=np.random.rand(100)
    us=UmbrellaPotential(givencenter, spring_const)
    us.add_trajectory(traj)
    overlap=np.random.random()
    s=UmbrellaIterator(us, overlap)
    newcenter=us.center_correction+us.center
    s.center_check()
    assert_almost_equal(newcenter,s.umbrella.center,2)
