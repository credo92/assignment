import pandas as pd
from utils import get_male_data
from utils import get_female_data
from utils import create_histogram

def main():
    data = pd.read_csv("../data/data.csv") 
    
    male_age,male_height = get_male_data(data)
    female_age,female_height = get_female_data(data)
    
    plt = create_histogram(male_age, female_age,'Age')
    plt.show()
    
    plt = create_histogram(male_height, female_height,'Height')
    plt.show()
    
main()
