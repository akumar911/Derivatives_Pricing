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


class Binary_Options(object):
    """
    A binary option (all-or-nothing or digital option) is an option where the payoff is either some amount or nothing at all. The payoff is, usually, a fixed amount
    or the value of the asset.
    """
    print "Welcome to the Binary Options Pricing Engine"

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
            S_T = hf.generate_asset_prices(self.S, self.vol, self.r, self.T)
            payoffs = hf.binary_call_payoff(S_T, self.k)
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