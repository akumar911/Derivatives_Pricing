import numpy as np
from math import sqrt, pi , log, e
from enum import Enum
import scipy.stats as stat
from scipy.stats import norm
import time

class BSMetron:
    def __init__(self,asset_price, vol, strike, risk_free, dividend_continuous_rate ,term, right):
        self.right = right
        self.S = asset_price
        self.k = strike
        self.r = risk_free
        self.q = dividend_continuous_rate
        self.t = term
        self.sigma = vol
        self.sigmaT = self.sigma * self.t ** 0.5
        self.d1 =