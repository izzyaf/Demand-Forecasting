from statsmodels.tools import eval_measures
import numpy as np
import pandas as pd


# --------------------------------------------------------------------------


def simple_exponential_smoothing(dataframe, ahead, alpha, file_name):
    # Datetime format
    date_format = '%b-%y'

    # Get size of original dataframe
    size = dataframe.count()

    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[0], periods=size + ahead, format=date_format,
                               freq='MS')

    # Create new dataframe for forecasting
    forecast_full_frame = pd.Series(data=[np.nan] * (len(date_range)), index=date_range)

    # Begin forecasting
    for idx in range(len(forecast_full_frame.index) - 1):
        if idx == 0:
            forecast_full_frame.iloc[idx + 1] = dataframe.iloc[idx]
        elif idx < size:
            forecast_full_frame.iloc[idx + 1] = alpha * dataframe.iloc[idx] + (1 - alpha) * forecast_full_frame.iloc[
                idx]
        else:
            forecast_full_frame.iloc[idx + 1] = forecast_full_frame.iloc[idx]

    # Drop all NaN values
    forecast_full_frame.dropna(inplace=True)

    # Future timeframe only
    forecast_partial_frame = forecast_full_frame[~forecast_full_frame.index.isin(dataframe.index)]

    # Root mean squared error
    rmse = eval_measures.rmse(dataframe[1:size], forecast_full_frame[0:size - 1])

    # Return result
    return forecast_full_frame, forecast_partial_frame, rmse

# --------------------------------------------------------------------------
