# Import

from __future__ import print_function

import test_movingAverage as tma

# test moving average
input_file_name = 'tshirt.csv'
data_frame = tma.load_data(input_file_name)
tma.execute(data_frame, input_file_name)