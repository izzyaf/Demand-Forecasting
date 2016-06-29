from __future__ import print_function
import pandas as pd


# --------------------------------------------------------------------------

# Process input file
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

# --------------------------------------------------------------------------
