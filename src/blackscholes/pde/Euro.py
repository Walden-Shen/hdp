import enum
import numpy as np
from .Parabolic import Solver1d

class CallPutType(enum.IntEnum):
    CALL = 1
    PUT = -1

class Euro1d(Solver1d):
    def __init__(self, domain, vol, ir, dividend, strike, cp_type):
        """
        cp_type (call/put type): 1 if call, -1 if put
        """
        p = lambda S, t: vol**2*S**2/2
        q = lambda S, t: (ir-dividend)*S
        r = lambda S, t: -ir*np.ones(len(S))
        f = lambda S, t: 0
        domain.ic = lambda S, t: np.maximum(cp_type*(S - strike), 0)
        domain.bc = lambda S, t: strike*np.exp(-ir*t) if abs(S) < 7/3-4/3-1 else 0
        super().__init__(p, q, r, f, domain)

