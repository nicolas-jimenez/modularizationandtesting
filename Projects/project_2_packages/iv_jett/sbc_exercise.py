import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import scipy.optimize as opt
from collections import namedtuple
from functools import partial
MarketParams = namedtuple(
    "MarketParams",
    [
        "alpha", "delta", "gamma", "psi",
        "xi_d", "xi_s", "z"
    ]
)
def unpack(market):
    return (
        market.alpha, market.delta, market.gamma, market.psi,
        market.xi_d, market.xi_s, market.z
    )
def draw_params():
    alpha = st.norm(12.0, 2.0).rvs()
    delta_d = -st.lognorm(1.0, scale=np.exp(0.0)).rvs()
    gamma = st.norm(0.0, 0.5).rvs()
    psi = st.lognorm(0.5, scale=np.exp(0.0)).rvs()
    xi_d = 0.5*np.random.randn()
    xi_s = 0.5*np.random.randn()
    z = xi_s + 0.20*np.random.randn()
    return MarketParams(alpha, delta_d, gamma, psi, xi_d, xi_s, z)
def create_markets(nmarkets):
    return [draw_params() for i in range(nmarkets)]
def quantities(p, market):
    # Unpack parameters
    alpha, delta_d, gamma, psi, xi_d, xi_s, z = unpack(market)
    # Compute quantities
    q_d = alpha + delta_d*p + xi_d
    q_s = gamma + psi*p + xi_s
    return q_d, q_s
def excess_supply(p, market):
    q_d, q_s = quantities(p, market)
    return q_s - q_d
def find_equilibrium(market):
    solveme = partial(excess_supply, market=market)
    pstar = opt.bisect(solveme, 0.0001, 250.0)
    return pstar
nmarkets = 50
markets = create_markets(nmarkets)
demand_shocks = [market.xi_d for market in markets]
equilibrium_prices = [find_equilibrium(market) for market in markets]
equilibrium_qs = [
    quantities(equilibrium_prices[i], markets[i])[0] for i in range(nmarkets)
]
equilibrium_qs = [
    quantities(equilibrium_prices[i], markets[i])[1] for i in range(nmarkets)
]






