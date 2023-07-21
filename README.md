# Big-Mart-Sales-Prediction-with-Python
# Big Mart Sales Prediction

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This project aims to predict the sales of products in Big Mart outlets using machine learning algorithms. It involves data analysis, preprocessing, and model training to create predictive models for sales.

## Table of Contents

- [Big Mart Sales Prediction](#big-mart-sales-prediction)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data](#data)
  - [Features](#features)
  - [Data Preprocessing](#data-preprocessing)
  - [Machine Learning Model Training](#machine-learning-model-training)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/IAMMDDANISHEQBAL/big-mart-sales-prediction.git
   cd big-mart-sales-prediction
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
Usage
Once the installation is complete and the dataset is available, you can run the main script "big_mart_sales_prediction.py" to perform data analysis, preprocessing, and model training.
python Big_Mart_sales_prediction_using_Python.py
The script will display various visualizations, including histograms and count plots, to explore the data distribution and relationships. It will then preprocess the data, handle missing values, and convert categorical data into numerical format. Finally, it will train two regression models - Linear Regression and XGBoost Regression, to predict the sales.

Data
The dataset used in this project is stored in the file "Train.csv". It contains information about various products sold in Big Mart outlets, along with their sales data. If you have a different dataset or want to use real-time data, make sure to format it appropriately for the code to work correctly.

Features
The main features of this project are as follows:

Data analysis and visualization to understand the dataset.
Data preprocessing, handling missing values, and converting categorical data into numerical format.
Training two regression models - Linear Regression and XGBoost Regression.
Predicting sales for Big Mart products using the trained models.
Data Preprocessing
The data preprocessing steps include:

Handling missing values in the "Item_Weight" and "Outlet_Size" columns.
Converting the "Item_Fat_Content," "Item_Type," "Outlet_Size," "Outlet_Location_Type," and "Outlet_Type" columns into numerical values using LabelEncoder.
Machine Learning Model Training
Two regression models are trained in this project:

Linear Regression: It uses the LinearRegression algorithm from scikit-learn.

XGBoost Regression: It utilizes the XGBRegressor algorithm from the XGBoost library.

Results
The results of the trained models are evaluated using R-squared values. The R-squared values on both the training and testing data are displayed.

Contributing
Contributions to this project are welcome! If you find any bugs, have suggestions, or want to add new features, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or questions, please contact [md.danish.eqbal.fiem.csds20@teamfuture.in].

Thank you for using Big Mart Sales Prediction! Happy modeling!

