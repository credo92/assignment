import pandas as pd
from utils import get_male_data
from utils import get_female_data

def main():
    data = pd.read_csv("../data/data.csv") 
    
    male_age,male_height = get_male_data(data)
    
    female_age =[]
    female_height= []
    
    for index, row in data.iterrows():            
        if row['gender'] == 'F':
            female_age.append(row['age'])
            female_height.append(row['height'])
            print('FEMALE ', row['gender'] , row['age'] , row['height'])
    
    print(male_age)   
    print(male_height)
    
main()
