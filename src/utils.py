def get_male_data(data):
    male_age =[]
    male_height= []
    
    for index,row in data.iterrows():
        if row['gender'] == 'M':
            male_age.append(row['age'])
            male_height.append(row['height'])
    
    return male_age, male_height
    

def get_female_data(data):
    female_age = []
    female_height = []
    
    for index, row in data.iterrows():
        if row['gender'] == 'F':
            female_age.append(row['age'])
            female_height.append(row['height'])
    
    return female_age, female_height