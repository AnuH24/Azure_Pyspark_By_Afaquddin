import pandas as pd
import csv
import json

#input_file = "E:\onboarding_file.csv"
data = pd.read_csv(r"E:\new.csv", sep=",")
#print(data)
c=data['name'].to_dict().values()
print(c)

#print(data.loc[:,"COLUMN_NAME"])
# print(type(c))

# with open('test6.csv', 'w') as f:
#     for i in c:
#         f.write("%s," % (i))
# with open('Names.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile)
#     writer.writeheader()
#     writer.writerows(c)

with open('mycsvfile.csv','a') as f:
    w = csv.writer(f)
    #w.writerow(c.keys())
    w.writerow(c)

# with open('c', 'w') as f:
#     csv_reader= csv.writer(f)
#     for line in csv_reader:
#         print(line)

# for row in data:
#     print(row[2])
# print(type(data))

#
# import csv
#
# inputfile = csv.reader(open('E:\onboarding_file.csv','r'))
#
# for row in inputfile:
#     print(row[2])

# with open('E:\onboarding_file.csv','r') as fin, \
#      open('E:\output_file.csv', 'w') as fout:
#     print(json.dump(fout))
    # print(fout)
    # reader = csv.DictReader(fin)
    # writer = csv.DictWriter(fout, reader.fieldnames, delimiter=',')
    # writer.writeheader()
    # writer.writerows(reader)
# import file_utils1
# data = file_utils1.read_csv_file_into_json(input_file, separator="|",header=None)
# print(data)