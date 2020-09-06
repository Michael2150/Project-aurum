import pandas as pd
import numpy as np

#See the .py file to see how this function works
def get_regression_slope(xs,ys):
    n = min(len(xs),len(ys))
    mean_x = sum(xs)/n
    mean_y = sum(ys)/n
    reg_val1 = []
    reg_val2 = []
    for i in range(n):
        reg_val1.append((xs[i] - mean_x)*(xs[i] - mean_x))
        reg_val2.append((xs[i] - mean_x)*(ys[i] - mean_y))
    a = sum(reg_val2)/sum(reg_val1)
    return a

training_rows = 11

print("======== Reading Data ==========")
input_file_name = "ParsedDataSmoll.csv"
input_data = pd.read_csv(input_file_name)
print(input_data)

print("======== Parsing Data ==========")
reg_vals = []
corr_vals = []
ouputs = []

calcxs = []
calcys = []

i = 0 
for row_data in input_data.iterrows():
    row = row_data[1]
    calcxs.append(row["time"])
    calcys.append(row["value"])
    if i == training_rows:
        ouputs.append(calcys[len(calcys)-1])
        calcxs.pop()
        calcys.pop()
        
        reg_vals.append(get_regression_slope(calcxs,calcys))
        corr_vals.append(np.corrcoef(calcxs,calcys)[0][1])
        
        calcxs = []
        calcys = []
        i = 0
    i += 1

print("======== Saving Data ==========")
inputdata = {"regression_slope":reg_vals,
             "correlation_coefficient":corr_vals,
             "output":ouputs}
generatedData = pd.DataFrame(data=inputdata)
generatedData.to_csv('GeneratedTrainingData.csv')
print(generatedData.tail())
    

    
    

