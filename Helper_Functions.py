"Derivatives_Pricing"
"Copyright Aviral_Kumar"
__author__ = "Aviral (Avi) Kumar"
__date__ = '2/15/2018'
__copyright__ = 'Aviral (Avi) Kumar'



from random import gauss
from math import exp, sqrt, log
from matplotlib import pyplot as plt
from scipy.stats import norm
N = norm.cdf
n = norm.pdf
import pandas as pd
import csv
import requests
import re
import datetime as dt

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

def binary_put_payoff(S_T, K):
    """
        Since it is a Binary Option, we will
        :param S_T: The simulated stock price
        :param K: The given strike price
        :return:
        """
    if S_T <= K:
        return 1.0
    else:
        return 0.0

def bs_price(right, spot_price, strike_price, time_to_exp, rate, sigma, q = 0.0):

    d1 = (log(spot_price/strike_price) + (rate + sigma*sigma/2.)*time_to_exp)/(sigma * sqrt(time_to_exp))
    d2 = d1 - sigma*sqrt(time_to_exp)
    if right == 'C':
        price = spot_price*exp(-q * time_to_exp)* N(d1) - strike_price*exp(-rate*time_to_exp) * N(d2)
    else:
        price = strike_price*exp(-rate*time_to_exp)* N(-d2) - spot_price*exp(-q*time_to_exp)*N(-d1)
    return price

def bs_vega(right, spot_price, strike_price, time_to_exp, rate, sigma , q = 0.0):
    d1 = (log(spot_price/ strike_price)  + (rate + sigma*sigma/2.)*time_to_exp)/ (sigma*sqrt(time_to_exp))
    return spot_price * sqrt(time_to_exp) * n(d1)



def find_vol_newton(target_value, right, spot_price, strike_price, time_to_exp, rate):
    '''
    This function implements the Newton Method in python and calculates the most precise Volatility value
    :param target_value:
    :param call_put:
    :param spot_price:
    :param strike_price:
    :param time_to_exp:
    :param rate:
    :return:
    '''
    iterations = 100
    precision = 0.0005
    sigma = 0.5
    for i in range(0, iterations):
        price = bs_price(right, spot_price, strike_price, time_to_exp, rate, sigma)
        vega = bs_vega(right, spot_price, strike_price, time_to_exp, rate, sigma)

        diff = target_value - price
        if abs(diff) < precision :
            return sigma
        else:
            sigma = sigma + diff/vega

    price = bs_price(right, spot_price, strike_price, time_to_exp, rate, sigma)
    return sigma

def GoogleFinanceAPI(ticker, period = 60, days = 1):
    # prefix = "http://finance.google.com/finance/info?client=ig&q="
    # url = prefix + "%s:%s"%(exchange, symbol)
    # u = urllib2.urlopen(url)
    # content = u.read().decode('utf-8')
    # print content
    url = 'http://www.google.com/finance/getprices?i={period}&p={days}d&f=d,o,h,l,c,v&df=cpct&q={ticker}'.format(ticker=ticker,
                                                                          period=period,days=days)
    page = requests.get(url)
    reader = csv.reader(page.content.splitlines())
    columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    rows = []
    times = []
    for row in reader:
        if re.match('^[a\d]', row[0]):
            if row[0].startswith('a'):
                start = dt.datetime.fromtimestamp(int(row[0][1:]))
                times.append(start)
            else:
                times.append(start + dt.timedelta(seconds=period * int(row[0])))
            rows.append(map(float, row[1:]))
    if len(rows):
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'),
                            columns=columns)
    else:
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'))

