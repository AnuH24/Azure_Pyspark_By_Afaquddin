import pandas as pd
import csv
from datetime import datetime


def generate_onboarding_document(onboarding_config_file, client_name="client", separator=","):
    df=pd.read_csv(onboarding_config_file,sep=separator)
    return df

if __name__ == '__main__':

    onboarding_config_file="E:\onboarding_file.csv"
    # Loading csv file into data frame
    data = generate_onboarding_document(onboarding_config_file, separator="|")
    #print(data)
    # extracting the coulumn "COLUMN_NAME" and converting to dictionary
    c=data['COLUMN_NAME'].to_dict()
    #print(c)
    client_name=input("please enter:")
    x = datetime.now()
    file_name = r"Onboarding_document"+"_"+client_name+"_" + x.strftime('%m-%d-%Y.csv')
    with open(file_name,'w') as f:
        w = csv.writer(f)
        #w.writerow(c.keys())
        w.writerow(c.values())