import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import pickle as pk
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

pickle_in = open("regression_output.pkl","rb")
model = pk.load(pickle_in)


def main():
    #st.title("Heart disease prediction and remedies")
    html_temp="""
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align-center;">Heart disease prediction and remedies ML app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    age = st.number_input("Age",0,None)
    sex = st.number_input("Sex",0,1)
    cp = st.number_input("Chest Pain Type",1,4)
    trestbps= st.number_input("Resting Blood Pressure",0,None)
    chol = st.number_input("Cholesterol",0,None)
    fbs = st.number_input("Fasting Blood Sugar",0,1)
    restecg = st.number_input("Resting Electrocardiographic Results",0,2)
    thalach = st.number_input("Maximum Heart Rate Achieved ",0,None)
    exang = st.number_input("Exercise Induced Angina",0,1)
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest",0.0,None)
    slope = st.number_input("The Slope of the Peak Exercise ST Segment",0,3)
    ca = st.number_input("Number of Major Vessels colored by Flourosopy",0,3)
    thal = st.number_input("Thalassemia",1,3)
    result = ""
    
    
    #Documentation for webapp usage
    st.sidebar.header("Some Important terms: ")
    st.sidebar.write("""
     Values to be Entered:
    - **Sex**  
        - 0 for Female 
        - 1 for male
    - **[Chest Pain Type](https://www.heart.org/en/health-topics/heart-attack/angina-chest-pain)**
       - 1 for typical angina\n
       - 2 for atypical angina\n
       - 3 for non-anginal pain\n
       - 4 for asymptomatic\n  
    - **[Resting Blood Pressure](https://www.nhs.uk/common-health-questions/lifestyle/what-is-blood-pressure/)**
        - Enter Systolic Value
    - **[Cholesterol](https://www.healthline.com/health/high-cholesterol/levels-by-age)**
        - Enter serum cholestoral in mg/dl
    - **[Fasting Blood Sugar](https://www.mayoclinic.org/diseases-conditions/diabetes/diagnosis-treatment/drc-20371451)**
        - If fasting blood sugar > 120mg/dl
            - Enter 1 for True 
            - Enter 2 for False
    - **[Resting Electrocardiographic Results](https://www.healthline.com/health/electrocardiogram#:~:text=An%20electrocardiogram%20is%20a%20simple,electrical%20activity%20of%20your%20heart.)**
        - Enter 0 for normal 
        - Enter 1 for having ST-T wave abnormality (T wave inversions and/or ST
          elevation or depression of > 0.05 mV)
        - Enter 2 for showing probable or definite left ventricular hypertrophy
          by Estes' criteria
    - **[Maximum Heart rate achieved](https://www.hopkinsmedicine.org/health/wellness-and-prevention/understanding-your-target-heart-rate#:~:text=The%20maximum%20rate%20is%20based,or%2085%20beats%20per%20minute.)**
        - Measured per minute.
    - **[Exercise Induced Angina](https://www.mayoclinic.org/diseases-conditions/angina/symptoms-causes/syc-20369373#:~:text=Stable%20angina%20is%20usually%20triggered,arteries%20slow%20down%20blood%20flow.) **
        - Enter 1 for yes 
        - Enter 0 for no
    - **[ST Depression Induced by Exercise Relative to Rest](https://en.wikipedia.org/wiki/ST_depression#:~:text=In%20a%20cardiac%20stress%20test,to%20significantly%20indicate%20reversible%20ischaemia.)**
        - Value found from ECG report
    - **[The Slope of the Peak Exercise ST Segment](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1123032/#:~:text=Normal%20trace%20during%20exercise,exercise%20therefore%20slopes%20sharply%20upwards)**
        - Enter 1 for upsloping
        - Enter 2 for flat
        - Enter 3 downsloping
    - **Number of Major Vessels colored by Flourosopy**
        - Number of major vessels (0-3) colored by flourosopy
    - **Thalassemia**
        - Enter 1 for normal 
        - Enter 2 for fixed defect
        - Enter 3 for reversable defect
    
    """)
    # x_value = []
    # y_value = []
    
    #Prediction
    if st.button("Predict"):
        
        result = prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal) 
        if result == 1:
            st.error('Chance of Heart attack')
        else:
            st.success('Not having Heart attack')
        # x_value.append(result)
        # y_value.append(count())


    # Visualization  
    if st.button("Visualization"):
        # data = np.append(np.array(x_value), np.array(y_value))
        # st.line_chart(data)
    
    #Remedies
    if st.button("Remedies"):
        if cp == 1 or cp == 2 or cp == 3:
            st.write("""
            **Occurance of Chest Pain:**
         - If you smoke, stop smoking. Avoid exposure to secondhand smoke.
         - Angina is often brought on by exertion, it's helpful to pace yourself and take breaks.
         - Limit alcohol consumption to two drinks or fewer a day for men, and one drink a day or less for women.
         - Consult a doctor.
         """)
        if trestbps >=140:
            st.write("""
            **High Resting Blood Pressure:** 
        - Stop smoking.
        - Limit alcohol and sodium content in your food.
        - Keep your weight at check
        - Take breaks and avoid stress.
        """)
        if chol>=200:
            st.write("""
            **High Cholesterol level:**
        - Exercise regualrly for atleast 30 minutes everyday.
        - Monounsaturated fat, found in olive and canola oils is a healthier option.
         """)
        if fbs == 1 :
            st.write("""
            **High fasting blood pressure:**
        - If you take diabetes medicine, change the timing or type by consulting a doctor
        - Take lighter breakfast.
        - Choose food with low glycemic value
         """)
        if thalach> age-220:
            st.write("""
            **Relatively high maximum heart rate achieved:**
            - Reduce coffee, tea and soda consumption.
            - Try and reduce stress.
            - Exercise regularly.
             """)
        if exang == 1:
            st.write("""
            **Occurance of exercise induced angina** 
            - Consult a doctor.
            """)



def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

    predicted_output = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(predicted_output)
    return(predicted_output)


if __name__ == '__main__':
        main()

