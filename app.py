
import streamlit as st
import pickle

# Load model dan encoder
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

st.title("Prediksi Hasil Berdasarkan Data Personal")

# Input form
usia = st.selectbox("Usia", encoders["Usia"].classes_)
jenis_kelamin = st.selectbox("Jenis Kelamin", encoders["Jenis_Kelamin"].classes_)
merokok = st.selectbox("Merokok", encoders["Merokok"].classes_)
bekerja = st.selectbox("Bekerja", encoders["Bekerja"].classes_)
rumah_tangga = st.selectbox("Rumah Tangga", encoders["Rumah_Tangga"].classes_)
begadang = st.selectbox("Aktivitas Begadang", encoders["Aktivitas_Begadang"].classes_)
olahraga = st.selectbox("Aktivitas Olahraga", encoders["Aktivitas_Olahraga"].classes_)
asuransi = st.selectbox("Asuransi", encoders["Asuransi"].classes_)
penyakit = st.selectbox("Penyakit Bawaan", encoders["Penyakit_Bawaan"].classes_)

# Encode input
input_data = [
    encoders["Usia"].transform([usia])[0],
    encoders["Jenis_Kelamin"].transform([jenis_kelamin])[0],
    encoders["Merokok"].transform([merokok])[0],
    encoders["Bekerja"].transform([bekerja])[0],
    encoders["Rumah_Tangga"].transform([rumah_tangga])[0],
    encoders["Aktivitas_Begadang"].transform([begadang])[0],
    encoders["Aktivitas_Olahraga"].transform([olahraga])[0],
    encoders["Asuransi"].transform([asuransi])[0],
    encoders["Penyakit_Bawaan"].transform([penyakit])[0]
]

# Prediksi
if st.button("Prediksi"):
    pred = model.predict([input_data])[0]
    hasil = encoders["Hasil"].inverse_transform([pred])[0]
    st.success(f"Hasil Prediksi: **{hasil.upper()}**")
