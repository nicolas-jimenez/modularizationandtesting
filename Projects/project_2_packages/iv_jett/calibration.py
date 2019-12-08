# Calibration

import statsmodel as sm
import math
import nympy as np
import random

N = 100
k = 1
m = 1
sims = 500

random.seed(12345)
X = np.random.rand(N, k)
Z = np.random.rand(N, m)

for s in range(1,1):
	beta_hat = np.random.normal(0,2)
	sigma_hat = math.exp(np.random.normal(0,1))
	y_hat = np.random.normal(X @ beta_hat, sigma_hat)

	model = sm.OLS(y_hat, X)
	results = model.fit()
	beta_est = results.params
	cov_est = results.cov_params()

	d = np.random.multivariate_normal(beta_est, cov_est, 1000)

	for i in range(1, d.shape[1]):
		if d[0][i] < beta_hat:
			d_true = 1
		else:
			d_true = 0















