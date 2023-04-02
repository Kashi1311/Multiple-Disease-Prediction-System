import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Arpit/Downloads/Multiple disease prediction system/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Arpit/Downloads/Multiple disease prediction system/saved models/heart_disease_model.sav', 'rb'))
parkisons_model = pickle.load(open('C:/Users/Arpit/Downloads/Multiple disease prediction system/saved models/parkisons_model.sav', 'rb'))
chronic_kidney_disease_model = pickle.load(open('C:/Users/Arpit/Downloads/Multiple disease prediction system/saved models/chronic_kidney_disease_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Detection System',
                           
                           ['Diabetes Prediction',
                            'Heart-Disease Prediction',
                            'Parkisons Prediction',
                            "Chronic Kidney Disease Prediction"],
                            default_index = 0)
    
if(selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediciton using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('No. of Pregnancies')
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin Value")
    with col3:
        BMI_value = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input("Age")

    #code for prediction
    diabetes_result = ''
    #creating a button
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI_value,DiabetesPedigreeFunction,Age]])

        if(diabetes_prediction[0]==1):
           diabetes_result = "The Person is Diabetic"
        else:
           diabetes_result = "The Person is not Diabetic"

        st.success(diabetes_result)


if(selected == 'Heart-Disease Prediction'):
    st.title('Heart-Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("CP")
    with col1:
        trestbps = st.text_input("trestbps")
    with col2:
        chol = st.text_input("chol")
    with col3:
        fbs = st.text_input("fbs")
    with col1:
        restecg = st.text_input("restecg")
    with col2:
        thalach = st.text_input("thalach")
    with col3:
        exang = st.text_input("exang")
    with col1:
        oldpeak = st.text_input("oldpeak")
    with col2:
        slope = st.text_input("slope")
    with col3:
        ca = st.text_input("ca")
    with col1:
        thal = st.text_input("thal")

    #code for prediction
    heart_disease_result = ''

    #creating a button
    if st.button("Heart Disease Test Result"):
        heart_disease_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if(heart_disease_prediction[0]==1):
           heart_disease_result = "The Person is effected"
        else:
           heart_disease_result = "The Person is not effected"

        st.success(heart_disease_result)

if(selected == 'Parkisons Prediction'):
    st.title('Parkisons Prediction using ML')
    col1 ,col2, col3 = st.columns(3)
    with col1:
        FoHz = st.text_input("MDVP:Fo(Hz)")
    with col2:
        FhiHz = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        FloHz = st.text_input("MDVP:Flo(Hz)")
    with col1:
        Jitter_percentage = st.text_input("MDVP:Jitter(%)")
    with col2:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        RAP = st.text_input("MDVP:RAP")
    with col1:
        PPQ = st.text_input("MDVP:PPQ")
    with col2:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col3:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col1:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col3:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    with col1:
        APQ = st.text_input("MDVP:APQ")
    with col2:
        NHR = st.text_input("NHR")
    with col3:
        HNR = st.text_input("HNR")
    with col1:
        RPDE = st.text_input("RPDE")
    with col2:
        DFA = st.text_input("DFA")
    with col3:
        spread1 = st.text_input("spread1")
    with col1:
        spread2 = st.text_input("spread2")
    with col2:
        D2 = st.text_input("D2")
    with col3:
        PPE = st.text_input("PPE")

    #code for prediction
    parkinson_disease_result = ''

    #creating a button
    if st.button("Parkinsons Disease Test Result"):
        parkinson_disease_prediction = parkisons_model.predict([[FoHz,FhiHz,FloHz,Jitter_percentage,Jitter_Abs,RAP,PPQ,Jitter_DDP,Shimmer,Shimmer_dB,Shimmer_APQ3
                                                                 ,Shimmer_APQ5,APQ,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if(parkinson_disease_prediction[0]==1):
           parkinson_disease_result = "The Person is effected"
        else:
           parkinson_disease_result = "The Person is not effected"

        st.success(parkinson_disease_result)

if(selected == "Chronic Kidney Disease Prediction"):
    st.title("Chronic Kidney Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        bp = st.text_input("Blood Pressure level")
    with col3:
        sg = st.text_input("sg")
    with col1:
        al = st.text_input("al")
    with col2:
        su = st.text_input("au")
    with col3:
        bgr = st.text_input("bgr")
    with col1:
        bu = st.text_input("bu")
    with col2:
        sc = st.text_input("sc")
    with col3:
        sod = st.text_input("sod")
    with col1:
        pot = st.text_input("pot")
    with col2:
        hemo = st.text_input("hemo")
    with col3:
        pcv = st.text_input("pvc")
    with col1:
        wc = st.text_input("wc")
    with col2:
        rc = st.text_input("rc")

    #code for prediction
    chronic_kidney_disease_result = ''

    #creating a button
    if st.button("Chronic kidney Disease Test Result"):
        chronic_kidney_disease_prediction = chronic_kidney_disease_model.predict([[age,bp,sg,al,su,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc]])

        if(chronic_kidney_disease_prediction[0]==1):
           chronic_kideny_disease_result = "The Person is effected"
        else:
           chronic_kideny_disease_result = "The Person is not effected"

        st.success(chronic_kidney_disease_result)












