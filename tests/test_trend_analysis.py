from FashionTrendForecasting.trend_analysis.model import *
from sklearn.model_selection import train_test_split
from FashionTrendForecasting.data_processing.sql_interactions import Interactions
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

def split_data(data, target_feature, test_size=0.2, random_state=42):
    # Separate target variable
    y = data[target_feature]

    # Extract features
    X = data.drop(columns=[target_feature])

    # Identify categorical features
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()

    # One-hot encode categorical features
    X_encoded = pd.get_dummies(X, columns=categorical_features, drop_first=True)

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test


sql_interactions_instance = Interactions()
df = sql_interactions_instance.get_sales_volume()
X_train, X_test, y_train, y_test = split_data(df, 'trend_score')
y_pred = train_and_predict(X_train, y_train, X_test)


def mae(y_test, y_pred):
    return mean_absolute_error(y_test, y_pred)

mae_value = mae(y_test, y_pred)
print("MAE:", mae_value)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted')
plt.scatter(y_test, y_test, color='red', label='Actual')
plt.title('Actual vs. Predicted')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.legend()
plt.show()
