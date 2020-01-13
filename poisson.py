import numpy as np


def poisson(k, userlam):
    prob = np.power(userlam, k)*np.exp(-userlam)/np.math.factorial(k)
    return round(prob,3)

mean = float(input())
user_k = float(input())
print(poisson(user_k, mean))