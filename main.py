from __future__ import print_function

import test_croston as tcr
import test_des as tdes
import test_holtwinters as thw
import test_moving_average as tma
import test_ses as tses


# --------------------------------------------------------------------------

def ses():
    # test simple exponential smoothing
    print('Test simple exponential smoothing')

    input_file_name = 'ses_sales_diet_product.csv'
    print('Input file: {}'.format(input_file_name))

    data_frame = tses.load_data(input_file_name)
    tses.execute(data_frame, input_file_name)


# --------------------------------------------------------------------------

def des():
    print('Test double exponential smoothing')
    file_name = 'm3.csv'

    print('Input file: {}'.format(file_name))

    df = tdes.load_data(file_name)
    tdes.execute(df, file_name)


# --------------------------------------------------------------------------

def mva():
    # test moving average
    print('Test moving average')

    input_file_name = 'tshirt.csv'
    print('Input file: {}'.format(input_file_name))

    data_frame = tma.load_data(input_file_name)
    tma.execute_ma(data_frame, input_file_name)


# --------------------------------------------------------------------------

def wmva():
    # test weighted moving average
    print('Test weighted moving average')

    input_file_name = 'tshirt.csv'
    print('Input file: {}'.format(input_file_name))

    data_frame = tma.load_data(input_file_name)
    tma.execute_wma(data_frame, input_file_name)


# --------------------------------------------------------------------------

def hw():
    print('Test Holt Winters')

    file_name = 'm3.csv'
    print('Input file: {}'.format(file_name))

    df = thw.load_data(file_name)
    thw.execute(df, file_name)


# --------------------------------------------------------------------------


def croston():
    print('Test Croston\'s Method')

    file_name = 'intermittent_umpire_chair_paris.csv'
    print('Input file: {}'.format(file_name))

    df = tcr.load_data(file_name)
    tcr.execute(df, file_name)


# --------------------------------------------------------------------------


def show_menu():
    print("------------------- DEMAND FORECASTING -------------------")
    print("1. Single Exponential Smoothing")
    print("2. Double Exponential Smoothing")
    print("3. Holt Winters Exponential Smoothing with Multiplicative")
    print("4. Moving Average")
    print("5. Weighted Moving Average")
    print("6. Croston\'s Method")
    print("0. Quit\n")


# --------------------------------------------------------------------------

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

        elif choice == 5:
            wmva()
        elif choice == 6:
            croston()


# --------------------------------------------------------------------------

__main__()
