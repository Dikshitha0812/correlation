import csv
import plotly.express as px
import numpy as np

with open("data1.csv") as f:
    df =csv.DictReader(f)
    temp = []
    icecream = []
    colddrinks = []
    for row in df:
        temp.append(float(row["Temperature"]))
        icecream.append(float(row["Ice-cream Sales( ₹ )"]))
        colddrinks.append(float(row["Cold drink sales( ₹ )"]))

correlation = np.coercoeff(icecream, colddrinks)
print(correlation)
