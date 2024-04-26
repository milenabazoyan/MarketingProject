# database_manager.py
import sqlite3
import pandas as pd
from FashionTrendForecasting.data_processing.sql_interactions import Interactions
from FashionTrendForecasting.trend_analysis.config import DATABASE_PATH

def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def insert_predictions(data):
    conn = create_connection()
    data.to_sql('predictions', conn, if_exists='append', index=False)
    conn.close()

def fetch_data():
    interactions_instance = Interactions()
    df = interactions_instance.get_sales_volume()
    return df
