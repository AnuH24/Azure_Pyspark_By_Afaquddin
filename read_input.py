import getpass
import file_utils1
import json
import anur
import pandas as pd


def read_input(input_json_str):

    input_json=json.loads(input_json_str)
    # print(input_json)

    for row_num in input_json:
        column_name=input_json[row_num]["COLUMN_NAME"]
        #return column_name
        print(column_name)
        # description=input_json[row_num]["DESCRIPTION"]
        # hint=input_json[row_num]["HINT"]
        # user_input=input(f"{description}[{hint}]:" )
        # input_json[row_num]["USER_INPUT"]=user_input

        
    # print(input_json)
    # print(type(input_json))
    # df = pd.read_json(input_json)
    # df.to_csv('file.csv')

    # data = json.loads(input_json)
    # headers = data[0].keys()
    #
    # with open('file.csv', 'w') as f:
    #     writer = csv.DictWriter(f, fieldnames=headers)
    #     writer.writeheader()
    #     writer.writerows(data)

    # with open('data.txt', 'a') as d:
    #     d.write(json.dumps(input_json))
    #     d.write('\n')


    # user = input("Username [%s]: " % getpass.getuser())
    # if not user:
    #     user = getpass.getuser()

    # pprompt = lambda: (getpass.getpass(), getpass.getpass('Retype password: '))

    # p1, p2 = pprompt()
    # while p1 != p2:
    #     print('Passwords do not match. Try again')
    #     p1, p2 = pprompt()

    # return user, p1


if __name__ == '__main__':

    input_file = "E:\onboarding_file.csv"
    input_json = file_utils1.read_csv_file_into_json(
        input_file, separator="|", header=0)
    # print(input_json)

    print(read_input(input_json))
