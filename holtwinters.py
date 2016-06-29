from __future__ import division
from pandas.tseries.offsets import *
from scipy.optimize import fmin_l_bfgs_b
import numpy as np
import pandas as pd


# --------------------------------------------------------------------------

# def RMSE(params, *args):
#     Y = args[0]
#     type = args[1]  # multiplicative
#     rmse = 0
#
#     alpha, beta, gamma = params
#     m = args[2]
#     a = [sum(Y[0:m]) / float(m)]
#     b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]
#     y = []
#
#     if type == 'multiplicative':
#         s = [Y[i] / a[0] for i in range(m)]
#         y = [(a[0] + b[0]) * s[0]]
#
#         for i in range(len(Y)):
#             a.append(alpha * (Y[i] / s[i]) + (1 - alpha) * (a[i] + b[i]))
#             b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
#             s.append(gamma * (Y[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
#             y.append((a[i + 1] + b[i + 1]) * s[i + 1])
#
#     else:
#         exit('Type must be multiplicative')
#
#     rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y, y[:-1])]) / len(Y))
#
#     return rmse

def RMSE(params, *args):
    dataframe = args[0]
    type = args[1]  # multiplicative
    rmse = 0

    alpha, beta, gamma = params
    m = args[2]
    a = [sum(dataframe.iloc[0:m]) / float(m)]
    b = [(sum(dataframe.iloc[m:2 * m]) - sum(dataframe.iloc[0:m])) / m ** 2]
    y = []

    if type == 'multiplicative':
        s = [dataframe.iloc[i] / a[0] for i in range(m)]
        y = [(a[0] + b[0]) * s[0]]

        for i in range(dataframe.count()):
            a.append(alpha * (dataframe.iloc[i] / s[i]) + (1 - alpha) * (a[i] + b[i]))
            b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
            s.append(gamma * (dataframe.iloc[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
            y.append((a[i + 1] + b[i + 1]) * s[i + 1])

    else:
        exit('Type must be multiplicative')

    rmse = np.sqrt(sum([(m - n) ** 2 for m, n in zip(dataframe, y[:-1])]) / dataframe.count())

    return rmse


# # Holt Winters Exponential Smoothing with multiplicative
# def multiplicative(x, m, fc, alpha=None, beta=None, gamma=None):
#     Y = x[:]
#     y = []
#
#     if alpha is None or beta is None or gamma is None:
#         initial_values = array([0.0, 1.0, 0.0])
#         boundaries = [(0, 1), (0, 1), (0, 1)]
#         type = 'multiplicative'
#
#         parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(Y, type, m),
#                                    bounds=boundaries, approx_grad=True)
#         alpha, beta, gamma = parameters[0]
#
#         a = [sum(Y[0:m]) / float(m)]
#         b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]
#         s = [Y[i] / a[0] for i in range(m)]
#         y = [(a[0] + b[0]) * s[0]]
#         rmse = 0
#
#         t = len(Y)
#         for i in range(t + fc):
#             if i >= t:
#                 T = i - t
#                 Y.append((a[t - 1] + T * b[t - 1]) * s[i + T - m])
#             else:
#                 a.append(alpha * (Y[i] / s[-m]) + (1 - alpha) * (a[i] + b[i]))
#                 b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
#                 s.append(gamma * (Y[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
#                 y.append((a[i + 1] + b[i + 1]) * s[i + 1])
#
#     rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))
#
#     return Y[-fc:], alpha, beta, gamma, rmse, y

# --------------------------------------------------------------------------

# Holt Winters Exponential Smoothing with multiplicative
def multiplicative(x, m, fc, alpha=None, beta=None, gamma=None):
    dataframe = x.copy()
    y = pd.Series(data=np.nan, index=[dataframe.index[dataframe.count() - 1] + DateOffset(months=1)])

    if alpha is None or beta is None or gamma is None:
        initial_values = np.array([0.0, 1.0, 0.0])
        boundaries = [(0, 1), (0, 1), (0, 1)]
        type = 'multiplicative'

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(dataframe, type, m),
                                   bounds=boundaries, approx_grad=True)
        alpha, beta, gamma = parameters[0]

        a = [sum(dataframe[0:m]) / float(m)]
        b = [(sum(dataframe[m:2 * m]) - sum(dataframe[0:m])) / m ** 2]
        s = [dataframe.iloc[i] / a[0] for i in range(m)]
        y[0] = (a[0] + b[0]) * s[0]
        rmse = 0

        t = dataframe.count()
        for i in range(t + fc):
            if i >= t:
                T = i - t
                dataframe.append(pd.Series(data=(a[t - 1] + T * b[t - 1]) * s[i + T - m],
                                           index=[dataframe.index[dataframe.count() - 1] + DateOffset(months=1)]))
            else:
                a.append(alpha * (dataframe[i] / s[-m]) + (1 - alpha) * (a[i] + b[i]))
                b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
                s.append(gamma * (dataframe[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
                y.append(pd.Series(data=(a[i + 1] + b[i + 1]) * s[i + 1],
                                   index=[y.index[y.count() - 1] + DateOffset(months=1)]))

    rmse = np.sqrt(sum([(m - n) ** 2 for m, n in zip(dataframe[:-fc], y[:-fc - 1])]) / len(dataframe.iloc[:-fc]))

    return dataframe.iloc[-fc:], alpha, beta, gamma, rmse, y

# --------------------------------------------------------------------------
