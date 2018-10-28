import matplotlib.pyplot as plt
import pandas as pd
from utils import get_male_data
from utils import get_female_data

def main():
    data = pd.read_csv("../data/data.csv") 
    
    male_age,male_height = get_male_data(data)
    female_age,female_height = get_female_data(data)
    
    #creating histogram
    legend = ['Male', 'Female']
    plt.hist([male_age, female_age], color=['Black', 'Red'], bins=50)
    plt.xlabel(' Age Values')
    plt.ylabel('Frequency')
    plt.legend(legend)
    plt.title('Male/Female Age Distribution')
    plt.show()
    
main()
