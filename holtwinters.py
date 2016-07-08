from __future__ import division
from statsmodels.tools import eval_measures
from pandas.tseries.offsets import *
from scipy.optimize import fmin_l_bfgs_b
import numpy as np
import pandas as pd


# --------------------------------------------------------------------------


def RMSE(params, *args):
    dataframe = args[0]
    type = args[1]  # multiplicative
    rmse = 0

    alpha, beta, gamma = params
    period_len = args[2]
    smooth = [0] * period_len
    trend = [0] * period_len
    smooth[-1] = sum(dataframe.iloc[0:period_len]) / float(period_len)
    trend[-1] = (sum(dataframe.iloc[period_len:2 * period_len]) - sum(dataframe.iloc[0:period_len])) / period_len ** 2
    forecast = []

    if type == 'multiplicative':
        season = [dataframe.iloc[i] / smooth[-1] for i in range(period_len)]

        for i in range(period_len, dataframe.count()):
            smooth.append(alpha * (dataframe.iloc[i] / season[-period_len]) + (1 - alpha) * (smooth[-1] + trend[-1]))
            trend.append(beta * (smooth[i] - smooth[-1]) + (1 - beta) * trend[-1])
            season.append(gamma * (dataframe.iloc[i] / (smooth[-1] + trend[-1])) + (1 - gamma) * season[-period_len])
            forecast.append((smooth[-1] + trend[-1]) * season[-period_len])

    else:
        exit('Type must be multiplicative')

    rmse = eval_measures.rmse(dataframe[period_len:], forecast)

    return rmse


# --------------------------------------------------------------------------


# Holt Winters Exponential Smoothing with multiplicative
def multiplicative(input_dataframe, period_len, next_periods, alpha=None, beta=None, gamma=None):
    dataframe = input_dataframe.copy()

    # Datetime format
    date_format = '%Y-%m'

    # Get size of original dataframe
    t = dataframe.count()

    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[period_len], periods=t, format=date_format, freq='MS')

    forecast = pd.Series(data=[np.nan] * len(date_range), index=date_range)

    if alpha is None or beta is None or gamma is None:
        initial_values = np.array([0.0, 1.0, 0.0])
        boundaries = [(0, 1), (0, 1), (0, 1)]
        type = 'multiplicative'

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(dataframe, type, period_len),
                                   bounds=boundaries, approx_grad=True)
        alpha, beta, gamma = parameters[0]

    smooth = [0] * period_len
    trend = [0] * period_len
    smooth[-1] = sum(dataframe.iloc[0:period_len]) / float(period_len)
    trend[-1] = (sum(dataframe.iloc[period_len:2 * period_len]) - sum(dataframe.iloc[0:period_len])) / period_len ** 2
    season = [dataframe.iloc[i] / smooth[-1] for i in range(period_len)]

    rmse = 0

    for i in range(period_len, t + next_periods):
        if i >= t:
            T = i - t
            forecast.iloc[i - period_len] = (smooth[t - 1] + T * trend[t - 1]) * season[i - period_len]
        else:
            smooth.append(alpha * (dataframe[i] / season[-period_len]) + (1 - alpha) * (smooth[-1] + trend[-1]))
            trend.append(beta * (smooth[i] - smooth[-1]) + (1 - beta) * trend[-1])
            season.append(gamma * (dataframe[i] / (smooth[-1] + trend[-1])) + (1 - gamma) * season[-period_len])
            forecast.iloc[i - period_len] = (smooth[-1] + trend[-1]) * season[-period_len]

    rmse = eval_measures.rmse(dataframe[period_len:], forecast[:-period_len])

    return forecast, alpha, beta, gamma, rmse

# --------------------------------------------------------------------------
