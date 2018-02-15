"Derivatives_Pricing"

__author__ = "Aviral (Avi) Kumar"
__date__ = '1/26/2018'
__copyright__ = 'Aviral_Kumar'

import datetime
import European_Options as EurOpt
import Binary_Options as BinOpt
import Helper_Functions as hf



if  __name__ == "__main__":

    """
    Enter the current spot price , Volatility, Risk - Free Rate, Term, Strike Price, Number of Simulations
    """
    term = (datetime.date(2013,9,21) - datetime.date(2013,9,3)).days / 365.0

    european_call =  EurOpt.price_european_call()
    european_call.initialise(857.29, 0.2076, 0.0014, term, 860.0, 90000)
    european_call.calculate_price()

    binary_options = BinOpt.Binary_Options()
    binary_options.initialise(857.29, 0.2076, 0.0014, term, 860.0, 900000)
    price_MC = binary_options.calculate_price_MC()
    price_BS = binary_options.calculate_price_BS()
    print "The price using Monte-Carlo Simulation is %s and using Black Scholes Model is %s.\n We are only off by %s" %(price_MC, price_BS, price_BS-price_MC)