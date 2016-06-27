import pandas as pd
from matplotlib import pyplot as plt
import readFile

import moving_average as ma


def load_data(file_name):
    # Generate tshirt's sales dataframe

    date_format = lambda dates: pd.datetime.strptime(dates, '%b-%y')

    tshirt_raw = readFile.parse_csv_file(file_name, date_format)
    return tshirt_raw


def execute(df, file_name):
    # Moving average
    ma.moving_average(dataframe=df, window=3, ahead=5, file_name=file_name)

    # Weighted moving average
    ma.weighted_moving_average(dataframe=df, window=5, ahead=5, file_name=file_name)

    plt.show()
