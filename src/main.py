import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv("../data/data.csv") 
    
    for index, row in data.iterrows():
        print(row['gender'] , row['age'] , row['height'])
main()
