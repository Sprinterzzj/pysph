from numpy import linspace, ones_like
from pysph.base.particle_array import get_particle_array

from equations import SummationDensity
from kernels import CubicSpline
from locators import AllPairLocator
from sph_eval import SPHEval

def make_particles():
    x = linspace(0, 1.0, 11); dx = x[1] - x[0]
    h = ones_like(x) * 2*dx
    m = ones_like(x) * dx
    f = get_particle_array(x=x, h=h, m=m, name = 'fluid')
    s = get_particle_array(x=x, name = 'solid')
    return [f, s]

particles = make_particles()

kernel = CubicSpline(dim=1)

equations = [SummationDensity(dest='fluid', sources=['fluid', 'solid']),
            ]            

locator = AllPairLocator()
evaluator = SPHEval(particles, equations, locator, kernel)
evaluator.compute()
    
print particles[0].rho
print particles[1].rho