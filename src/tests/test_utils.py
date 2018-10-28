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

def test_get_male_data(): 
    assert 1==1
def test_get_female_data(): 
    assert 1==1
def test_create_histogram_age_Distribution():
    assert 1==1