import pandas as pd
from matplotlib import pyplot as plt

import read_file
import ses


# --------------------------------------------------------------------------

# Parse input file
def load_data(file_name):
    # Date format
    date_format = lambda dates: pd.datetime.strptime(dates, '%b-%y')

    # Generate diet product sales dataframe
    diet_raw = read_file.parse_csv_file(file_name, date_format)

    # Return dataframe
    return diet_raw


# --------------------------------------------------------------------------

# Simple exponential smoothing
def execute(dataframe, file_name):
    # Generate result
    forecast_full_frame, forecast_partial_frame, rmse, alpha = ses.simple_exponential_smoothing(dataframe=dataframe,
                                                                                                next_periods=5)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_ses.txt'
    f = open(out_file_name, 'w')

    print('Full timeframe:\n{}'.format(forecast_full_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Partial timeframe:\n{}'.format(forecast_partial_frame), file=f)
    print('\n------------------------\n', file=f)
    print('Alpha:\n{}'.format(alpha), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Plot
    fig = plt.figure(0)
    fig.canvas.set_window_title('Single Exponential Smoothing')

    dataframe.plot()
    forecast_full_frame.plot()

    plt.show()

# --------------------------------------------------------------------------
