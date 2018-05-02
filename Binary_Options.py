"Derivatives_Pricing"
"Copyright Aviral_Kumar"
__author__ = "Aviral (Avi) Kumar"
__date__ = '2/15/2018'
__copyright__ = 'Aviral (Avi) Kumar'


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

    def initialise(self , spot_price, vol, risk_free_rate, term, strike_price, simulations, right):
        self.S = spot_price
        self.vol = vol
        self.r = risk_free_rate
        self.T = term
        self.k = strike_price
        self.simulations = simulations
        self.right = right
    def calculate_price_MC(self):
        result = []
        payoffs = 0.0
        discount_factor = exp(-(self.r) * self.T)
        for i in range(self.simulations):
            S_T = hf.generate_asset_prices(self.S, self.vol, self.r, self.T)
            if self.right == "C":
                payoffs = hf.binary_call_payoff(S_T, self.k)
            else:
                payoffs = hf.binary_put_payoff(S_T, self.k)
            result.append((S_T,payoffs))

        """
        Let us convert th is into a Dataframe to plot the Price vs Payoff
        """
        right = ("Call" if self.right == "C" else "Put")
        df = pd.DataFrame(data=result, columns=['Price', '%s Binary_Payoff'%right]).sort_values('Price', ascending = True)
        print df.head()
        df.plot(x='Price', y='%s Binary_Payoff'%right, style='o')
        plt.show()
        price = discount_factor * (sum(df['%s Binary_Payoff'%right])/ float(self.simulations))
        print "The price of the %s Binary Option is % .4f" % (right,price)
        return price

    def calculate_price_BS(self):
        d2 = (log(self.S/ self.k) + (self.r - 0.5*self.vol**2) * self.T) / self.vol*sqrt(self.T)
        price =  exp(-self.r * self.T) * norm.cdf(d2)
        return price