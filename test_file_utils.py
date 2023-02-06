""" This is the testing file of file_utils.py"""

import json

import file_utils1 as file_utils


def test_read_csv_file_into_json_test_header():
    """ Testing json header functionality"""

    min_header=["COLUMN_NAME","DESCRIPTION","HINT"]

if __name__ == '__main__':
    input_file="E:\onboarding_file.csv"
    input_str = file_utils.read_csv_file_into_json(input_file,separator="|",header=0)
    json_dic=json.loads(input_str)
    print(type(json_dic))
    #headers=json_dic[0].keys()
    #print(json_dic.keys())


    # assert json_dic is not None
    # assert json_dic[0] is not None
    # assert json_dic[0]["ORDER"]==1