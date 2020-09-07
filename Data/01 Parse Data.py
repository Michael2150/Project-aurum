import pandas as pd
from datetime import datetime

def secs(dt):
    return (dt - datetime(2000, 1, 1)).total_seconds()

FileNames = ['DAT_XLSX_GBPUSD_M1_2000.csv' ]
#             'DAT_XLSX_GBPUSD_M1_2001.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2002.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2003.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2004.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2005.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2006.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2007.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2008.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2009.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2010.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2011.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2012.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2013.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2014.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2015.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2016.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2017.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2018.csv' ,
#             'DAT_XLSX_GBPUSD_M1_2019.csv' ]

print("======== Reading Data ==========")
concatData = []
for i in range(len(FileNames)):
    print("Reading file: " + FileNames[i])
    dataval = pd.read_csv(FileNames[i])
    print(dataval.tail())
    concatData.append(dataval)
raw_input_data = pd.concat(concatData)

print(raw_input_data)

print("======== Parsing Data ==========")
seconds = []
mean_vals = []
file_index = 0
for row_data in raw_input_data.iterrows():
    
    if row_data[0] == 0:
        print("parsing file: " + FileNames[file_index])
        file_index += 1
    
    #Converts the Date/time collumn to seconds:
    seconds.append(secs(datetime.strptime(row_data[1]["Date/time"],'%m/%d/%Y %H:%M')))
    #Get mean of the 3 values:
    mean_vals.append(sum([row_data[1]["Value1"],row_data[1]["Value2"],row_data[1]["Value3"]]) / 3 )

print("======== Saving Data ==========")
inputdata = {"time":seconds,
            "value":mean_vals}
parsedData = pd.DataFrame(data=inputdata)
parsedData.to_csv('ParsedDataSmoll.csv')
print(parsedData.tail())
