
import pandas as pd

df = pd.read_csv("health_08-02-2022.csv")
for i, j in df.iterrows():
    my_list = j[:1].get(0).split(",")
    for x in my_list:
        print(x)
