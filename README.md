# Derivatives_Pricing
This repository contains the derivatives pricing programs


We will see how to price derivatives using Monte-Carlo Simulations. To price an option using a MC Simulation we use a risk-neutral valuation, where the fair value for a derivative is the expected value of its future payoff. 

So basically, at any date before maturity , denoted by t, the option's value is the present value of the expectation of its payoff at maturity , T

    Ct=PV(E[max(0,ST−K)])
    Pt=PV(E[max(0,K−ST)])
    
Since we are sticking to the risk-neutral valuation method, we will assume that underlying asset is going to earn, on average, the risk free interest rate. So we just discount the payoff by that interest rate. 

    Ct=e^(−r(T−t))E[max(0,ST−K)]
    
We have all our variables except the ST, which is what out simulation will provide. 

To price our option, we're going to create a simulation that provides us with many observations for the final proce of the asset ST. We will just take an average of all these values and get our ST.

## Extending the model 
After pricing basic European options by Monte Carlo Simulations, we can extend our model to generate prices for some exotic options. 

We will create a new class called Binary_Options to play around with thi. We can price a binary option by using the same methodology as before or we can use the B-S Model.

    C=e^(−rT)N(d2)
    
 Here N is the cumulative normal distribution function, and d2 is given by the standard Black Scholes formula.
 
 NOTE : The cumulative normal distribution function can be accessed by import norm from scipy.stats and calling the cdf function (norm.cdf('d2')).
 
 ## Calculating the Break-Even Move
Black-Scholes says that when the underlying moves by one standard deviation, your gamma profits should offset your theta losses.
This known as the break even move

### To-do : 
Write a class that for the BSM model 
Calculate the Option Greeks
