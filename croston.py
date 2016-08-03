from statsmodels.tools import eval_measures
from scipy.optimize import fmin_l_bfgs_b
import numpy as np
import pandas as pd


# -------------------------------------------------


def croston_method(dataframe, next_periods, alpha=None):
    # Datetime format
    date_format = '%Y-%m'

    # Get size of original dataframe
    size = dataframe.count()

    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[0], periods=size + next_periods, format=date_format, freq='MS')

    # Create new dataframe for forecasting
    forecast_full_frame = pd.Series(data=[np.nan] * (len(date_range)), index=date_range)

    if alpha is None:
        alpha = 0.3

    # Estimate of intervals between demands
    X = [0] * size
    # count number of zero-demand
    q = 2
    last_period_non_zero = 0

    # Init values
    if dataframe.iloc[0] == 0:
        forecast_full_frame.iloc[0] = 1
        X[0] = 2
    else:
        forecast_full_frame.iloc[0] = dataframe.iloc[0]
        X[0] = 1
        q = 1
        last_period_non_zero = 1

    # predict values
    for i in range(1, size):
        if dataframe.iloc[i] == 0:
            q += 1
            forecast_full_frame.iloc[i] = forecast_full_frame.iloc[i - 1]
            X[i] = X[i - 1]
        else:
            forecast_full_frame.iloc[i] = (1 - alpha) * forecast_full_frame.iloc[i - 1] + alpha * dataframe.iloc[i]
            X[i] = (1 - alpha) * X[i - 1] + alpha * q
            q = 1
            last_period_non_zero = i

    # forecast new values
    for i in range(size, size + next_periods):
        forecast_full_frame.iloc[i] = forecast_full_frame.iloc[last_period_non_zero] / X[last_period_non_zero]

    rmse = eval_measures.rmse(dataframe, forecast_full_frame[0:size])

    return forecast_full_frame, forecast_full_frame[-next_periods:], rmse