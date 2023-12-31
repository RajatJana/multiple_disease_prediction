# multiple_disease_prediction



## Overview
This project aims to develop a machine learning-based prediction system for heart disease and diabetes. The system uses a dataset of medical records and employs various machine learning algorithms to predict the likelihood of a patient developing heart disease or diabetes based on their health information.

## Table of Contents
- Introduction
+ Data
- Methodology
+ Dependencies
- Results

## Introduction
Heart disease and diabetes are two prevalent and serious health conditions that affect millions of people worldwide. Early detection and prediction of these conditions can significantly improve patient outcomes. This project aims to create a predictive model that can assist in identifying individuals at risk of heart disease and diabetes based on their medical history and health data.

## Data

The dataset used for this project contains various features such as age, sex, cholesterol levels, blood pressure, and other relevant health metrics. It is essential to preprocess the data to ensure that it is suitable for machine learning algorithms. Data cleaning, feature engineering, and data splitting are performed to prepare the dataset for training and evaluation.

Kaggle : 

- https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset
- https://www.kaggle.com/datasets/mathchi/diabetes-data-set

## Methodology

The project utilizes a supervised machine learning approach to build predictive models for heart disease and diabetes. Several classification algorithms are experimented with, including:

Logistic Regression

Support Vector Machine (SVM)

Cross-validation techniques and hyperparameter tuning are applied to optimize the models' performance.

## Dependencies
To run this project, you will need the following dependencies:

 Python (>=3.6)
 
 NumPy
 
 pandas
 
 scikit-learn

You can install these dependencies using pip:

`_
pip install numpy pandas scikit-learn tensorflow matplotlib
_`

## Results

Accuracy : Heart Disease : Test data : 81% & Train data : 85%

                           

Accuracy : Diabetes : Test data : 77% & Train data : 78%

                     
   
The project is deployed in Streamlit : https://multiplediseaseprediction-rajatjana.streamlit.app/

![Screenshot (80)](https://github.com/RajatJana/multiple_disease_prediction/assets/75692637/1204910d-b364-4ee7-91a1-5249d2c7f876)

![Screenshot (81)](https://github.com/RajatJana/multiple_disease_prediction/assets/75692637/92829113-331f-4d8b-a210-8a52b606799d)

![Screenshot (82)](https://github.com/RajatJana/multiple_disease_prediction/assets/75692637/02e553aa-6864-449f-bf95-d1d206d6f28e)
