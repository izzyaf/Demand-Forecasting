import pandas as pd
from pandas.tseries.offsets import *


# --------------------------------------------------------------------------

# input are series of data, alpha and beta. Output is result data after forecast
def double_exponential_smoothing(series, alpha, beta):
    # result = [series[0]]
    # for n in range(1, len(series) + 1):
    #     if n == 1:
    #         level, trend = series[0], series[1] - series[0]
    #     if n >= len(series):  # we are forecasting
    #         value = result[-1]
    #     else:
    #         value = series[n]
    #     last_level, level = level, alpha * value + (1 - alpha) * (level + trend)
    #     trend = beta * (level - last_level) + (1 - beta) * trend
    #     result.append(level + trend)
    # return result

    result = series.copy()
    for n in range(1, result.count() + 1):
        if n == 1:
            level, trend = series.iloc[0], series.iloc[1] - series.iloc[0]
        if n >= series.count():  # we are forecasting
            value = result.iloc[-1]
        else:
            value = series.iloc[n]
        last_level, level = level, alpha * value + (1 - alpha) * (level + trend)
        trend = beta * (level - last_level) + (1 - beta) * trend
        result.append(pd.Series(data=level + trend, index=[result.index[result.count() - 1] + DateOffset(months=1)]))
    return result

# --------------------------------------------------------------------------
