# Import

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


# ------------------------------------------------------------------

# Process .csv as input. Return a dataframe, with time-series used as index


def parse_csv_file(file_name, date_format):
    data = pd.read_csv(filepath_or_buffer=file_name, parse_dates=True, date_parser=date_format, index_col=0,
                       squeeze=True)
    return data


# ------------------------------------------------------------------

# Generate historical dataframe

file_name = 'data/car.csv'
f = open('data/raw_historical_data.txt', 'w')
date_format = lambda dates: pd.datetime.strptime(dates, "%Y-%m")

historical_data = parse_csv_file(file_name, date_format)

print(historical_data, file=f)
f.close()

# ------------------------------------------------------------------
