"Derivatives_Pricing"

__author__ = "Aviral (Avi) Kumar"
__date__ = '1/26/2018'
__copyright__ = 'Aviral_Kumar'

import datetime
from random import gauss
from math import exp, sqrt, log
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm

" Common Function Go Here"
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

"    END     "


class price_european_call(object):
    """
    This class computes the price of a Vanilla Call/Put option.
    """

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
            result.append((S_T, call_payoff(S_T, self.k)))

        """
        Let us convert this into a Dataframe to plot the Price vs Payoff
        """
        df = pd.DataFrame(data = result, columns= ['Price','Call_Payoff'])
        print df.head()
        df.plot(x = 'Price',y = 'Call_Payoff', style = 'o')
        plt.show()
        price = discount_factor * (sum(df['Call_Payoff']) / float(self.simulations))
        print "The price of the European Call Option is % .4f" %(price)


class Binary_Options(object):
    """
    A binary option (all-or-nothing or digital option) is an option where the payoff is either some amount or nothing at all. The payoff is, usually, a fixed amount
    or the value of the asset.
    """


    def initialise(self , spot_price, vol, risk_free_rate, term, strike_price, simulations):
        self.S = spot_price
        self.vol = vol
        self.r = risk_free_rate
        self.T = term
        self.k = strike_price
        self.simulations = simulations

    def calculate_price_MC(self):
        result = []
        payoffs = 0.0
        discount_factor = exp(-(self.r) * self.T)
        for i in range(self.simulations):
            S_T = generate_asset_prices(self.S, self.vol, self.r, self.T)
            payoffs = binary_call_payoff(S_T, self.k)
            result.append((S_T,payoffs))

        """
        Let us convert th is into a Dataframe to plot the Price vs Payoff
        """
        df = pd.DataFrame(data=result, columns=['Price', 'Binary_Payoff'])
        print df.head()
        df = df.sort_values('Price', ascending = True)
        df.plot(x='Price', y='Binary_Payoff', style='o')
        plt.show()
        price = discount_factor * (sum(df['Binary_Payoff'])/ float(self.simulations))
        print "The price of the Binary Option is % .4f" % (price)
        return price

    def calculate_price_BS(self):
        d2 = (log(self.S/ self.k) + (self.r - 0.5*self.vol**2) * self.T) / self.vol*sqrt(self.T)
        price =  exp(-self.r * self.T) * norm.cdf(d2)
        return price

if  __name__ == "__main__":

    """
    Enter the current spot price , Volatility, Risk - Free Rate, Term, Strike Price, Number of Simulations
    """
    term = (datetime.date(2013,9,21) - datetime.date(2013,9,3)).days / 365.0

    # european_call =  price_european_call()
    # european_call.initialise(857.29, 0.2076, 0.0014, term, 860.0, 90000)
    # european_call.calculate_price()

    binary_options = Binary_Options()
    binary_options.initialise(857.29, 0.2076, 0.0014, term, 860.0, 900000)
    price_MC = binary_options.calculate_price_MC()
    price_BS = binary_options.calculate_price_BS()
    print "The price using Monte-Carlo Simulation is %s and using Black Scholes Model is %s.\n We are only off by %s" %(price_MC, price_BS, price_BS-price_MC)