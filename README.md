# Property-Valuation

#### • A Machine Learning Web App created with Flask.
#### • Do ⭐ the repository if it helped you in anyway.

## Preview

https://user-images.githubusercontent.com/65092456/115704250-c4f1e900-a388-11eb-86e6-70aff442385d.mp4


## Overview

A platform to help property owners to know the best sale price for their estate based on Machine Learning models. The project is aimed at valuating properties of Tier 1 cities.

## Data Scource and Description

The data is scrapped from nobroker.com website using BeautifulSsoup and Selenium tool.
The data consist of records for 10,000 properties from tier 1 cities. In total there are 17 variables. 

## Model Selection

To fit the data, the regress models that we wish to compare are Linear Regression, Lasso Regression, KNN regressor and Random Forest regressor. 
I have split the entire data frame into 80% Training Set and 20% Test set, where I hold out the Test Set for final model evaluation. 
Using the models with best score I have further deployed the app.
