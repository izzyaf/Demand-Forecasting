import numpy as np
import pandas as pd
from scipy.optimize import fmin_l_bfgs_b
from statsmodels.tools import eval_measures


# -------------------------------------------------

def RMSE(params, *args):
    data_frame = args[0]
    alpha = params

    rmse = 0

    forecast = [0] * len(data_frame)

    forecast[1] = data_frame[0]

    for index in range(2, len(data_frame)):
        forecast[index] = alpha * data_frame[index - 1] + (1 - alpha) * forecast[index - 1]

    rmse = eval_measures.rmse(forecast[1:], data_frame[1:])

    return rmse


# -------------------------------------------------
def prepare(dataframe):
    non_zero_demand = []
    # inter-arrival between two non-demand
    q = []

    # mapping between dataframe index and non_zero_demand index
    map = []

    for i in range(dataframe.count()):
        if dataframe.iloc[i] != 0:
            non_zero_demand.append(dataframe.iloc[i])
            q.append(i + 1)
            map.append(i)

    # calculate q
    for i in reversed(range(1, len(q))):
        q[i] = q[i] - q[i - 1]

    return non_zero_demand, q, map


# -------------------------------------------------
def croston_method(dataframe, next_periods, alpha=None):
    # Datetime format
    date_format = '%Y-%m'

    # Get size of original dataframe
    size = dataframe.count()

    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[0], periods=size + next_periods, format=date_format, freq='MS')

    # Create new dataframe for forecasting
    forecast_full_frame = pd.Series(data=[0] * (len(date_range)), index=date_range)

    # prepare non-zero demand
    non_zero_demand, q, map = prepare(dataframe)

    # n-th non-zero demand
    n = len(q)

    forecast_non_zero_demand = [0] * n
    inter_arrival = [0] * n

    if alpha is None:
        initial_values = np.array([0.0])
        boundaries = [(0, 1)]

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(non_zero_demand, next_periods), bounds=boundaries,
                                   approx_grad=True)
        alpha = parameters[0]

    forecast_non_zero_demand[1] = non_zero_demand[0]
    inter_arrival[1] = q[0]

    for i in range(2, n):
        forecast_non_zero_demand[i] = alpha * non_zero_demand[i - 1] + (1 - alpha) * forecast_non_zero_demand[i - 1]
        inter_arrival[i] = alpha * q[i - 1] + (1 - alpha) * inter_arrival[i - 1]

    # predict values
    for i in range(n):
        forecast_full_frame.iloc[map[i]] = forecast_non_zero_demand[i]

    # forecast new values
    for i in range(size, size + next_periods):
        forecast_full_frame.iloc[i] = forecast_non_zero_demand[n - 1] / inter_arrival[n - 1]

    rmse = eval_measures.rmse(non_zero_demand[1:], forecast_non_zero_demand[1:])

    return forecast_full_frame, forecast_full_frame[-next_periods:], rmse, alpha
