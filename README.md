# Derivatives_Pricing
This repository contains the derivatives pricing programs


We will see how to price derivatives using Monte-Carlo Simulations. To price an option using a MC Simulation we use a risk-neutral valuation, where the fair value for a derivative is the expected value of its future payoff. 

So basically, at any date before maturity , denoted by t, the option's value is the present value of the expectation of its payoff at maturity , T

    Ct=PV(E[max(0,ST−K)])
    Pt=PV(E[max(0,K−ST)])
    
Since we are sticking to the risk-neutral valuation method, we will assume that underlying asset is going to earn, on average, the risk free interest rate. So we just discount the payoff by that interest rate. 

    Ct=e−r(T−t)E[max(0,ST−K)]
    
We have all our variables except the ST, which is what out simulation will provide. 

To price our option, we're going to create a simulation that provides us with many observations for the final proce of the asset ST. We will just take an average of all these values and get our ST.

