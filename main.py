# Import

from __future__ import print_function
import sys

import test_movingAverage as tma
import test_ses as tses
import test_des as tdes
import test_holtwinters as thw


def ses():
    # test simple exponential smoothing
    print('Test simple exponential smoothing')
    input_file_name = 'diet_product.csv'
    data_frame = tses.load_data(input_file_name)
    tses.execute(data_frame, input_file_name)


def des():
    print('Test double exponential smoothing')
    file_name = 'car.csv'

    alpha, beta = 0.3, 0.3
    df = tdes.load_data(file_name)
    tdes.execute(df, alpha, beta, file_name)


def mva():
    # test moving average
    print('Test moving average')
    input_file_name = 'tshirt.csv'
    data_frame = tma.load_data(input_file_name)
    tma.execute(data_frame, input_file_name)


def hw():
    print('Test Holt Winters')
    file_name = 'car.csv'

    df = thw.load_data(file_name)
    thw.execute(df, file_name)


def show_menu():
    print("------------------- DEMAND FORECASTING -------------------")
    print("1. Single Exponential Smoothing")
    print("2. Double Exponential Smoothing")
    print("3. Holt Winters Exponential Smoothing with Multiplicative")
    print("4. Moving Average")
    print("0. Quit\n")


def __main__():

    while True:
        show_menu()
        choice = int(input("Enter method: "))

        if choice == 0:
            break

        elif choice == 1:
            ses()

        elif choice == 2:
            des()

        elif choice == 3:
            hw()

        elif choice == 4:
            mva()


__main__()

