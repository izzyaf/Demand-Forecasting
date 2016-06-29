from fractions import Fraction
from statsmodels.tools import eval_measures
import numpy as np
import pandas as pd


# --------------------------------------------------------------------------

def moving_average(dataframe, window, ahead, file_name):
    # Datetime format
    date_format = '%b-%y'

    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[0], periods=dataframe.count() + ahead, format=date_format,
                               freq='MS')

    # Create new dataframe for forecasting
    forecast_full_frame = pd.Series(data=[np.nan] * (len(date_range)), index=date_range)

    # Begin forecasting
    for idx in range(window, len(forecast_full_frame.index)):
        # Estimation of actual data
        if idx < dataframe.count():
            forecast_full_frame.iloc[idx] = round(
                np.mean([dataframe.iloc[idx - i] for i in range(1, window + 1)]))
        # Calculation of future data
        else:
            forecast_full_frame.iloc[idx] = round(
                np.mean([forecast_full_frame.iloc[idx - i] for i in range(1, window + 1)]))

    # Drop all NaN values
    forecast_full_frame.dropna(inplace=True)

    # Future timeframe only
    forecast_partial_frame = forecast_full_frame[~forecast_full_frame.index.isin(dataframe.index)]

    # Root mean squared error
    rmse = eval_measures.rmse(dataframe[window:dataframe.count()], forecast_full_frame[:dataframe.count() - window])

    # Return result
    return forecast_full_frame, forecast_partial_frame, rmse


# --------------------------------------------------------------------------

def weighted_moving_average(dataframe, window, ahead, file_name):
    # Datetime format
    date_format = '%b-%y'

    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[0], periods=dataframe.count() + ahead, format=date_format,
                               freq='MS')

    # Create new dataframe for forecasting
    forecast_full_frame = pd.Series(data=[np.nan] * (len(date_range)), index=date_range)

    # Init weights
    weight_array = []
    for i in range(1, window + 1):
        weight_array.append(Fraction(i * 2, pow(window, 2) + window))

    # Begin forecasting
    for idx in range(window, len(forecast_full_frame.index)):
        # Estimation of actual data
        if idx < len(dataframe.index):
            forecast_full_frame.iloc[idx] = round(
                np.sum([dataframe.iloc[idx - i] * float(weight_array[window - i]) for i in range(1, window + 1)]))
        # Calculation of future data
        else:
            forecast_full_frame.iloc[idx] = round(
                np.sum([forecast_full_frame.iloc[idx - i] * float(weight_array[window - i]) for i in
                        range(1, window + 1)]))

    # Drop all NaN values
    forecast_full_frame.dropna(inplace=True)

    # Future timeframe only
    forecast_partial_frame = forecast_full_frame[~forecast_full_frame.index.isin(dataframe.index)]

    # Root mean squared error
    rmse = eval_measures.rmse(dataframe[window:dataframe.count()], forecast_full_frame[:dataframe.count() - window])

    # Return result
    return forecast_full_frame, forecast_partial_frame, rmse

# --------------------------------------------------------------------------
