# Import

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import moving_average as ma


# ------------------------------------------------------------------

# Process .csv as input. Return a dataframe, with time-series used as index


def parse_csv_file(file_name, date_format):
    name = file_name.split('.')[0]
    file_name = 'data/' + file_name
    out_file_name = 'data/raw_' + name + '.txt'

    data = pd.read_csv(filepath_or_buffer=file_name, parse_dates=True, date_parser=date_format, index_col=0,
                       squeeze=True)
    f = open(out_file_name, 'w')
    print('Original data:\n', file=f)
    print(data, file=f)
    f.close()
    return data


# ------------------------------------------------------------------

# Generate quebec's car sales dataframe

file_name = 'car.csv'
date_format = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

car_raw = parse_csv_file(file_name, date_format)

# ------------------------------------------------------------------

file_name = 'tshirt.csv'
date_format = lambda dates: pd.datetime.strptime(dates, '%b-%y')

tshirt_raw = parse_csv_file(file_name, date_format)

# Rolling average
ma.moving_average(dataframe=tshirt_raw, window=3, ahead=5, file_name=file_name)
