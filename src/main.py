import pandas as pd
from src.utils import get_male_data
from src.utils import get_female_data

def main():
    data = pd.read_csv("../data/data.csv") 
    
    male_age =[]
    male_height= []
    
    female_age =[]
    female_height= []
    
    for index, row in data.iterrows():
        if row['gender'] == 'M':
            male_age.append(row['age'])
            male_height.append(row['height'])
            print('MALE ',row['gender'] , row['age'] , row['height'])
            
        if row['gender'] == 'F':
            female_age.append(row['age'])
            female_height.append(row['height'])
            print('FEMALE ', row['gender'] , row['age'] , row['height'])
main()
