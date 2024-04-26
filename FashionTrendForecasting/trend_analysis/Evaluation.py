from FashionTrendForecasting.trend_analysis.model import *
from FashionTrendForecasting.data_processing.sql_interactions import Interactions
import numpy as np
sql_interactions_instance = Interactions()
df = sql_interactions_instance.get_sales_volume()

total_rows = len(df)
split_index = int(0.8 * total_rows)
train_data = df.iloc[:split_index]
test_data = df.iloc[split_index:]
X_test = test_data.drop(columns=['trend_score'])
X_train, y_train = split_data(train_data, 'trend_score')
y_pred = train_and_predict(X_train, y_train, X_test)
y_test = test_data['trend_score']

def mape(y_test, y_pred):
    return np.mean(np.abs((y_test - y_pred) / y_test)) * 100
mape_value = mape(y_test, y_pred)
print("MAPE:", mape_value)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted')
plt.scatter(y_test, y_test, color='red', label='Actual')
plt.title('Actual vs. Predicted')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.legend()
plt.show()

'''I will either use linear regression or would try to generate the data in a little different way to get more interesting results.'''

