import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
from sklearn.linear_model import LinearRegression


# loading the data from csv file to Pandas DataFrame
big_mart_data = pd.read_csv('D:\\Train.csv')
# first 5 rows of the dataframe
big_mart_data.head()
# number of data points & number of features
big_mart_data.shape
# getting some information about thye dataset
big_mart_data.info()
# checking for missing values
big_mart_data.isnull().sum()
# mean value of "Item_Weight" column
big_mart_data['Item_Weight'].mean()
# filling the missing values in "Item_weight column" with "Mean" value
big_mart_data['Item_Weight'].fillna(big_mart_data['Item_Weight'].mean(), inplace=True)
# mode of "Outlet_Size" column
big_mart_data['Outlet_Size'].mode()
# filling the missing values in "Outlet_Size" column with Mode
mode_of_Outlet_size = big_mart_data.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=(lambda x: x.mode()[0]))
print(mode_of_Outlet_size)
miss_values = big_mart_data['Outlet_Size'].isnull() 
#Replacing Null values to mode value of outlet_Size compared to outlet_type  
big_mart_data.loc[miss_values, 'Outlet_Size'] = big_mart_data.loc[miss_values,'Outlet_Type'].apply(lambda x: mode_of_Outlet_size[x])
# checking for missing values
big_mart_data.isnull().sum()
#statistical measures
big_mart_data.describe()
# Item_Weight distribution

# Item Weight distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Weight'])
plt.show()
# Item Visibility distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Visibility'])
plt.show()
# Item MRP distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_MRP'])
plt.show()
# Item_Outlet_Sales distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Outlet_Sales'])
plt.show()
# Outlet_Establishment_Year column
plt.figure(figsize=(6,6))
sns.countplot(x='Outlet_Establishment_Year', data=big_mart_data)
plt.show()
# Item_Fat_Content column
plt.figure(figsize=(6,6))
sns.countplot(x='Item_Fat_Content', data=big_mart_data)
plt.show()
# Item_Type column
plt.figure(figsize=(30,6))
sns.countplot(x='Item_Type', data=big_mart_data)
plt.show()
# Outlet_Size column
plt.figure(figsize=(6,6))
sns.countplot(x='Outlet_Size', data=big_mart_data)
plt.show()

#Data Pre-Processing
big_mart_data['Item_Fat_Content'].value_counts()
big_mart_data.replace({'Item_Fat_Content': {'low fat':'Low Fat','LF':'Low Fat', 'reg':'Regular'}}, inplace=True)
big_mart_data['Item_Fat_Content'].value_counts()

# CATEGORICAL DATA CONVERSION
big_mart_data.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)

encoder = LabelEncoder()
#big_mart_data['Item_Identifier'] = encoder.fit_transform(big_mart_data['Item_Identifier'])

big_mart_data['Item_Fat_Content'] = encoder.fit_transform(big_mart_data['Item_Fat_Content'])

big_mart_data['Item_Type'] = encoder.fit_transform(big_mart_data['Item_Type'])

#big_mart_data['Outlet_Identifier'] = encoder.fit_transform(big_mart_data['Outlet_Identifier'])

big_mart_data['Outlet_Size'] = encoder.fit_transform(big_mart_data['Outlet_Size'])

big_mart_data['Outlet_Location_Type'] = encoder.fit_transform(big_mart_data['Outlet_Location_Type'])

big_mart_data['Outlet_Type'] = encoder.fit_transform(big_mart_data['Outlet_Type'])


big_mart_data.head()

#Splliting the data
X = big_mart_data.drop(columns='Item_Outlet_Sales', axis=1)
Y = big_mart_data['Item_Outlet_Sales']
print(X)
print(Y)

#Splitting the data into Training data & Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
print('\n')

#Machine Learning Model Training



regressor=LinearRegression()
regressor.fit(X_train, Y_train)

# prediction on training data
training_data_prediction = regressor.predict(X_train)
testing_data_prediction = regressor.predict(X_test)
# R squared Value
print('LINEAR REGRESSOR ALGO OUTPUT')
print('')
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R Squared value = ', r2_train)
r2_test = metrics.r2_score(Y_test, testing_data_prediction)
print('R Squared value = ', r2_test)

print('')
print('XG BOOST REGRESSOR ALGO OUTPUT')
print('')
#by using XG boost regressor
reg= XGBRegressor()
reg.fit(X_train, Y_train)
train_data_prediction = reg.predict(X_train)
test_data_prediction = reg.predict(X_test)
# R squared Value
r2_train = metrics.r2_score(Y_train, train_data_prediction)
print('R Squared value = ', r2_train)
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R Squared value = ', r2_test)