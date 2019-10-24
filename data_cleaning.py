import numpy as np
import pandas as pd


def read_data():
    data = pd.read_csv('C:/Users/ameya/CSC522Project-AirBnbPricePrediction/data/AB_NYC_2019.csv')
    return data

def remove_attributes(df):
    df.drop('name', axis=1, inplace=True)
    df.drop('host_id', axis=1, inplace=True)
    df.drop('host_name', axis=1, inplace=True)
    df.drop('number_of_reviews', axis=1, inplace=True)
    df.drop('last_review', axis=1, inplace=True)
    df.drop('reviews_per_month', axis=1, inplace=True)
    return df

def remove_price_outliers(df):
    df_new = df.drop(df[(df['price'] == 0)].index)
    return df_new

data = read_data()
data = remove_attributes(data)
data = remove_price_outliers(data)
#print(data)

data.to_csv('Data_preprocessed')