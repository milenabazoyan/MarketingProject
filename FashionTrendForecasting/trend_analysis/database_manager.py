from FashionTrendForecasting.trend_analysis.config import DATABASE_PATH
import sqlite3


def add_predictions_to_database(database_path, predicted_data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        # Add a new column named "Predictions" to the "Item" table
        cursor.execute("ALTER TABLE Item ADD COLUMN Predictions REAL")

        # Update the "Predictions" column with the predicted data
        for index, row in predicted_data.iterrows():
            cursor.execute("UPDATE Item SET Predictions = ? WHERE item_id = ?", (row['Predictions'], row['item_id']))

        # Commit the changes to the database
        conn.commit()
        print("Predictions added to the database successfully.")
    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        conn.close()



