import pandas as pd
from matplotlib import pyplot as plt

import readFile
import des


def load_data(file_name):
    # Generate diet product's sales dataframe

    date_format = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

    df = readFile.parse_csv_file(file_name, date_format)
    return df


def execute(df, alpha, beta, file_name):
    tmp = df.tolist()

    des_result = des.double_exponential_smoothing(tmp, alpha, beta)

    plt.plot(tmp)
    plt.plot(des_result)

    plt.show()