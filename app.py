import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Sleep Quality Predictor")

age = st.number_input("Age", 1, 100)
sleep_duration = st.number_input("Sleep Duration (Hours)", 1.0, 12.0)
stress = st.number_input("Stress Level (1-10)", 1, 10)

if st.button("Predict"):
    result = model.predict([[age, sleep_duration, stress]])

    if result[0] == "Good":
        st.success("Good Sleep Expected")
    else:
        st.error("Poor Sleep Expected")
