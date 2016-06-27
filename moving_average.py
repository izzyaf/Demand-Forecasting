import pandas as pd
import numpy as np
import math
import matplotlib
from matplotlib import pyplot as plt
from pandas.tseries.offsets import *
from fractions import Fraction


def moving_average(dataframe, window, ahead, file_name):
    date_format = '%b-%y'
    date_range = pd.date_range(start=dataframe.index[-1] + DateOffset(months=1), periods=ahead, format=date_format,
                               freq='MS')

    forecast_frame = dataframe.append(pd.Series(data=[0] * ahead, index=date_range))
    forecast_frame.loc[range(window)] = np.nan

    for idx in dataframe.index[window:dataframe.count()]:
        forecast_frame.loc[idx] = round(
            np.mean([dataframe.loc[idx - DateOffset(months=i)] for i in range(1, window + 1)]))
    for idx in date_range:
        forecast_frame.loc[idx] = round(np.mean(
            [forecast_frame.loc[idx - DateOffset(months=i)] for i in range(1, window + 1)]))

    forecast_frame.dropna(inplace=True)

    percentage_of_accuracy = []

    for idx in dataframe.index[window:dataframe.count() - window]:
        percentage_of_accuracy.extend(
            ['{0}%'.format(round(np.mean([dataframe.loc[idx + DateOffset(months=i)] for i in range(window)]) / np.mean(
                [forecast_frame.loc[idx + DateOffset(months=i)] for i in range(window)]) * 100))])

    predicted_frame = forecast_frame[~forecast_frame.index.isin(dataframe.index)]

    out_file_name = 'data/result_' + file_name.split('.')[0] + '_moving_average.txt'
    f = open(out_file_name, 'w')
    print('Full timeframe:\n', file=f)
    print(forecast_frame, file=f)
    print('\nPartial timeframe:\n', file=f)
    print(predicted_frame, file=f)
    print('\nPercentage of accuracy\n', file=f)
    print(str(percentage_of_accuracy).strip('[]'), file=f)

    f.close()

    fig = plt.figure(0)
    fig.canvas.set_window_title('Moving Average')

    dataframe.plot()
    forecast_frame.plot()


def weighted_moving_average(dataframe, window, ahead, file_name):
    date_format = '%b-%y'
    date_range = pd.date_range(start=dataframe.index[-1] + DateOffset(months=1), periods=ahead, format=date_format,
                               freq='MS')
    forecast_frame = dataframe.append(pd.Series(data=[0] * ahead, index=date_range))
    forecast_frame.loc[range(window)] = np.nan

    weight_array = []

    for i in range(1, window + 1):
        weight_array.append(Fraction(i * 2, pow(window, 2) + window))

    for idx in dataframe.index[window:dataframe.count()]:
        forecast_frame.loc[idx] = round(np.sum([
                                                   dataframe.loc[idx - DateOffset(months=i)] * float(
                                                       weight_array[window - i])
                                                   for i in range(1, window + 1)]))
    for idx in date_range:
        forecast_frame.loc[idx] = round(np.sum([
                                                   forecast_frame.loc[idx - DateOffset(months=i)] * weight_array[
                                                       window - i] for i in
                                                   range(1, window + 1)]))

    forecast_frame.dropna(inplace=True)

    percentage_of_accuracy = []

    for idx in dataframe.index[window:dataframe.count() - window]:
        percentage_of_accuracy.extend(
            ['{0}%'.format(round(np.mean([dataframe.loc[idx + DateOffset(months=i)] for i in range(window)]) / np.mean(
                [forecast_frame.loc[idx + DateOffset(months=i)] for i in range(window)]) * 100))])

    predicted_frame = forecast_frame[~forecast_frame.index.isin(dataframe.index)]

    out_file_name = 'data/result_' + file_name.split('.')[0] + '_weighted_moving_average_.txt'
    f = open(out_file_name, 'w')
    print('Full timeframe:\n', file=f)
    print(forecast_frame, file=f)
    print('\nPartial timeframe:\n', file=f)
    print(predicted_frame, file=f)
    print('\nPercentage of accuracy\n', file=f)
    print(str(percentage_of_accuracy).strip('[]'), file=f)

    f.close()

    fig = plt.figure(1)
    fig.canvas.set_window_title('Weighted Moving Average')

    dataframe.plot()
    forecast_frame.plot()
