import pandas as pd
from utils import get_male_data
from utils import get_female_data

def main():
    data = pd.read_csv("../data/data.csv") 
    
    male_age,male_height = get_male_data(data)
    female_age,female_height = get_female_data(data)

    print(female_age)   
    print(female_height)
    
main()
