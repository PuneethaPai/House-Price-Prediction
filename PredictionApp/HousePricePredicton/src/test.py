import pandas as pd
import numpy as np
data_dict = {'bedrooms': float(1), 'bathrooms': float(2), 'sqft_living': float(3), 'sqft_lot': float(4),
                         'floors': float(5), 'yr_built': float(6), 'zipcode': float(7)}
print pd.DataFrame(np.reshape(data_dict.values(),[1,7]),columns=data_dict.keys(),dtype=float)
