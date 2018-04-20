"Derivatives_Pricing"

__author__ = "Aviral (Avi) Kumar"
__date__ = '1/26/2018'
__copyright__ = 'Aviral_Kumar'

import datetime
import European_Options as EurOpt
import Binary_Options as BinOpt
import Helper_Functions as hf


def main():
    """
    Enter the current spot price , Volatility, Risk - Free Rate, Term, Strike Price, Number of Simulations, Right (Call/Put)
    """
    spot_price = 805.29
    vol = 0.2076
    rf_rate = .0014
    term = None
    strike_price = 810.0
    simulations = 90000
    market_price = 17.50
    right = "P"
    if right  == "P":
        print "The program will price put options"
    else:
        print "The program will price call options"
    term = (datetime.date.today() - datetime.date(2017,9,3)).days / 365.0
    european_option =  EurOpt.price_european_option()
    european_option.initialise(spot_price, vol, rf_rate, term,strike_price, simulations, right = right)
    european_option.calculate_price()

    binary_options = BinOpt.Binary_Options()
    binary_options.initialise(spot_price, vol, rf_rate, term,strike_price, simulations, right = right)
    price_MC = binary_options.calculate_price_MC()
    price_BS = binary_options.calculate_price_BS()
    print "The price using Monte-Carlo Simulation is %s and using Black Scholes Model is %s.\n We are only off by %s" %(price_MC, price_BS, price_BS-price_MC)

    implied_vol= hf.find_vol_newton(market_price, right, spot_price, strike_price ,term, rf_rate)
    price = hf.bs_price(right, spot_price, strike_price,term, rf_rate, implied_vol, q = 0.0)
    print "Implied Volatility : %.2f%%"%(implied_vol*100.00)
    print "Market Value : %.2f" % (market_price)
    print "Price at Implied Volatility : %.2f" %(price)


if  __name__ == "__main__":
    main()
