from sqlalchemy import create_engine, text
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from creating_tables_and_filling_data import Item, Picture, Sales_Outcome, Trend, Search_Frequency
from insert_data import item_record

class CRUD:
    def __init__(self, db_uri='sqlite:///FashionAnalysis.db'):
        self.engine = create_engine(db_uri)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_item_with_details(self, item_data):
        try:
            # Create the main Item record
            new_item = Item(**{key: value for key, value in item_data.items() if key in Item.__table__.columns})
            self.session.add(new_item)
            self.session.flush()  # Flush to assign an ID to new_item without committing the transaction

            # Add Picture, if present
            if 'picture' in item_data:
                new_picture = Picture(**item_data['picture'], items=[new_item])
                self.session.add(new_picture)

            # Add related Sales_Outcome records, if present
            for sale_data in item_data.get('sales_outcomes', []):
                new_sale = Sales_Outcome(**sale_data, item_id=new_item.item_id)
                self.session.add(new_sale)

            # Add related Trend records, if present
            for trend_data in item_data.get('trends', []):
                new_trend = Trend(**trend_data, item_id=new_item.item_id)
                self.session.add(new_trend)

            # Add related Search_Frequency records, if present
            for search_data in item_data.get('search_frequencies', []):
                new_search = Search_Frequency(**search_data, item_id=new_item.item_id)
                self.session.add(new_search)

            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error adding item: {e}")
            return False

    def get_items(self):
        try:
            return self.session.query(Item).all()
        except SQLAlchemyError as e:
            print(f"Error retrieving items: {e}")
            return []

    def get_item_by_id(self, item_id):
        res = None
        try:
            res = self.session.query(Item).filter(Item.item_id == item_id).one_or_none()
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error getting item with id {item_id}: {e}")
        return res

    def update_item(self, item_id, update_data):
        try:
            self.session.query(Item).filter(Item.item_id == item_id).update(update_data)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error updating item: {e}")
            return False

    def delete_item(self, item_id):
        try:
            item_to_delete = self.session.query(Item).filter(Item.item_id == item_id).one()
            self.session.delete(item_to_delete)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error deleting item: {e}")
            return False


class Interactions:
    def __init__(self, db_uri='sqlite:///FashionAnalysis.db'):
        self.db_uri = db_uri

    def select_all_as_df(table_name):
        engine = create_engine('sqlite:///FashionAnalysis.db')
        with engine.connect() as connection:
            df = pd.read_sql(f"SELECT * FROM {table_name}", connection)
        return df

    def get_seasonal_trend_items(season):
        '''
        Seasonal Trend Items:
        Functionality: Trend data to extract the 3 most popular items for a specified season
        '''

        engine = create_engine('sqlite:///FashionAnalysis.db')
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
        '''
        Popularity Metrics:
        Functionality: Use the Search_Frequency entity to identify items with the highest search_count, indicating current consumer interest.
        '''

        engine = create_engine('sqlite:///FashionAnalysis.db')
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
        '''
        PSales Performance:
        Functionality: Sales_Outcome to determine which items have the highest sales_volume.
        '''
        engine = create_engine('sqlite:///FashionAnalysis.db')
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

    def get_detailed_item_trends(self):
        '''
        Detailed Item Trends:
        Functionality: Returns detailed attributes of items along with their trend score.
        '''
        engine = create_engine('sqlite:///FashionAnalysis.db')
        query = """
        SELECT i.category, i.material, i.style, i.color, SUM(t.trend_score) as trend_score
        FROM Item i
        JOIN Trend t ON i.item_id = t.item_id
        GROUP BY i.item_id
        ORDER BY trend_score DESC
        """
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df

    def get_sales_volume(self):
        '''
        Detailed Item Trends:
        Functionality: Returns detailed attributes of items along with their trend score.
        '''
        engine = create_engine('sqlite:///FashionAnalysis.db')
        query = """
        SELECT i.category, i.material, i.style, i.color, t.season, SUM(s.sales_volume) as sales_volume
        FROM Item i
        JOIN Trend t ON i.item_id = t.item_id
        JOIN Sales_Outcome s ON i.item_id = s.item_id
        GROUP BY i.item_id
        ORDER BY sales_volume DESC
        """
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df


if __name__ == '__main__':
    crud_obj = CRUD()
    print("testing insert operation")

    if crud_obj.add_item_with_details(item_record):
        print("PASS: New row inserted")
    else:
        print("FAIL: new row was not inserted")

    A = crud_obj.get_items()

    print("testing update operation")

    update_data = {
        "name": "Vintage pants",
        "category": "pants",
        "material": "linen"
    }
    if crud_obj.update_item(100, update_data):
        print("PASS: Updated successfully")
    else:
        print("FAILS: Was not updates")

    print("testing delete operation")

    if crud_obj.delete_item(5):
        print("PASS: object deleted")
    else:
        print("FAIL: object was not deleted")
