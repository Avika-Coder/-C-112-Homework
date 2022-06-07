from google.colab import files
data_to_load=files.upload()

import pandas as pd
import csv
import plotly.express as px
import statistics
df=pd.read_csv("savings_data_Hw.csv")
graph1=px.scatter(df,y="quant_saved",color="wealthy")
graph1.show()

import csv
import plotly.graph_objects as go

with open ('savings_data_Hw.csv',newline="") as f:
  r1=csv.reader(f)
  savingData=list(r1)
savingData.pop(0)
totalEntries=len(savingData)
totalPeopleGivenReminder=0
for i in savingData:
  if int(i[3])==1:
    totalPeopleGivenReminder=totalPeopleGivenReminder+1
v1=go.Figure(go.Bar(x=["reminder","notReminder"],y=[totalPeopleGivenReminder,(totalEntries-totalPeopleGivenReminder)]))
v1.show()

all_savings=[]
for data in savingData:
  all_savings.append(float(data[0]))
reminded_saving=[]
not_reminded_saving=[]
for data in savingData :
   if int(data[3])==1:
    reminded_saving.append(float(data[0]))
   else:
    not_reminded_saving.append(float(data[0]))

print("Results for people who were reminded to save")
print(f"Mean of savings - {statistics.mean(reminded_saving)}")
print(f"Median of savings - {statistics.median(reminded_saving)}")
print(f"Mode of savings - {statistics.mode(reminded_saving)}")
print("\n\n")
print(f"Mean of savings - {statistics.mean(not_reminded_saving)}")
print(f"Median of savings - {statistics.median(not_reminded_saving)}")
print(f"Mode of savings - {statistics.mode(not_reminded_saving)}")
print("\n\n")
print(f"Standard deviation of all data -> {statistics.stdev(all_savings)}")
print(f"Standard deviation of people who were reminded -> {statistics.stdev(reminded_saving)}")
print(f"Standard deviation of people who were not reminded -> {statistics.stdev(not_reminded_saving)}")
print("\n\n")

import numpy as np
age =[]
savings = []
for data in savingData:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))
correlation = np.corrcoef(age,savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")
