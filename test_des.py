from matplotlib import pyplot as plt
import pandas as pd
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
    des_result, rmse = des.double_exponential_smoothing(dataframe, next_period)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_double_exponential_smoothing.txt'
    f = open(out_file_name, 'w')

    print('Full time frame:\n{}'.format(des_result), file=f)
    print('\n------------------------\n', file=f)

    predicted_frame = des_result[-next_period:]

    print('Partial time frame:\n{}'.format(predicted_frame), file=f)
    print('\n------------------------\n', file=f)

    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Plot
    fig = plt.figure(1)
    fig.canvas.set_window_title('Double Exponential Smoothing')

    dataframe.plot()
    des_result.plot()

    plt.show()

# --------------------------------------------------------------------------
