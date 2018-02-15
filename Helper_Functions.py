"Derivatives_Pricing"
"Copyright Aviral_Kumar"
__author__ = "Aviral (Avi) Kumar"
__date__ = '2/15/2018'
__copyright__ = 'The Oakleaf Group, LLC.'



from random import gauss
from math import exp, sqrt, log
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm


def generate_asset_prices(S, v,r,T):
    """

    :param S: The current spot price
    :param v: The calculated volatility of the asset
    :param r: The risk free rate
    :param T: The term of option
    :return:  A stock price that is stimulated. The simulation follows a Geometric Brownian Motion
    NOTE : A geometric Brownian motion is a random process where the logarithm of the random variable follows a normal distribution.
           This type of process distributes prices over a lognormal distribution.
    """
    return S * exp((r - 0.5 * v ** 2) * T + v * sqrt(T) * gauss(0,1.0))


def call_payoff(S_T, K):
    """

    :param S_T: The simulated stock price
    :param K: The given strike price
    :return: payoff
    """
    return max(0.0, S_T - K)

def put_payoff(S_T, K):
    """

    :param S_T: The simulated stock price
    :param K: The given strike price
    :return: payoff
    """
    return max(K - S_T, 0.0)

def binary_call_payoff(S_T, K):
    """
    Since it is a Binary Option, we will
    :param S_T: The simulated stock price
    :param K: The given strike price
    :return:
    """
    if S_T >= K:
        return 1.0
    else :
        return 0.0

