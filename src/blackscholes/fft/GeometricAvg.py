import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../..")
from blackscholes.fft.Conv import ConvEuro
import numpy as np
from scipy.stats.mstats import gmean

class Euro:

    def __init__(self, strike, S0_vec, T, ir, vol, dividend, corr, cp_type):
        dim = len(S0_vec)
        vol_vec = np.full(dim, vol)
        dividend_vec = np.full(dim, dividend)
        corr_mat = np.full((dim, dim), corr)
        np.fill_diagonal(corr_mat, 1)
        payoff_func = lambda x: np.maximum(cp_type*(gmean(x, axis=1) - strike), 0)
        self.solver = ConvEuro(payoff_func, S0_vec, T, ir, vol_vec, dividend_vec, corr_mat)
        self.price_mat = None
    
    def price(self, n_vec):
        self.price_mat = self.solver.price(n_vec)
        return self.price_mat

    def greeks(self):
        return self.solver.greeks()