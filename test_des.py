import pandas as pd
from matplotlib import pyplot as plt

import des
import readFile


def load_data(file_name):
    # Generate diet product's sales dataframe

    date_format = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

    df = readFile.parse_csv_file(file_name, date_format)
    return df


def execute(df, alpha, beta, file_name):
    # tmp = df.tolist()
    #
    # des_result = des.double_exponential_smoothing(tmp, alpha, beta)

    des_result = des.double_exponential_smoothing(df, alpha, beta)

    plt.plot(df)
    plt.plot(des_result)

    plt.show()