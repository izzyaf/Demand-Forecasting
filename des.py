import numpy as np
import pandas as pd
from scipy.optimize import fmin_l_bfgs_b
from statsmodels.tools import eval_measures


# --------------------------------------------------------------------------

def RMSE(params, *args):
    data_frame = args[0]
    rmse = 0

    alpha, beta = params

    # Init
    smooth, trend = data_frame.iloc[0], data_frame.iloc[1] - data_frame.iloc[0]
    forecast = pd.Series(data=[np.nan] * data_frame.count(), index=data_frame.index)
    forecast.iloc[0] = data_frame.iloc[0]

    size = data_frame.count()

    for n in range(1, size):
        last_smooth, smooth = smooth, alpha * data_frame[n] + (1 - alpha) * (smooth + trend)
        trend = beta * (smooth - last_smooth) + (1 - beta) * trend
        forecast.iloc[n] = smooth + trend

    rmse = eval_measures.rmse(data_frame, forecast)

    return rmse


def double_exponential_smoothing(series, next_periods, alpha=None, beta=None):
    # Datetime format
    date_format = '%Y-%m'

    # Get size of original dataframe
    size = series.count()

    # Create ahead-day entries in future
    date_range = pd.date_range(start=series.index[0], periods=size + next_periods, format=date_format, freq='MS')

    forecast = pd.Series(data=[np.nan] * len(date_range), index=date_range)
    forecast.iloc[0] = series.iloc[0]

    # Init
    smooth, trend = series.iloc[0], series.iloc[1] - series.iloc[0]

    # Calculate alpha, beta if it's None
    if alpha is None or beta is None:
        initial_values = np.array([0.0, 1.0])
        boundaries = [(0, 1), (0, 1)]

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(series, next_periods), bounds=boundaries,
                                   approx_grad=True)
        alpha, beta = parameters[0]

    for n in range(1, size):
        last_smooth, smooth = smooth, alpha * series[n] + (1 - alpha) * (smooth + trend)
        trend = beta * (smooth - last_smooth) + (1 - beta) * trend
        forecast.iloc[n] = smooth + trend

    for n in range(size, size + next_periods):
        m = n - size + 1
        forecast.iloc[n] = smooth + m * trend

    rmse = eval_measures.rmse(series, forecast[:-next_periods])

    return forecast, rmse, alpha, beta

# --------------------------------------------------------------------------
