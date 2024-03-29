import pandas as pd
import matplotlib.pyplot as plt
from src.utils import get_male_data
from src.utils import get_female_data
from src.utils import create_histogram

#test data
test_dict = {
              'gender'  : pd.Series(['M','F','F']),
              'age'    : pd.Series([32.0,36.0,35.0]),
              'height' : pd.Series([1.72,1.64,1.68])
             }
# conver to df so we can extract female and male data lists from df
# using util functins

test_data = pd.DataFrame(test_dict)
test_male_age, test_male_height = get_male_data(test_data)
test_female_age, test_female_height = get_female_data(test_data)
# for test histogram
legend = ['Male', 'Female']

def test_get_male_data(): 
    assert len(test_male_age) == 1 and len(test_male_height) == 1 and  test_male_age == [32.0] and test_male_height == [1.72]
    
def test_get_female_data(): 
    assert len(test_female_age) == 2 and len(test_female_height) == 2 and  test_female_age == [36.0,35.0] and test_female_height == [1.64,1.68]
    
def test_create_histogram_age_Distribution():
    plt.hist([test_male_age, test_female_age], color=['Black', 'Red'], bins=20)
    plt.xlabel('Age' + " Values") # arg 
    plt.ylabel("Frequency")
    plt.legend(legend)
    plt.title('Male/Female '+ 'Age' +' Distribution') 
    
    test_plt_age = create_histogram(test_male_age, test_female_age, 'Age')
    assert plt == test_plt_age
    
def test_create_histogram_height_Distribution():
    plt.hist([test_male_height, test_female_height], color=['Black', 'Red'], bins=20)
    plt.xlabel('Height' + " Values") # arg 
    plt.ylabel("Frequency")
    plt.legend(legend)
    plt.title('Male/Female '+ 'Height' +' Distribution') 
    
    test_plt_height = create_histogram(test_male_age, test_female_age, 'Height')
    assert plt == test_plt_height
    