# Why numpy array over python list?
# 1. Many more functions available
# 2. Speed/performance, because numpy saves items of the array next to eachother in memory, 
# while plain python uses pointers to different locations. The result is that you can only store one
# data type within the numpy array (while more than one in a plain list). (Another reason is vectorization)

# What are pandas series?
# One-dimensional
# Able to store different dtypes per cell

# Parameters van een functie verwachten argumenten!

# Logging levels: Allow us to specify what we want to log, by seperating into categories.
# 5 standard logging levels: debug, info, warning, error, critical
# default logging level is warning and higher. So you wont see lower.

import pandas as pd
import numpy as np
import logging
import warnings
from pandas import Series, DataFrame
import datetime

logging.basicConfig(level=logging.INFO, filename='test.log')
warnings.filterwarnings("ignore")

def create_data():
    """Creating the data for this program"""
    return {
        "naam": ['niels', 'paula', 'jan', 'wil'],
        "club": ['ajax', 'feyenoord', 'sdvb', 'vvb'],
        "leeftijd": [33, 30, 69, 65],
        "punten": [100, 105, 103, 110],
        }

def dataframer(data: dict) -> DataFrame:
    """Creating a dataframe out of a dictionary"""
    return DataFrame(data)

def name_extender(df: DataFrame) -> DataFrame:
    """Should add the last name to the name variable"""
    for i in range(len(df)):
        df['naam'][i] = df['naam'][i] + ' anbeek'

def add_points(df: DataFrame) -> DataFrame:
    """Adds 10 points to all people"""
    for i in range(len(df)):
        df['punten'][i] += 10

if __name__ == '__main__':
#    data = name_extender(data)
#    print(data)

    logging.info(f'\n\n Starting {__name__} @' + datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S"))
    df = create_data()
    logging.info('data created')
    df = dataframer(df)
    logging.info('data turned into data frame')
    df.pipe(name_extender)
    logging.info('names are extended')
    df.pipe(add_points)
    logging.info('Added 10 points each')
    print(df)
    logging.info('End of script @' + datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S"))


