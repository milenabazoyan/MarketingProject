from database_processing.sql_interactions import Interactions
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import pandas as pd


sql_interactions_instance = Interactions()
df = sql_interactions_instance.get_detailed_item_trends()

X = df[['category', 'material', 'style', 'color']]
y = df['trend_score']
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
mse_dt = mean_squared_error(y_test, y_pred_dt)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error for Decision Tree: {mse_dt}")
print(f"Mean Squared Error for Random Forest: {mse}")
