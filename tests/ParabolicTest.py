import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../src")
from blackscholes.pde.Parabolic import Solver1d, Coef2d, Solver2d
from blackscholes.pde.Euro import Euro1d, GeometricAvg
from blackscholes.utils.Analytical import Analytical_Sol
from utils.Domain import Domain1d, Domain2d
from blackscholes.utils.Type import CallPutType
import unittest
import numpy as np

class Test(unittest.TestCase):

    def test_Euro1d(self):
        T = 1
        domain = Domain1d(0, 6, T)
        vol, ir, dividend, strike = 0.1, 0.03, 0.01, 1
        solver = Euro1d(domain, vol, ir, dividend, strike, CallPutType.PUT)
        spot = 1
        solver.solve(400, 200)
        approx_put = solver.evaluate(spot, T)
        analytical = Analytical_Sol(spot, strike, T, ir, vol, dividend_yield=dividend)
        _, real_put = analytical.european_option_price()
        assert abs(approx_put-0.030050214069580493) < 0.00000000000001
        assert abs(approx_put-real_put)/real_put < 0.00054

    def test_geometric_avg(self):
        dim = 4
        T = 1
        domain = Domain1d(0, 100, T)
        strike = 40
        init_price_vec = np.full(4, 40)
        vol = 0.2
        ir = 0.06
        dividend = 0.04
        corr = 0.25
        solver = GeometricAvg(dim, domain, vol, ir, dividend, corr, strike, CallPutType.CALL)
        solver.solve(800, 400)
        approx = solver.evaluate(40, T)
        print(approx)

    def dtest_Solver2d(self):
        ic = lambda x, y, t: np.zeros([len(x), len(y)])
        bc = lambda x, y, t: np.ones(len(x)) if type(y) is int else np.ones(len(y))

        domain = Domain2d(0, 10, 0, 10, 1, ic, bc)
        coef_b = Coef2d(lambda s1, t: np.ones(len(s1)), lambda s2, t: np.ones(len(s2)))
        coef_a, coef_c, coef_f, coef_d, coef_e = Coef2d(), Coef2d(), Coef2d(), Coef2d(), Coef2d()
        g = lambda s1, s2, t: np.zeros(len(s1)*len(s2))
        solver = Solver2d(coef_a, coef_b, coef_c, coef_d, coef_e, coef_f, g, domain)
        solver.solve(4, 4, 1)

if __name__ == '__main__':
    unittest.main()
