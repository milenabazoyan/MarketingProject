from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

def train_random_forest(df):
    X = df[['category', 'material', 'style', 'color']]
    y = df['trend_score']
    X = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    y_pred = rf.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return rf, mse

def train_decision_tree(df):
    X = df[['category', 'material', 'style', 'color']]
    y = df['trend_score']
    X = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    dt = DecisionTreeRegressor(random_state=42)
    dt.fit(X_train, y_train)
    
    y_pred = dt.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return dt, mse
