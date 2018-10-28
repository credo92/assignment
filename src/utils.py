import matplotlib.pyplot as plt

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


def create_histogram(male_data, female_data):
    legend = ['Male', 'Female']
    plt.hist([male_data, female_data], color=['Black', 'Red'], bins=20)
    plt.xlabel('Age Values')
    plt.ylabel('Frequency')
    plt.legend(legend)
    plt.title('Male/Female Age Distribution')
    return plt