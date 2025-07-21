{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d7251580-0213-4a1a-b06c-bf305a5930bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Model dan encoder berhasil disimpan.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import pickle\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv(\"predic_tabel.csv\")\n",
    "\n",
    "# Hapus kolom 'No'\n",
    "df = df.drop(columns=[\"No\"])\n",
    "\n",
    "# Label encoding semua kolom kategorikal KECUALI 'Hasil'\n",
    "le_dict = {}\n",
    "for col in df.columns:\n",
    "    if col != \"Hasil\" and df[col].dtype == 'object':\n",
    "        le = LabelEncoder()\n",
    "        df[col] = le.fit_transform(df[col])\n",
    "        le_dict[col] = le\n",
    "\n",
    "# Label encoding kolom target 'Hasil'\n",
    "le_hasil = LabelEncoder()\n",
    "df[\"Hasil\"] = le_hasil.fit_transform(df[\"Hasil\"])\n",
    "le_dict[\"Hasil\"] = le_hasil\n",
    "\n",
    "# Pisahkan fitur dan label\n",
    "X = df.drop(columns=[\"Hasil\"])\n",
    "y = df[\"Hasil\"]\n",
    "\n",
    "# Latih model\n",
    "model = RandomForestClassifier()\n",
    "model.fit(X, y)\n",
    "\n",
    "# Simpan model dan encoder\n",
    "with open(\"model.pkl\", \"wb\") as f:\n",
    "    pickle.dump(model, f)\n",
    "\n",
    "with open(\"encoders.pkl\", \"wb\") as f:\n",
    "    pickle.dump(le_dict, f)\n",
    "\n",
    "print(\"✅ Model dan encoder berhasil disimpan.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7f3522c-4b24-4e88-8687-5c6309513e71",
   "metadata": {},
   "outputs": [],
   "source": []
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
