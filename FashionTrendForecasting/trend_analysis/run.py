from FashionTrendForecasting.trend_analysis.model import *
from FashionTrendForecasting.data_processing.sql_interactions import Interactions
import pandas as pd

# Define the new data
new_data = {
    'category': ['pants', 'shirt', 'shoes'],
    'material': ['cotton', 'leather', 'denim'],
    'style': ['casual', 'formal', 'sportswear'],
    'color': ['blue', 'black', 'red'],
    'sales_volume': [200, 150, 100]
}
new_data = pd.DataFrame(new_data)

sql_interactions_instance = Interactions()
df = sql_interactions_instance.get_sales_volume()
X_train, y_train = split_data(df, 'trend_score')
y_pred = train_and_predict(X_train, y_train, new_data)
print(y_pred)