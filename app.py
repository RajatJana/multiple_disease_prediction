# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 01:32:30 2023

@author: RAJAT JANA
"""

import pickle
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("./models/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("./models/heart_disease_model.sav",'rb'))


# sidebar for navigation
with st.sidebar:
   
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Home','Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['house','activity','heart'],
                          default_index=0)
    
if (selected == 'Home'):
    
   img0 = Image.open("./images/main.png")
   img0 = img0.resize((400,100))
   st.image(img0,use_column_width=True)
   
   st.title('Welome to Multiple Disease Prediction System using Machine Learning')    
   
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    img1 = Image.open("./images/d_logo.png")
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    img2 = Image.open("./images/h_logo.png")
    img2 = img2.resize((156,145))
    st.image(img2,use_column_width=False)
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex_display = ('Female','Male')
        sex_options = list(range(len(sex_display)))
        sex = st.selectbox("Sex",sex_options, format_func=lambda x: sex_display[x])
        
    with col3:
        cp_display = ('typical angina','atypical angina','non-anginal pain','asymptomatic')
        cp_options = list(range(len(cp_display)))
        cp = st.selectbox("Chest Pain types",cp_options, format_func=lambda x: cp_display[x])
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs_display = ('False','True')
        fbs_options = list(range(len(fbs_display)))
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",fbs_options, format_func=lambda x: fbs_display[x])
        
    with col1:
        restecg_display = ('0','1','2')
        restecg_options = list(range(len(restecg_display)))
        restecg = st.selectbox("Resting Electrocardiographic results",restecg_options, format_func=lambda x: restecg_display[x])
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang_display = ('No','Yes')
        exang_options = list(range(len(exang_display)))
        exang = st.selectbox("Exercise Induced Angina",exang_options, format_func=lambda x: exang_display[x])
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope_display = ('up sloping','flat','down sloping')
        slope_options = list(range(len(slope_display)))
        slope = st.selectbox("Slope of the peak exercise ST segment",slope_options, format_func=lambda x: slope_display[x])
        
    with col3:
        ca_display = ('0','1','2','3','4')
        ca_options = list(range(len(ca_display)))
        ca = st.selectbox("Major vessels colored by flourosopy",ca_options, format_func=lambda x: ca_display[x])
        
    with col1:
        thal_display = ('normal','fixed defect','reversable defect')
        thal_options = list(range(len(thal_display)))
        thal = st.selectbox("thal",thal_options, format_func=lambda x: thal_display[x])
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
       
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
