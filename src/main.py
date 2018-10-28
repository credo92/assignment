import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("../data/data.csv") 
    
    for index, row in data.iterrows():
        if row['gender'] == 'M':
            print('MALE ',row['gender'] , row['age'] , row['height'])    
        if row['gender'] == 'F':    
            print('FEMALE ', row['gender'] , row['age'] , row['height'])
main()
