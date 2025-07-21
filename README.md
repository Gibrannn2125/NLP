# Web Aplikasi Klasifikasi Hasil Berdasarkan Data Pribadi

Proyek ini adalah aplikasi web berbasis **Streamlit** untuk memprediksi nilai **Hasil (Ya/Tidak)** berdasarkan fitur-fitur personal seperti usia, jenis kelamin, merokok, aktivitas olahraga, dan lainnya. Model klasifikasi dilatih menggunakan algoritma **Random Forest** dari dataset berisi 30.000 entri.

---

## 📌 Fitur Aplikasi

- Input form interaktif (usia, merokok, olahraga, dll.)
- Prediksi hasil menggunakan model Machine Learning
- Web ringan dan dapat dijalankan secara lokal maupun online (Streamlit Cloud)

---

## 🧠 Dataset

Dataset digunakan: `predic_tabel.csv`  
Jumlah data: 30.000  
Fitur yang digunakan:
- Usia
- Jenis_Kelamin
- Merokok
- Bekerja
- Rumah_Tangga
- Aktivitas_Begadang
- Aktivitas_Olahraga
- Asuransi
- Penyakit_Bawaan  
Target label: **Hasil** (`Ya` atau `Tidak`)

---

## 🚀 Cara Menjalankan (Lokal)

1. **Clone repo ini**:
   ```bash
   git clone https://github.com/username/klasifikasi-hasil.git
   cd klasifikasi-hasil
