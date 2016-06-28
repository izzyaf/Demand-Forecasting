import pandas as pd
from matplotlib import pyplot as plt

import holtwinters as hw
import readFile


def load_data(file_name):
    # Generate quebec's car sales dataframe

    date_format = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

    car_raw = readFile.parse_csv_file(file_name, date_format)

    return car_raw


def execute(df, file_name):
    tmp = df.tolist()

    m, fc = 12, 12
    forecast_data, alpha, beta, gamma, rmse, y = hw.multiplicative(tmp, m, fc)

    # head = [0 for i in range(len(tmp))]

    # head.extend(forecast_data)
    y.extend(forecast_data)

    text = 'rmse = ' + str(round(rmse, 2))

    plt.xlabel('Bucket')
    plt.ylabel('Demand Values')
    plt.title('Holt Winters Exponential Smoothing with Multiplicative')
    plt.text(10, 2500, text)
    plt.grid(True)

    plt.plot(tmp)
    plt.plot(y)

    plt.show()


