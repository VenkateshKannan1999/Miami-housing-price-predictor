import streamlit as st
import joblib
import numpy as np
import os
def main():
    st.title("Miami Housing Price Prediction")
    model_path = (os.path.join('miami_housing_price'),'model_joblib_gr')
    model = joblib.load('miami_housing_price')
    
    # Example of using a relative path
    model_path = os.path.join(os.path.dirname('miami_housing_price'), 'model_joblib_gr')
    model = joblib.load('miami_housing_price')
    
    st.title('Miami Housing Price Predictor')
    st.write('Enter the following details to predict the house price:')
    sqft_living = st.number_input('Square Footage', min_value=0)
    bedrooms = st.number_input('Number of Bedrooms', min_value=0)
    bathrooms = st.number_input('Number of Bathrooms', min_value=0)
    year_built = st.number_input('Year Built', min_value=1800, max_value=2023)
if st.button('Predict Price'):
    input_data = np.array([[sqft_living, bedrooms, bathrooms, year_built]])
    prediction = model.predict(input_data)
    st.success(f'The predicted house price is ${prediction[0]:,.2f}')
