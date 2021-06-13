import pandas as pd
from datetime import datetime
import numpy as np

# Reading the data
data = pd.read_excel('Birthdays.xlsx')
data = data[data['Birth'].notna()]

# Turning days and months to integers
days = data.Birth.dt.day
months = data.Birth.dt.month
data['days'] = days
data['months'] = months
data.days = data.days.map(int)
data.months = data.months.map(int)

# Identification of the present day and month
day = int(datetime.now().strftime('%d'))
month = int(datetime.now().strftime('%m'))

## Testes
# day = 15
# month = 6


# Function that returns a list of Birth dates today
def Birthday_today():


    check = data.loc[(data.days == day) & (data.months == month)]
    lista_contatos = np.array(check['Telephone'])
    birthday_list = np.array(check['Name'])


    return birthday_list, lista_contatos


# Function that returns the next birthday
def next_Birthday():

    # Find people that will still have birthday the same year
    check_two = data.loc[(data.days > day) & (data.months >= month)]

    if not (check_two.empty):

        # Get next birthday in the same year
        next_birthday = check_two.sort_values(['months','days'], ascending=True).iloc[0].Birth
        
    else:
        # Get first birthday of the next year
        next_birthday = data.sort_values(['months','days'], ascending=True).iloc[0].Birth

    return next_birthday  
