# abc={}
# abc["abhi"]=1
# print(abc)
# if i in abc:
#     abc[i]+=1
#     print()

import anur
import json

import pandas as pd

import read_input
#json_string = '[{"Name": "Nik", "Age": 30, "Active": true}, {"Name": "Kate", "Age": 32, "Active": true}, {"Name": "Evan", "Age": 45, "Active": false}, {"Name": "Kyra", "Age": 43, "Active": true}]'
# json_string = {'0': {'ORDER': 1, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'SOURCE_TYPE', 'DESCRIPTION': 'Source Type', 'HINT': ' Type of database like Oracle, MySql, PostgresSQL', 'USER_INPUT': 'S'}, '1': {'ORDER': 2, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'SOURCE_DB_NAME', 'DESCRIPTION': 'Source Database Name', 'HINT': ' Input Source database name', 'USER_INPUT': 'D'}, '2': {'ORDER': 3, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'SOURCE_TABLE_NAME', 'DESCRIPTION': 'Source Table Name', 'HINT': ' Input Source table name', 'USER_INPUT': 'F'}, '3': {'ORDER': 4, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'CREDENTIAL_TYPE', 'DESCRIPTION': 'Credential Type', 'HINT': ' Where the credenital has provided like SECRETMANAGER, FILE', 'USER_INPUT': 'D'}, '4': {'ORDER': 5, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'CREDENTIAL_VALUE', 'DESCRIPTION': 'Credential Value', 'HINT': ' The secrets name or file location', 'USER_INPUT': 'F'}, '5': {'ORDER': 6, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'CDC_COLUMNS', 'DESCRIPTION': 'CDC Columns', 'HINT': ' The data base column on which CDC will be applied comma seperated columns', 'USER_INPUT': 'D'}, '6': {'ORDER': 7, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'START_VALUE', 'DESCRIPTION': 'Start Value', 'HINT': ' This is the start value of the CDC columns if the CDC columns are of type Dates, the start value will be 1970-01-01 00:00:00, other wise it starts from -1', 'USER_INPUT': ''}, '7': {'ORDER': 8, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'END_VALUE', 'DESCRIPTION': 'END VALUE', 'HINT': ' This is the end value of the CDC columns if the CDC columns are of type Dates, Computed on the fly if not provided', 'USER_INPUT': 'S'}, '8': {'ORDER': 9, 'CATEGORY': 'SOURCE', 'COLUMN_NAME': 'FORMAT', 'DESCRIPTION': 'FORMAT', 'HINT': ' Format of the Start Value', 'USER_INPUT': 'D'}, '9': {'ORDER': 10, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'TARGET_CREDENTIALS', 'DESCRIPTION': 'Target Credentials', 'HINT': ' Target Credentials required to Connect to target system', 'USER_INPUT': 'F'}, '10': {'ORDER': 11, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'TARGET_TYPE', 'DESCRIPTION': 'Target Type', 'HINT': ' Target information like s3, snowflake, default to S3', 'USER_INPUT': 'F'}, '11': {'ORDER': 12, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'TARGET_LOCATION', 'DESCRIPTION': 'Target Location', 'HINT': ' Target location information where we need to store data if it is s3, its a bucket', 'USER_INPUT': 'F'}, '12': {'ORDER': 13, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'TARGET_KEY', 'DESCRIPTION': 'Target Key', 'HINT': ' The directory where we need to store, default to table name', 'USER_INPUT': 'D'}, '13': {'ORDER': 14, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'PARTION_COLUMN', 'DESCRIPTION': 'Partition Column', 'HINT': ' The partition on which column', 'USER_INPUT': 'E'}, '14': {'ORDER': 15, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'SOURCE_PARTION_COLUMN_FORMAT', 'DESCRIPTION': 'Source Partition Column FORMAT', 'HINT': ' The partition column format of the source, default MMddYYYY', 'USER_INPUT': 'S'}, '15': {'ORDER': 16, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'PARTION_COLUMN_FORMAT', 'DESCRIPTION': 'Partition Column FORMAT', 'HINT': ' The partition column format to store on destination, default MMddYYYY', 'USER_INPUT': 'SW'}, '16': {'ORDER': 17, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'ADD_COLUMN_NAME_1', 'DESCRIPTION': 'Addition Column 1', 'HINT': ' Additional Column 1 required to add', 'USER_INPUT': 'W'}, '17': {'ORDER': 18, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'ADD_COLUMN_VALUE_1', 'DESCRIPTION': 'Addition Column Value 1', 'HINT': ' Additional Column 1 value to add', 'USER_INPUT': 'E'}, '18': {'ORDER': 19, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'ADD_COLUMN_NAME_2', 'DESCRIPTION': 'Addition Column 2', 'HINT': ' Additional Column 2 required to add', 'USER_INPUT': 'D'}, '19': {'ORDER': 20, 'CATEGORY': 'TARGET', 'COLUMN_NAME': 'ADD_COLUMN_VALUE_2', 'DESCRIPTION': 'Addition Column Value 2', 'HINT': ' Additional Column 2 value to add', 'USER_INPUT': 'E'}}
#
# data = json.loads(json_string)
# headers = data[0].keys()
#
# with open('file.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(data)
df = pd.read_csv('E:\onboarding_file.csv')
df= pd.DataFrame(df)
print(df.to_string())
# df.del
# for line in df:
#     print(line[2])
#df=df.drop(columns='description')
#print(df)


# info = pd.DataFrame(df)
# #print('DataFrame:\n', info.to_string())
# csv_data = info.to_csv(sep='|')
# print(csv_data)

#print(type(csv_data))

# with open('E:\onboarding_file.csv', 'r') as csv_file:
#     csv_reader= csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)