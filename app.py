import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

st.title("Web App for Medical Diagnosis ")
st.subheader("Does the patient have diabetes?")

#Step1: Load the model
model=open('pipeline.pickle', 'rb')
clf=pickle.load(model)
model.close()

# Step2: Get the data from the frontend user 
pregs=st.number_input('Pregnancies', 0, 20,0)
plas=st.slider('Glucose', 40, 200, 40)
bp=st.slider('BloodPressure', 20, 140, 20)
skin=st.slider('SkinThickness', 7, 99, 7)
insulin=st.slider('Insulin', 14, 846, 14)
bmi=st.slider('BMI', 18, 70, 18)
dpf=st.slider('DiabetesPedigreeFunction', 0.05, 2.50, 0.05)
age=st.slider('Age', 21, 90, 21)

# Step3: Convert the from end user input to model input data
data={
    'Pregnancies':pregs,
    'Glucose':plas,
    'BloodPressure':bp,
    'SkinThickness':skin,
    'Insulin':insulin,
    'BMI':bmi,
    'DiabetesPedigreeFunction':dpf,
    'Age':age }
input_data=pd.DataFrame([data])

# Step4: get the predictions and print the diagnosis
prediction=clf.predict(input_data)[0]
if st.button('Predict'):
    if prediction==0:
        st.subheader('Woman is healthy')
    else:
        st.subheader('Has Diabetes')
        
        
