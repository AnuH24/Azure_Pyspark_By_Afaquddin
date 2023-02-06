""" This module is common module"""
import json

import pandas as pd

def read_csv_file_into_pandas(input_file, separator=",",header=None):
    
    """ Reading csv file into pandas
    """
    return pd.read_csv(input_file, sep = separator, header = header)

def read_csv_file_into_json(input_file, separator=",",header=None):
    """ Reading csv file into json
    """
    input_df=read_csv_file_into_pandas(input_file,separator,header)
    return input_df.to_json(orient='index')


if __name__ == '__main__':
    INPUT_FILE="E:\onboarding_file.csv"
    input_df = read_csv_file_into_json(INPUT_FILE,separator="|",header=0)
    print(input_df)
    print(type(input_df))

