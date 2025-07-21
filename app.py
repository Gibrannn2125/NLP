import streamlit as st
import joblib
import numpy as np

# Load model dan label encoders
model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

st.title("Klasifikasi Studi Kasus")

# Form input
with st.form("user_input"):
    usia = st.selectbox("Usia", ["Tua", "Muda"])
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
    merokok = st.selectbox("Merokok", ["Aktif", "Pasif", "Ya", "Tidak"])
    bekerja = st.selectbox("Bekerja", ["Ya", "Tidak"])
    rumah_tangga = st.selectbox("Rumah Tangga", ["Ya", "Tidak"])
    begadang = st.selectbox("Aktivitas Begadang", ["Ya", "Tidak"])
    olahraga = st.selectbox("Aktivitas Olahraga", ["Sering", "Jarang"])
    asuransi = st.selectbox("Asuransi", ["Ada", "Tidak"])
    penyakit = st.selectbox("Penyakit Bawaan", ["Ada", "Tidak"])

    submitted = st.form_submit_button("Prediksi")

if submitted:
    input_data = {
        "Usia": usia,
        "Jenis_Kelamin": jenis_kelamin,
        "Merokok": merokok,
        "Bekerja": bekerja,
        "Rumah_Tangga": rumah_tangga,
        "Aktivitas_Begadang": begadang,
        "Aktivitas_Olahraga": olahraga,
        "Asuransi": asuransi,
        "Penyakit_Bawaan": penyakit
    }

    # Encode input
    encoded_input = [label_encoders[col].transform([val])[0] for col, val in input_data.items()]

    # Prediksi
    prediction = model.predict([encoded_input])[0]
    hasil = label_encoders["Hasil"].inverse_transform([prediction])[0]

    st.success(f"Prediksi Hasil: **{hasil}**")