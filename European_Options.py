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
import Helper_Functions as hf

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
            S_T = hf.generate_asset_prices(self.S, self.vol, self.r, self.T)
            result.append((S_T, hf.call_payoff(S_T, self.k)))

        """
        Let us convert this into a Dataframe to plot the Price vs Payoff
        """
        df = pd.DataFrame(data = result, columns= ['Price','Call_Payoff'])
        print df.head()
        df.plot(x = 'Price',y = 'Call_Payoff', style = 'o')
        plt.show()
        price = discount_factor * (sum(df['Call_Payoff']) / float(self.simulations))
        print "The price of the European Call Option is % .4f" %(price)

