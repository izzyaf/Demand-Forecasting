import pandas as pd
from matplotlib import pyplot as plt

import readFile
import ses


def load_data(file_name):
    # Generate diet product's sales dataframe

    date_format = lambda dates: pd.datetime.strptime(dates, '%b-%y')

    diet_raw = readFile.parse_csv_file(file_name, date_format)
    return diet_raw


def execute(df, file_name):
    ses.simple_exponential_smoothing(dataframe=df, ahead=5, alpha=0.2, file_name=file_name)

    plt.show()
