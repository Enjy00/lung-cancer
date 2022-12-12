import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('cancer-patient.sav', 'rb'))

st.title('Prediksi Kanker Paru-Paru')

col1, col2, col3 = st.columns(3)

with col1:
    Index = st.number_input('Index')

with col2:
    Age = st.number_input('Umur')

with col3:
    Gender = st.number_input('Jenis Kelamin')

with col1:
    Air_Pollution = st.number_input('Polusi Udara')

with col2:
    Alcohol_use = st.number_input('Pengguna Alkohol')

with col3:
    Dust_Allergy = st.number_input('Alergi Debu')

with col1:
    OccuPational_Hazards = st.number_input('bahaya pekerjaan')

with col2:
    Genetic_Risk = st.number_input('Risiko Genetik')

with col3:
    chronic_Lung_Disease = st.number_input('Penyakit Paru-paru Kronis')

with col1:
    Balanced_Diet = st.number_input('Diet Seimbang')

with col2:
    Obesity = st.number_input('Kegemukan')

with col3:
    Smoking = st.number_input('Merokok')

with col1:
    Passive_Smoker = st.number_input('Perokok Pasif')

with col2:
    Chest_Pain = st.number_input('Sakit Dada')

with col3:
    Coughing_of_Blood = st.number_input('Batuk Darah')

with col1:
    Fatigue = st.number_input('Kelelahan')

with col2:
    Weight_Loss = st.number_input('Penurunan Berat Badan')

with col3:
    Shortness_of_Breath = st.number_input('Sesak Napas')

with col1:
    Wheezing = st.number_input('Wheezing')

with col2:
    Swallowing_Difficulty = st.number_input('Kesulitan Menelan')

with col3:
    Clubbing_of_Finger_Nails = st.number_input('Clubbing of Finger Nails')

with col1:
    Frequent_Cold = st.number_input('Sering Dingin')

with col2:
    Dry_Cough = st.number_input('Batuk Kering')

with col3:
    Wet_Cough = st.number_input('Batuk Basah')

cancer_diagnosis = ''

if st.button('Prediksi Kanker Paru-Paru'):
    cancer_prediction = model.predict([[Index,Age,Gender,Air_Pollution,Alcohol_use,Dust_Allergy,OccuPational_Hazards,Genetic_Risk,chronic_Lung_Disease,Balanced_Diet,Obesity,Smoking,Passive_Smoker,Chest_Pain,Coughing_of_Blood,Fatigue,Weight_Loss,Shortness_of_Breath,Wheezing,Swallowing_Difficulty,Clubbing_of_Finger_Nails,Frequent_Cold,Dry_Cough,Wet_Cough]])

    if(cancer_prediction[0]==0):
        cancer_diagnosis = 'Tingkat Resiko Rendah'
    elif(cancer_prediction[0]==1):
        cancer_diagnosis = 'Tingkat Resiko Sedang'
    else:
        cancer_diagnosis = 'Tingkat Resiko Tinggi'

st.success(cancer_diagnosis)