import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

house_features_dataframe = pd.read_csv("../../../kc_house_data.csv")
Y = house_features_dataframe.as_matrix(['price'])
# house_features_dataframe.drop(['price', 'date'], inplace=True, axis=1)
X = house_features_dataframe.as_matrix(['bedrooms','bathrooms','sqft_living','sqft_lot','floors','yr_built','zipcode'])
X_train, X_test, y_train, y_test = np.asarray(train_test_split(X, Y, test_size=0.2))
model = LinearRegression()
model.fit(X_train, y_train)
print "Score:", model.score(X_test, y_test)
filename = 'house_price_prediction_model.sav'
pickle.dump(model, open(filename, 'wb'))
