import pandas as pd
from matplotlib import pyplot as plt

import holtwinters as hw
import read_file


# --------------------------------------------------------------------------

# Parse input file
def load_data(file_name):
    # Date format
    date_format = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

    # Generate car sales dataframe
    car_raw = read_file.parse_csv_file(file_name, date_format)

    # Return dataframe
    return car_raw


# --------------------------------------------------------------------------

# Holt-Winters exponential smoothing with multiplicative
def execute(dataframe, file_name):
    # Parameters
    period_len, next_periods = 12, 12

    # Generate result
    forecast_result, alpha, beta, gamma, rmse = hw.multiplicative(dataframe, period_len, next_periods)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_holt_winter.txt'
    f = open(out_file_name, 'w')

    print('Full timeframe:\n{}'.format(forecast_result), file=f)
    print('\n------------------------\n', file=f)
    print('Partial timeframe:\n{}'.format(forecast_result[-next_periods:]), file=f)
    print('\n------------------------\n', file=f)
    print('Alpha = {}'.format(alpha), file=f)
    print('\n------------------------\n', file=f)
    print('Beta = {}'.format(beta), file=f)
    print('\n------------------------\n', file=f)
    print('Gamma = {}'.format(gamma), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Combine dataframe
    result = pd.concat(objs=[dataframe, forecast_result], axis=1)
    result.columns = ['Actual', 'Forecast']

    # Plot
    result.plot()
    plt.show()

# --------------------------------------------------------------------------
