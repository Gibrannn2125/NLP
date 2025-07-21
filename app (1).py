{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85187332-daa3-4d18-a351-a1ee7f8706dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load model dan label encoders\n",
    "model = joblib.load(\"model.pkl\")\n",
    "label_encoders = joblib.load(\"label_encoders.pkl\")\n",
    "\n",
    "st.title(\"Klasifikasi Studi Kasus\")\n",
    "\n",
    "# Form input\n",
    "with st.form(\"user_input\"):\n",
    "    usia = st.selectbox(\"Usia\", [\"Tua\", \"Muda\"])\n",
    "    jenis_kelamin = st.selectbox(\"Jenis Kelamin\", [\"Pria\", \"Wanita\"])\n",
    "    merokok = st.selectbox(\"Merokok\", [\"Aktif\", \"Pasif\", \"Ya\", \"Tidak\"])\n",
    "    bekerja = st.selectbox(\"Bekerja\", [\"Ya\", \"Tidak\"])\n",
    "    rumah_tangga = st.selectbox(\"Rumah Tangga\", [\"Ya\", \"Tidak\"])\n",
    "    begadang = st.selectbox(\"Aktivitas Begadang\", [\"Ya\", \"Tidak\"])\n",
    "    olahraga = st.selectbox(\"Aktivitas Olahraga\", [\"Sering\", \"Jarang\"])\n",
    "    asuransi = st.selectbox(\"Asuransi\", [\"Ada\", \"Tidak\"])\n",
    "    penyakit = st.selectbox(\"Penyakit Bawaan\", [\"Ada\", \"Tidak\"])\n",
    "    \n",
    "    submitted = st.form_submit_button(\"Prediksi\")\n",
    "\n",
    "if submitted:\n",
    "    input_data = {\n",
    "        \"Usia\": usia,\n",
    "        \"Jenis_Kelamin\": jenis_kelamin,\n",
    "        \"Merokok\": merokok,\n",
    "        \"Bekerja\": bekerja,\n",
    "        \"Rumah_Tangga\": rumah_tangga,\n",
    "        \"Aktivitas_Begadang\": begadang,\n",
    "        \"Aktivitas_Olahraga\": olahraga,\n",
    "        \"Asuransi\": asuransi,\n",
    "        \"Penyakit_Bawaan\": penyakit\n",
    "    }\n",
    "    \n",
    "    # Encode input\n",
    "    encoded_input = [label_encoders[col].transform([val])[0] for col, val in input_data.items()]\n",
    "    \n",
    "    # Prediksi\n",
    "    prediction = model.predict([encoded_input])[0]\n",
    "    hasil = label_encoders[\"Hasil\"].inverse_transform([prediction])[0]\n",
    "    \n",
    "    st.success(f\"Prediksi Hasil: **{hasil}**\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
