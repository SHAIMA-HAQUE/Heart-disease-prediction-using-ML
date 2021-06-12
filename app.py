import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import pickle as pk

pickle_in = open("regression_output.pkl","rb")
model = pk.load(pickle_in)


def main():
    st.title("Heart disease prediction and remedies")
    html_temp="""
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align-center;">Heart disease prediction and remedies ML app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    age = st.text_input("Age"," ")
    sex = st.text_input("Sex"," ")
    cp = st.text_input("CP"," ")
    trestbps= st.text_input("Resting Blood Pressure"," ")
    chol = st.text_input("cholesterol"," ")
    fbs = st.text_input("Fasting Blood Sugar"," ")
    restecg = st.text_input("resting electrocardiographic results"," ")
    thalach = st.text_input("maximum heart rate achieved "," ")
    exang = st.text_input("exercise induced angina"," ")
    oldpeak = st.text_input("ST depression induced by exercise relative to rest"," ")
    slope = st.text_input("the slope of the peak exercise ST segment"," ")
    ca = st.text_input("number of major vessels colored by flourosopy"," ")
    thal = st.text_input("thalassemia"," ")
    result = ""

    if st.button("Predict"):
        result = prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    
    st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Shubham Patel")



def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

    predicted_output = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(predicted_output)
    return(predicted_output)


if __name__ == '__main__':
        main()

