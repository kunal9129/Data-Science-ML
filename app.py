# streamlit run app.py
import streamlit as st 
import pickle
import numpy as np 

with open("model.pkl","rb") as p:
    model = pickle.load(p)

st.title("Sales Prediction Application ")

st.write("Please enter your Advertisement Invest in Each to Predict Sales.")

TV = st.number_input("Advertising Investment In TV ",min_value=0.0,format="%.2f")
RADIO = st.number_input("Advertising Radio In Radio ",min_value=0.0,format="%.2f")
NEWSPAPER = st.number_input("Advertising Newspaper In TV ",min_value=0.0,format="%.2f")

if st.button("Predict Sales"):
    features = np.array([[TV,RADIO,NEWSPAPER]])
    predictions = model.predict(features)[0]
    st.success(f"Predicted Sales : {predictions:.2f}")