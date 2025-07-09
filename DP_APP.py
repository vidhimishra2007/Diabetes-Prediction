#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 02:43:26 2025

@author: vidhimishra
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('/Users/vidhimishra/Desktop/DiabetesPrediction/DP_model.pkl','rb'))


#creating a function for Prediction

def diabetes_prediction(sample_data):

    sample_data = np.asarray(sample_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(sample_data)

    if prediction == 0:
       return'The person is not diabetic.'
    else:
       return'The person is diabetic.'
    print("Prediction:", prediction) # Output: 0 (No Diabetes) or 1 (Diabetes)
    
    
    
def main():
    
    
    #giving a title
    st.title('Diabetes Prediction System')
    
    #getting the input data from the user
    
    Pregnancies = st.text_input ( 'Number of Pregnancies')
    Glucose=st.text_input ( 'Glucose Level')
    BloodPressure=st.text_input ( 'Blood Pressure Value')
    SkinThickness=st.text_input ( 'Skin Thickness Value')
    Insulin=st.text_input ( 'Insulin Level')
    BMI=st.text_input ( 'BMI Value')
    DiabetesPedigreeFunction=st.text_input ( 'Diabetes Pedigree Function Value')
    Age=st.text_input ( 'Age of the Person ')
    
    
    # code for Prediction
    diagnosis = ''
    
    
    # creating a button for Prediction
    if st.button( 'Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
    
if __name__=='__main__':
    main()