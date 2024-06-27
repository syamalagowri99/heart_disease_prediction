import sklearn
import streamlit as st
import pickle
import os

# Load the model
def load_model(file_path):
    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_file = '/content/heartdise.sav'
loaded_model = load_model(model_file)

# Streamlit app
st.title("Heart Disease Prediction App")
st.markdown("By Syamala")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=0, max_value=120, step=1)

with col2:
    sex = st.selectbox('Sex', options=[0, 1], help='0: Female, 1: Male')

with col3:
    cp = st.number_input('Chest Pain types', min_value=0, max_value=3, step=1)

with col1:
    trestbps = st.number_input('Resting Blood Pressure', min_value=0)

with col2:
    chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0)

with col3:
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])

with col1:
    restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1)

with col2:
    thalach = st.number_input('Maximum Heart Rate achieved', min_value=0)

with col3:
    exang = st.selectbox('Exercise Induced Angina', options=[0, 1])

with col1:
    oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, format="%.1f")

with col2:
    slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)

with col3:
    ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=4, step=1)

with col1:
    thal = st.number_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', min_value=0, max_value=2, step=1)

heart_diagnosis = ''
if st.button('Heart Disease Test Result'):
    if loaded_model:
        features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        try:
            heart_prediction = loaded_model.predict(features)[0]
            if heart_prediction == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Model not loaded.")

st.success(heart_diagnosis)
