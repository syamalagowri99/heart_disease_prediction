import sklearn
import streamlit as st
import pickle

loaded_model = pickle.load(open('heartdise.sav', 'rb'))

st.title("Heart Disease Prediction App")
st.markdown("By Syamala")

col1, col2, col3 = st.columns(3)

with col1:
	age = st.number_input('Age')

with col2:
      sex = st.number_input('Sex')

with col3:
	cp = st.number_input('Chest Pain types')

with col1:
	trestbps = st.number_input('Resting Blood Pressure')

with col2:
	chol = st.number_input('Serum Cholestoral in mg/dl')

with col3:
	fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
	restecg = st.number_input('Resting Electrocardiographic results')

with col2:
	thalach = st.number_input('Maximum Heart Rate achieved')

with col3:
	exang = st.number_input('Exercise Induced Angina')

with col1:
	oldpeak = st.number_input('ST depression induced by exercise')

with col2:
	slope = st.number_input('Slope of the peak exercise ST segment')

with col3:
      ca = st.number_input('Major vessels colored by flourosopy')

with col1:
	thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

# code for Prediction
heart_diagnosis = ''
heart_prediction=None
# creating a button for Prediction Heart Disease Test Result

if st.button('Heart Disease Test Result'):
	heart_prediction= loaded_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
if (heart_prediction == 1):
	heart_diagnosis = 'The person is having heart disease'
else:
	heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)
