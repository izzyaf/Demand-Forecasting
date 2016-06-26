# Import

from __future__ import print_function
import pandas as pd
from matplotlib import pyplot as plt

import des
import holtwinters as hw


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

alpha, beta = 0.3, 0.3
# des_result = des.double_exponential_smoothing(historical_data, alpha, beta)

# plt.plot(des_result)

tmp = historical_data.tolist()
hw_result = hw.multiplicative(tmp, 12, 12)

plt.plot(tmp)
plt.plot(hw_result[0])
print(hw_result[1:])
plt.show()

# print(historical_data, file=f)
f.close()

# ------------------------------------------------------------------
