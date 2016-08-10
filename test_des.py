import pandas as pd
from matplotlib import pyplot as plt

import des
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

# Double exponential smoothing
def execute(dataframe, file_name):
    next_period = 12

    # Generate result
    forecast_result, rmse, alpha, beta = des.double_exponential_smoothing(dataframe, next_period)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_double_exponential_smoothing.txt'
    f = open(out_file_name, 'w')

    print('Full time frame:\n{}'.format(forecast_result), file=f)
    print('\n------------------------\n', file=f)
    print('Partial time frame:\n{}'.format(forecast_result[-next_period:]), file=f)
    print('\n------------------------\n', file=f)
    print('Alpha = {}'.format(alpha), file=f)
    print('\n------------------------\n', file=f)
    print('Beta = {}'.format(beta), file=f)
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
