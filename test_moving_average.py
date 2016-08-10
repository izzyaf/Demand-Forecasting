import pandas as pd
from matplotlib import pyplot as plt

import moving_average as ma
import read_file


# --------------------------------------------------------------------------

# Parse input file
def load_data(file_name):
    # Date format
    date_format = lambda dates: pd.datetime.strptime(dates, '%b-%y')

    # Generate tshirt sales dataframe
    tshirt_raw = read_file.parse_csv_file(file_name, date_format)

    # Return dataframe
    return tshirt_raw


# --------------------------------------------------------------------------

# Moving average
def execute_ma(dataframe, file_name):
    # Generate result
    forecast_full_frame, forecast_partial_frame, rmse = ma.moving_average(dataframe=dataframe, window=3, ahead=5,
                                                                          file_name=file_name)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_moving_average.txt'
    f = open(out_file_name, 'w')

    print('Full timeframe:\n{}'.format(forecast_full_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Partial timeframe:\n{}'.format(forecast_partial_frame), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Combine dataframe
    result = pd.concat(objs=[dataframe, forecast_full_frame], axis=1)
    result.columns = ['Actual', 'Forecast']

    # Plot
    result.plot()
    plt.show()


# --------------------------------------------------------------------------

# Weighted moving average
def execute_wma(dataframe, file_name):
    # Generate result
    forecast_full_frame, forecast_partial_frame, rmse, weight = ma.weighted_moving_average(dataframe=dataframe,
                                                                                           window=3,
                                                                                           ahead=5,
                                                                                           file_name=file_name)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_weighted_moving_average.txt'
    f = open(out_file_name, 'w')

    print('Full timeframe:\n{}'.format(forecast_full_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Partial timeframe:\n{}'.format(forecast_partial_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Weight:\n{}'.format(weight), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Combine dataframe
    result = pd.concat(objs=[dataframe, forecast_full_frame], axis=1)
    result.columns = ['Actual', 'Forecast']

    # Plot
    result.plot()
    plt.show()

# --------------------------------------------------------------------------
