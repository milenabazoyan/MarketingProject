from sqlalchemy import create_engine, text
import pandas as pd

class CRUD:
    def __init__(self, db_uri='sqlite:///FashionAnalysis_temp.db'):
        self.db_uri = db_uri

    def execute_query(self, query, params=None, read=True):
        engine = create_engine(self.db_uri)
        with engine.connect() as connection:
            if read:
                df = pd.read_sql(query, connection, params=params)
                return df
            else:
                # Ensure the query is explicitly prepared and executed as a text SQL expression
                connection.execute(text(query), params)

    def select_all_as_df(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return self.execute_query(query)

    def insert_into_table(self, table_name, data_dict):
        engine = create_engine('sqlite:///FashionAnalysis_temp.db')
        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join([f":{key}" for key in data_dict.keys()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        return self.execute_query(query, params=data_dict, read=False)

    def update_table(self, table_name, data_dict, condition):
        set_clause = ', '.join([f"{key} = :{key}" for key in data_dict.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        return self.execute_query(query, params=data_dict, read=False)

    def delete_from_table(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        return self.execute_query(query, read=False)

    def select_with_condition_as_df(self, table_name, condition, params):
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        return self.execute_query(query, params=params)


class Interactions:
    def __init__(self, db_uri='sqlite:///FashionAnalysis_temp.db'):
        self.db_uri = db_uri

    def select_all_as_df(table_name):
        engine = create_engine('sqlite:///FashionAnalysis_temp.db')
        with engine.connect() as connection:
            df = pd.read_sql(f"SELECT * FROM {table_name}", connection)
        return df

    def get_seasonal_trend_items(season):
        engine = create_engine('sqlite:///FashionAnalysis_temp.db')
        query = f"""
        SELECT i.category, i.material, SUM(t.trend_score) as total_trend_score
        FROM Trend t
        JOIN Item i ON t.item_id = i.item_id
        WHERE t.season = '{season}'
        GROUP BY t.item_id
        ORDER BY total_trend_score DESC
        LIMIT 3
        """
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df


    def get_popularity_metrics(self):
        engine = create_engine('sqlite:///FashionAnalysis_temp.db')
        query = """
        SELECT i.category, i.material, MAX(sf.search_count) as max_search_count
        FROM Search_Frequency sf
        JOIN Item i ON sf.item_id = i.item_id
        GROUP BY sf.item_id
        ORDER BY max_search_count DESC
        """
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df


    def get_sales_performance(self):
        engine = create_engine('sqlite:///FashionAnalysis_temp.db')
        query = """
        SELECT i.category, i.material, SUM(so.sales_volume) as total_sales_volume
        FROM Sales_Outcome so
        JOIN Item i ON so.item_id = i.item_id
        GROUP BY so.item_id
        ORDER BY total_sales_volume DESC
        """
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df
