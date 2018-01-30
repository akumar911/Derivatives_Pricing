"Derivatives_Pricing"

__author__ = "Aviral (Avi) Kumar"
__date__ = '1/26/2018'
__copyright__ = 'Aviral_Kumar'

import datetime
from random import gauss
from math import exp, sqrt
import pandas as pd
from matplotlib import pyplot as plt

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

    :param S_T: The stimulated stock price
    :param K: The given strike price
    :return: payoff
    """
    return max(0.0, S_T - K)

class price_european_call(object):

    def initialise(self , spot_price, vol, risk_free_rate, term, strike_price, simulations):
        self.S = spot_price
        self.vol = vol
        self.r = risk_free_rate
        self.T = term
        self.k = strike_price
        self.simulations = simulations

    def calculate_price(self):
        result = []
        discount_factor = exp(-(self.r) *self.T)
        for i in range(self.simulations):
            S_T = generate_asset_prices(self.S, self.vol, self.r, self.T)
            result.append((S_T,call_payoff(S_T, self.k)))

        """
        Let us convert this into a Dataframe to plot the Price vs Payoff
        """
        df = pd.DataFrame(data = result, columns= ['Price','Call_Payoff'])
        print df.head()
        df.plot(x = 'Price',y = 'Call_Payoff', style = 'o')
        plt.show()
        price = discount_factor * (sum(df['Call_Payoff']) / float(self.simulations))
        print "The price of the European Call Option is % .4f" %(price)


if  __name__ == "__main__":


    term = (datetime.date(2013,9,21) - datetime.date(2013,9,3)).days / 365.0
    european_call =  price_european_call()
    european_call.initialise(857.29, 0.2076, 0.0014, term, 860.0, 9000)
    european_call.calculate_price()
