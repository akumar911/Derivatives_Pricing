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
    Enter the current spot price , Volatility, Risk - Free Rate, Term, Strike Price, Number of Simulations, Right (Call/Put)
    """
    right = "P"
    if right  == "P":
        print "The program will price put options"
    else:
        print "The program will price call options"
    term = (datetime.date.today() - datetime.date(2017,9,3)).days / 365.0
    european_option =  EurOpt.price_european_option()
    european_option.initialise(805.29, 0.2076, 0.0014, term, 810.0, 90000, right = right)
    european_option.calculate_price()

    binary_options = BinOpt.Binary_Options()
    binary_options.initialise(800.29, 0.2076, 0.0014, term, 810.0, 900000, right = right)
    price_MC = binary_options.calculate_price_MC()
    price_BS = binary_options.calculate_price_BS()
    print "The price using Monte-Carlo Simulation is %s and using Black Scholes Model is %s.\n We are only off by %s" %(price_MC, price_BS, price_BS-price_MC)