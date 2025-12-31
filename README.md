Housing Price Prediction

Project Overview
This project focuses on predicting house prices using a machine learning regression model.
The model is trained on the Kaggle “House Prices – Advanced Regression Techniques” dataset.
The purpose of this project is to understand regression, feature selection, and prediction
using Python.

Objectives
The main objectives of this project are:
- To predict house prices based on selected features
- To apply Linear Regression on real-world data
- To visualize actual and predicted house prices
- To gain practical experience with Python and machine learning

Dataset
Source: Kaggle – House Prices: Advanced Regression Techniques  
File used: train.csv  
Target variable: SalePrice

Selected Features
The following features are used for prediction:
- GrLivArea (Above ground living area)
- OverallQual (Overall quality of the house)
- BedroomAbvGr (Number of bedrooms)
- FullBath (Number of full bathrooms)
- GarageCars (Garage capacity)

These features were selected because they have a strong impact on house prices
and are easy to interpret.

Tools and Technologies
Programming Language:
- Python

Libraries:
- pandas
- matplotlib
- scikit-learn

Methodology
First, the dataset is loaded using pandas.
Relevant numerical features are selected from the dataset.
The data is split into training and testing sets.
A Linear Regression model is trained on the training data.
The model predicts house prices on test data.
The results are visualized using a scatter plot comparing actual and predicted prices.

Output
The output of this project includes:
- Predicted house prices
- A graph showing actual prices versus predicted prices

How to Run the Project
1. Place train.csv in the project folder
2. Open terminal or PowerShell in the project directory
3. Run the following command:
   python train.py
4. A graph window will appear showing the prediction results

Project Structure
Housing-Price-Prediction
│
├── train.py
├── train.csv
└── README.md

Group Information
Group No: 02

Maryam Khan – 2023-UAM-2268  
Muneeb Ur Rahman – 2023-UAM-2228  
Arslan Zafar – 2023-UAM-2225  
Sadaf Javed – 2023-UAM-2234  
Bushra Kanwal – 2023-UAM-2238  
Afifa Shafiq – 2023-UAM-227

Conclusion
This project demonstrates the use of Linear Regression for house price prediction.
The model successfully learns patterns from the dataset and provides reasonable
predictions. The visualization helps in evaluating the performance of the model.
