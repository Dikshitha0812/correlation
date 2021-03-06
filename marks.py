import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    marks = []
    attendance = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"]))

    return {"x" : marks, "y": attendance}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between marks and attendance :-  \n--->",correlation)

def setup():
    data_path  = "./data3.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()