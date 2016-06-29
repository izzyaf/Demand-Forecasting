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
def execute(dataframe, alpha, beta, file_name):
    # Generate result
    des_result = des.double_exponential_smoothing(dataframe, alpha, beta)

    # Log result to file
    out_file_name = 'data/result_' + file_name.split('.')[0] + '_double_exponential_smoothing.txt'
    f = open(out_file_name, 'w')

    print('Full timeframe:\n{}'.format(des_result), file=f)
    print('\n------------------------\n', file=f)

    # Bổ sung đoạn timeframe dự đoán thêm vào đây
    # print('Partial timeframe:\n{}'.format(predicted_frame), file=f)
    # print('\n------------------------\n', file=f)

    # Chỗ này để RMSE = sai số
    # print('RMSE = {}'.format(rmse), file=f)

    f.close()

    # Plot
    fig = plt.figure(1)
    fig.canvas.set_window_title('Double Exponential Smoothing')

    dataframe.plot()
    des_result.plot()

    plt.show()

# --------------------------------------------------------------------------
