#Database Documentation

##Introduction

This documentation covers the data generation, schema details, CRUD, and Interactions functionality of the FashionTrendForecasting package, which utilizes an SQLite database to store and manage fashion item data and associated sales and trends.

##Data Generation

The data generation scripts use the Faker library to create realistic mock data for a clothing `item`, `material`, `category`, `style`, `color`, `picture_id`, `sales_outcome`, `trend_score`, `search_frequencies`, and `predicted_trend_score` (this is initially set to 0 and is updated after). 

##Database Schema and filling data into it

Creates a separate class for each of the following tables:

1. Item
2. Picture
3. Sales_Outcomes
4. Trend
5. Search_Frequency

Defines connections to other tables from our main Item table.

It uses the following functions:

`random.randint()` for generating numerical data.(sales_volumne, trend_score etc)

`fake.date()` for date data.

`random.choice()` for categorical data (item, season, etc)

It fills everything into an SQLite db file in a separate folder for easier access from different levels.

##SQL Operations

SQL operations are all included in the 'sql_interactions.py' file, which has 2 separate classes, CRUD and Interactions, with the following functions.

##CRUD class functions

1. add_item_with_details(self, item_data: dict) -> bool: Adds new item to the table
2. get_item_data_by_id(self, item_id: int) -> list: Gives item information from item table by the given id
3. get_item_by_id(self, item_id): Gives object from item table by the given id
4. update_item(self, item_id: int, update_data: dict) -> bool: updates item with the given info
5. delete_item(self, item_id: int) -> bool:Deletes item with the given id

##Interactions class functions

1. select_all_as_df(self, table_name: str) -> pd.DataFrame: Returns all rows and columns of the given table.
2. get_seasonal_trend_items_top_n_offset_k(self, season: str, n: int, k: int) -> list: Extracts the top n popular items for a specified season based on trend scores.
3. get_popularity_metrics(self) -> pd.DataFrame: Use the Search_Frequency entity to identify items with the highest search_count, indicating current consumer interest.
4. get_sales_performance(self) -> pd.DataFrame: Functionality: Sales_Outcome to determine which items have the highest sales_volume.
5. get_detailed_item_trends(self) -> pd.DataFrame: Functionality: Returns detailed attributes of items along with their trend score.
6. get_sales_volume(self) -> pd.DataFrame: Functionality: Returns detailed attributes of items along with their sales volume.
7. get_top_n_items_with_highest_sales(self, season: str, n: int) -> pd.DataFrame: Get item with the highest trend score for a given season.



