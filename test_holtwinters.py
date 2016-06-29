from matplotlib import pyplot as plt
import pandas as pd
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
    forecast_data, alpha, beta, gamma, rmse = hw.multiplicative(dataframe, period_len, next_periods)

    text = 'rmse = ' + str(round(rmse, 2))

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_holt_winter.txt'
    f = open(out_file_name, 'w')

    print('Full timeframe:\n{}'.format(forecast_data), file=f)
    print('\n------------------------\n', file=f)
    print('Partial timeframe:\n{}'.format(forecast_data[-next_periods:]), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Plot
    fig = plt.figure(0)
    fig.canvas.set_window_title('Holt-Winters Exponential Smoothing with Multiplicative')

    dataframe.plot()
    forecast_data.plot()

    plt.show()

# --------------------------------------------------------------------------
