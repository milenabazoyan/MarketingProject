# FashionTrendForecasting: Sustainable Fashion Trend Analysis

## Project Objective
FashionTrendForecasting aims to address the rapidly changing trends in the fashion industry, focusing particularly on sustainability and personalization. By leveraging advanced data analytics and machine learning algorithms, this Python package helps fashion brands dynamically adapt their product development cycles to meet consumer demands efficiently. Our model predicts emerging trends by analyzing real-time data from social media, sales channels, and consumer feedback, enabling brands to respond with agility. The methodology includes comprehensive data collection, AI-driven trend analysis, and implementation strategies that emphasize sustainable and ethical production practices. FashionTrendFarecasting is designed to enhance the capability of fashion brands to maintain profitability while prioritizing environmental consciousness and personalized consumer experiences.

## Installation
To install FashionTrendForecasting, use the following pip command:

```bash
pip install FashionTrendForecasting==0.1.0
```

For more details, updates, and versions, please visit our project on PyPI:
[FashionTrendForecasting on PyPI]( "(https://pypi.org/project/FashionTrendForecasting/0.1.0/)")


## License
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.


## Getting Started

To run the project, follow these steps:

1. **Install Dependencies**:
   Install all required packages using the command below:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Application**:
   Start the application by running:
   ```bash
   python run.py
   ```
3. **Access the Application**:
   - **Open the Application**: Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
   - **API Documentation**: To access the API documentation, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). 


```
# FashionTrendForecasting: Sustainable Fashion Trend Analysis

## Project Objective
FashionTrendForecasting aims to address the rapidly changing trends in the fashion industry, focusing particularly on sustainability and personalization. By leveraging advanced data analytics and machine learning algorithms, this Python package helps fashion brands dynamically adapt their product development cycles to meet consumer demands efficiently. Our model predicts emerging trends by analyzing real-time data from social media, sales channels, and consumer feedback, enabling brands to respond with agility. The methodology includes comprehensive data collection, AI-driven trend analysis, and implementation strategies that emphasize sustainable and ethical production practices. EcoTrendz is designed to enhance the capability of fashion brands to maintain profitability while prioritizing environmental consciousness and personalized consumer experiences.

## Installation
To install FashionTrendForecasting, use the following pip command:

```bash
pip install FashionTrendForecasting==0.1.0
```
## Trend Analysis

### Folder Structure

- **simple_model.py**: Contains functions to evaluate different machine learning models by training and testing them, then giving a mean squared error.
- **model.py**: Contains functions to train machine learning models on the whole dataset and make predictions.

### Description

- **simple_model.py**: Provides functions to split data and evaluate models like Random Forest, Decision Tree, and Gradient Boosting.
  - `split_data`: Splits the data into features and targets.
  - `train_random_forest`, `train_decision_tree`, `train_gradient_boosting`: Train Random Forest, Decision Tree, and Gradient Boosting models respectively, and return mean squared error.

- **model.py**: Uses pipelines to preprocess categorical features before training the models.
  - `train_and_predict_rf`, `train_and_predict_dt`, `train_and_predict_gb`: Train and make predictions using Random Forest, Decision Tree, and Gradient Boosting models respectively.

### Usage

#### Training Models/ Evaluate them:

Use `simple_model.py` to train machine learning models on your fashion trend data and evaluate them.
Pass the appropriate data and parameters to the functions based on your requirements.

#### Predictions:

Use `model.py` to train machine learning models on your fashion trend data and make predictions on the model chosen by you from the evaluations in `simple_model.py`.

### Examples


## Example: Training and evaluating a Random Forest model
### Step 1: Import Required Libraries

```python
from FashionTrendForecasting.trend_analysis.Simple_Model import * 
import pandas as pd  
```

In this step, we import the necessary modules from the FashionTrendForecasting package and the pandas library.

### Step 2: Prepare the Data

```python
df = pd.DataFrame
```

Here, we create a pandas DataFrame named `df`. This DataFrame represents the dataset on which we want to train the Random Forest model.

### Step 3: Train and Evaluate the Random Forest Model

```python
rf_model, rf_mse = train_random_forest(df, test_size=0.2, random_state=42) 
```

We call the `train_random_forest()` function to train a Random Forest model on the provided dataset (`df`). The `test_size` parameter specifies the proportion of the dataset to include in the test split, and the `random_state` parameter ensures reproducibility of the results. The function returns the trained Random Forest model (`rf_model`) and the mean squared error (`rf_mse`) of the model.

## Example: Making predictions using a Random Forest model

### Step 1: Import Required Libraries

```python
from FashionTrendForecasting.trend_analysis.model import * 
```

Here, we import the necessary modules from the FashionTrendForecasting package.

### Step 2: Prepare the Data

```python
df = pd.DataFrame
```

Similarly, we create a pandas DataFrame named `df` to represent the dataset on which we want to make predictions.

### Step 3: Split Data and Make Predictions

```python
X_train, y_train = split_data(df, 'trend_score')
y_pred_rf = train_and_predict_rf(X_train, y_train, df, n_estimators=100, random_state=42)
```

We use the `split_data()` function to split the dataset into features (`X_train`) and target variable (`y_train`) based on the column `'trend_score'`.
```
```
# Database Documentation

## Introduction
This documentation covers the data generation, schema details, CRUD, and Interactions functionality of the FashionTrendForecasting package, which utilizes an SQLite database to store and manage fashion item data and associated sales and trends.

## Data Generation
The data generation scripts use the Faker library to create realistic mock data for clothing items, including material, category, style, color, picture ID, sales outcomes, trend score, search frequencies, and predicted trend score (initially set to 0 and updated later).

## Database Schema and Filling Data Into It
Creates a separate class for each of the following tables:
- Item
- Picture
- Sales_Outcomes
- Trend
- Search_Frequency

Defines connections to other tables from our main Item table.
It uses the following functions:
- `random.randint()` for generating numerical data (sales volume, trend score, etc.)
- `fake.date()` for date data.
- `random.choice()` for categorical data (item, season, etc.)

It fills everything into an SQLite db file in a separate folder for easier access from different levels.

## SQL Operations
SQL operations are all included in the 'sql_interactions.py' file, which has 2 separate classes, CRUD and Interactions, with the following functions.

### CRUD class functions
- `add_item_with_details(self, item_data: dict) -> bool`: Adds new item to the table
- `get_item_data_by_id(self, item_id: int) -> list`: Gives item information from item table by the given id
- `get_item_by_id(self, item_id)`: Gives object from item table by the given id
- `update_item(self, item_id: int, update_data: dict) -> bool`: updates item with the given info
- `delete_item(self, item_id: int) -> bool`: Deletes item with the given id

### Interactions class functions
- `select_all_as_df(self, table_name: str) -> pd.DataFrame`: Returns all rows and columns of the given table.
- `get_seasonal_trend_items_top_n_offset_k(self, season: str, n: int, k: int) -> list`: Extracts the top n popular items for a specified season based on trend scores.
- `get_popularity_metrics(self) -> pd.DataFrame`: Use the Search_Frequency entity to identify items with the highest search count, indicating current consumer interest.
- `get_sales_performance(self) -> pd.DataFrame`: Functionality: Sales_Outcome to determine which items have the highest sales volume.
- `get_detailed_item_trends(self) -> pd.DataFrame`: Functionality: Returns detailed attributes of items along with their trend score.
- `get_sales_volume(self) -> pd.DataFrame`: Functionality: Returns detailed attributes of items along with their sales volume.
- `get_top_n_items_with_highest_sales(self, season: str, n: int) -> pd.DataFrame`: Get item with the highest trend score for a given season.
```
