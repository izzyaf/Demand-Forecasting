# Import

from __future__ import print_function

import test_movingAverage as tma
import test_ses as tses

choice = 2

if choice == 1:
    # test moving average
    print('Test moving average')
    input_file_name = 'tshirt.csv'
    data_frame = tma.load_data(input_file_name)
    tma.execute(data_frame, input_file_name)

if choice == 2:
    # test simple exponential smoothing
    print('Test simple exponential smoothing')
    input_file_name = 'diet_product.csv'
    data_frame = tses.load_data(input_file_name)
    tses.execute(data_frame, input_file_name)
