#Model

##Files

- simple_model.py: This file contains functions to evaluate different machine learning models by train, testing the models then giving a mean squared error.
- model.py: This file contains functions to train machine learning models on the whole dataset and make predictions.

##Description

###simple_model.py:

- Provides functions to split data and evaluate models like Random Forest, Decision Tree, and Gradient Boosting.
- The `split_data` function splits the data into features and targets.
- The `train_random_forest`, `train_decision_tree`, and `train_gradient_boosting` functions train Random Forest, Decision Tree, and Gradient Boosting models respectively, and return  mean squared error.

###model.py:
- Uses pipelines to preprocess categorical features before training the models.
- Provides functions to train and make predictions using Random Forest, Decision Tree, and Gradient Boosting models (`train_and_predict_rf`, `train_and_predict_dt`, `train_and_predict_gb`)

##Usage

- Training Models/ Evaluate them:

Use the `simple_model.py` to train machine learning models on your fashion trend data and evaluate it.

Pass the appropriate data and parameters to the functions based on your requirements.

- Predictions:

Use the `model.py` to train machine learning models on your fashion trend data and make predictions on the model chosen by you from the evaluations in the `simple_model.py`.

##Example Usage

###Trend Analysis  

####Folder Structure  

- **simple_model.py**: Contains functions to evaluate different machine learning models by training and testing them, then giving a mean squared error. 

- **model.py**: Contains functions to train machine learning models on the whole dataset and make predictions.  

#### Description  

- **simple_model.py**: Provides functions to split data and evaluate models like Random Forest, Decision Tree, and Gradient Boosting.  

- `split_data`: Splits the data into features and targets. 

- `train_random_forest`, `train_decision_tree`, `train_gradient_boosting`: Train Random Forest, Decision Tree, and Gradient Boosting models respectively, and return mean squared error. 

- **model.py**: Uses pipelines to preprocess categorical features before training the models. 

- `train_and_predict_rf`, `train_and_predict_dt`, `train_and_predict_gb`: Train and make predictions using Random Forest, Decision Tree, and Gradient Boosting models respectively.  

#### Usage  


##### Training Models/ Evaluate them:  

Use `simple_model.py` to train machine learning models on your fashion trend data and evaluate them. Pass the appropriate data and parameters to the functions based on your requirements.  

##### Predictions: 
 Use `model.py` to train machine learning models on your fashion trend data and make predictions on the model chosen by you from the evaluations in `simple_model.py`.  


### Example: Training and evaluating a Random Forest model  

#### Step 1: Import Required Libraries  
```py

from FashionTrendForecasting.trend_analysis.Simple_Model import *  

import pandas as pd   
```  

In this step, we import the necessary modules from the FashionTrendForecasting package and the pandas library.  

#### Step 2: Prepare the Data  

```py

python df = pd.DataFrame 

```  
Here, we create a pandas DataFrame named `df`. This DataFrame represents the dataset on which we want to train the Random Forest model.  

#### Step 3: Train and Evaluate the Random Forest Model 

```py

rf_model, rf_mse = train_random_forest(df, test_size=0.2, random_state=42) 

``` 
We call the `train_random_forest()` function to train a Random Forest model on the provided dataset (`df`). The `test_size` parameter specifies the proportion of the dataset to include in the test split, and the `random_state` parameter ensures reproducibility of the results. The function returns the trained Random Forest model (`rf_model`) and the mean squared error (`rf_mse`) of the model. 

### Example: Making predictions using a Random Forest model 

#### Step 1: Import Required Libraries 

```py

from FashionTrendForecasting.trend_analysis.model import *  

``` 
Here, we import the necessary modules from the FashionTrendForecasting package.  

#### Step 2: Prepare the Data 

 ```python df = pd.DataFrame ```  

Similarly, we create a pandas DataFrame named `df` to represent the dataset on which we want to make predictions. 

#### Step 3: Split Data and Make Predictions  

```py

X_train, y_train = split_data(df, 'trend_score') y_pred_rf = train_and_predict_rf(X_train, y_train, df, n_estimators=100, random_state=42) 
 
```  

We use the `split_data()` function to split the dataset into features (`X_train`) and target variable (`y_train`) based on the column `'trend_score'`. 













