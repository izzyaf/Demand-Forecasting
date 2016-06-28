import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.tseries.offsets import *
from statsmodels.tools import eval_measures


def simple_exponential_smoothing(dataframe, ahead, alpha, file_name):
    date_format = '%b-%y'
    date_range = pd.date_range(start=dataframe.index[-1] + DateOffset(months=1), periods=ahead, format=date_format,
                               freq='MS')

    forecast_frame = dataframe.append(pd.Series(data=[np.nan] * ahead, index=date_range))
    forecast_frame.drop(forecast_frame.index[0], inplace=True)
    for idx in dataframe.index:
        if dataframe.index.get_loc(idx) == 0:
            forecast_frame.iloc[0] = dataframe.loc[idx]
        else:
            forecast_frame.loc[idx + DateOffset(months=1)] = alpha * dataframe.loc[idx] + (1 - alpha) * \
                                                                                          forecast_frame.loc[
                                                                                              idx]
    for idx in date_range[1:ahead]:
        forecast_frame.loc[idx] = forecast_frame.loc[idx - DateOffset(months=1)]

    predicted_frame = forecast_frame[~forecast_frame.index.isin(dataframe.index)]

    rmse = eval_measures.rmse(dataframe[1:dataframe.count()], forecast_frame[0:dataframe.count() - 1])

    out_file_name = 'data/result_' + file_name.split('.')[0] + '_ses.txt'
    f = open(out_file_name, 'w')
    print('Full timeframe:\n{}'.format(forecast_frame), file=f)
    print('\n------------------------\n', file=f)
    print
    print('Partial timeframe:\n{}'.format(predicted_frame), file=f)
    print('\n------------------------\n', file=f)
    print('RMSE = {}'.format(rmse), file=f)

    f.close()

    fig = plt.figure(0)
    fig.canvas.set_window_title('Single Exponential Smoothing')

    dataframe.plot()
    forecast_frame.plot()
