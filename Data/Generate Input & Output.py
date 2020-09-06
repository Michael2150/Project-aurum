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

training_rows = 51

print("======== Reading Data ==========")
input_file_name = "ParsedDataSmoll.csv"
input_data = pd.read_csv(input_file_name)
print(input_data)

print("======== Parsing Data ==========")
reg_vals = []
corr_vals = []
outputs = []
outputtimes = []
sec_output_time_difs = []

timedifs = []
starttimes = []
endtimes = []

maxvals = []
minvals = []
valdifs = []

calcxs = []
calcys = []

i = 0 
for row_data in input_data.iterrows():
    row = row_data[1]
    calcxs.append(row["time"])
    calcys.append(row["value"])
    if i == training_rows:
        outputs.append(calcys[len(calcys)-1])
        outputtimes.append(calcxs[len(calcxs)-1])
            
        calcxs.pop()
        calcys.pop()

        starttimes.append(calcxs[0])
        endtimes.append(calcxs[len(calcxs)-1])
        timedifs.append(endtimes[len(endtimes)-1] - starttimes[len(endtimes)-1])
        sec_output_time_difs.append(outputtimes[len(outputtimes)-1] - endtimes[len(endtimes)-1])
        
        maxvals.append(max(calcys))
        minvals.append(min(calcys))
        valdifs.append(max(calcys - min(calcys)))
        
        corr_vals.append(np.corrcoef(calcxs,calcys)[0][1])
        reg_vals.append(get_regression_slope(calcxs,calcys))
            
        calcxs = []
        calcys = []
        i = 0
    i += 1
        
print("======== Saving Data ==========")
inputdata = {"regression_slope":reg_vals,
             "correlation_coefficient":corr_vals,
             "output":outputs,
             "output_time":outputtimes,
             "section_&_output_time_difference":sec_output_time_difs,
             "section_start_time":starttimes,
             "section_end_time":endtimes,
             "section_time_difference":timedifs,
             "section_max_value":maxvals,
             "section_min_value":minvals,
             "section_max_min_difference":valdifs}
generatedData = pd.DataFrame(data=inputdata)
generatedData.to_csv('TrainingData.csv')
print(generatedData.tail())
    

    
    

