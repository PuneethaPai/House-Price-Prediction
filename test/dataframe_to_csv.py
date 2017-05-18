import pandas as pd

house_features_dataframe = pd.read_csv("/Users/surajus/Shanbhag/House Price Prediction/kc_house_data.csv")
# print house_features_dataframe
second_house_features_dataframe=house_features_dataframe[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','yr_built','zipcode','price']]
second_house_features_dataframe_10000=second_house_features_dataframe.ix[:10000]
second_house_features_dataframe_10000.to_csv('train_data.csv',index=False,header=False)