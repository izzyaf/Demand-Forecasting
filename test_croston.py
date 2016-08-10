import pandas as pd
from matplotlib import pyplot as plt

import croston
import read_file


# load data
def load_data(file_name):
    # Date format
    date_format = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

    # Generate diet product sales dataframe
    umpire_chair_raw = read_file.parse_csv_file(file_name, date_format)

    # Return dataframe
    return umpire_chair_raw


# execute Croston Method
def execute(dataframe, file_name):
    forecast_full_frame, forecast_partial_frame, rmse, alpha = croston.croston_method(dataframe=dataframe,
                                                                                      next_periods=12)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_croston.txt'
    f = open(out_file_name, 'w')

    print('Full time frame:\n{}'.format(forecast_full_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Partial time frame:\n{}'.format(forecast_partial_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Alpha = {}'.format(alpha), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Plot
    fig = plt.figure(0)
    fig.canvas.set_window_title('Croston\'s Method')

    dataframe.plot()
    forecast_full_frame.plot()

    plt.show()

# --------------------------------------------------------------------------
