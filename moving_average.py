import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from pandas.tseries.offsets import *


def write_result_file(file_name, full_result, partial_result):
    out_file_name = 'data/result_' + file_name.split('.')[0] + '.txt'
    f = open(out_file_name, 'w')
    print('Full timeframe:\n', file=f)
    print(full_result, file=f)
    print('\nPartial timeframe:\n', file=f)
    print(partial_result, file=f)
    f.close()


def moving_average(dataframe, window, ahead, file_name):
    date_format = '%b-%y'
    date_range = pd.date_range(start=dataframe.index[-1] + DateOffset(months=1), periods=ahead, format=date_format,
                               freq='MS')

    forecast_frame = dataframe.append(pd.Series(data=[0] * ahead, index=date_range))
    for idx in date_range:
        forecast_frame.loc[idx] = np.mean(
            [forecast_frame.loc[idx - DateOffset(months=i)] for i in range(1, window + 1)])

    predicted_frame = forecast_frame[~forecast_frame.index.isin(dataframe.index)]

    write_result_file(file_name, forecast_frame, predicted_frame)

    dataframe.plot()
    predicted_frame.plot()

    plt.show()
