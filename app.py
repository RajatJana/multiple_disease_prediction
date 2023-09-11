
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 01:32:30 2023

@author: RAJAT JANA
"""
import sklearn
import pickle
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Home','Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['house','activity','heart'],
                          default_index=0)
    
if (selected == 'Home'):
    
   img0 = Image.open('main.jpg')
   img0 = img0.resize((400,100))
   st.image(img0,use_column_width=True)
   
   st.title('Welome to Multiple Disease Prediction System using Machine Learning and Streamlit')    
   
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    img1 = Image.open('d_logo.png')
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
    
    img2 = Image.open('h_logo.png')
    img2 = img2.resize((156,145))
    st.image(img2,use_column_width=False)
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
       sex = st.text_input('Sex(0:Female 1:Male)')
        
    with col3:
        cp = st.text_input('Chest Pain types(0:'typical angina',1:'atypical angina',2:'non-anginal pain',3:'asymptomatic')')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl(0:False 1:True)')
        
    with col1:
      restecg = st.text_input('Resting Electrocardiographic results(0,1,2)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
       exang = st.text_input('Exercise Induced Angina(0:No 1:Yes)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment(0:'up sloping',1:'flat',2:'down sloping')')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
       
            f=[[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]]
            print(f)
        heart_prediction = heart_disease_model.predict(f)       
        lc = [str(i) for i in heart_prediction]
        ans = int("".join(lc))
        
        if (ans == 1):
            st.error(
          heart_diagnosis = 'The person is having heart disease'
            )
        else:
            st.success(
          heart_diagnosis = 'The person does not have any heart disease'
            )
        
    
