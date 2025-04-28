# Analisis Hubungan Antara Gaya Hidup Sehat dan Kualitas Hidup Lansia
Sebuah mini-proyek berbasis FastAPI yang dapat memprediksi faktor yang paling berpengaruh ke kualitas hidup berdasarkan kondisi pengisinya.

## Struktur File
```
├── main.py             # Endpoint API utama
├── model_rfr.pkl       # File model Machine Learning yang telah dilatih
├── scaler.pkl          # File scaler untuk normalisasi fitur input
├── req.txt             # Daftar dependency yang dibutuhkan
```

## Fitur API
- Prediksi Pengaruh Faktor Eksternal Ke Kualitas Hidup
- Hasil prediksi

## Cara Menjalankan
### 1. Clone Repositori
```bash
git clone [https://github.com/david123410/Postest-PDAB-1.git]
cd Postest-PDAB-1
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r req.txt
```

### 4. Jalankan API

```bash
uvicorn app:app --reload
```

### 5. Akses FastAPI

Buka browser ke:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "Number_Of_Doctors_Visited": 2,
  "Physical_Health": 3,
  "Mental_Health": 1,
  "Dental_Health": 2,
  "Stress_Keeps_Patient_from_Sleeping": 1,
  "Medication_Keeps_Patient_from_Sleeping": 0,
  "Pain_Keeps_Patient_from_Sleeping": 1,
  "Bathroom_Needs_Keeps_Patient_from_Sleeping": 1,
  "Trouble_Sleeping": 1,
  "Prescription_Sleep_Medication": 0,
  "Gender": 1,
  "Race": 1
}
```

## ✅ Contoh Output

```json
{
  "manual_average_health": 2,
  "model_prediction": 3.1178811341029746,
  "feature_importance": {
    "Pain Keeps Patient from Sleeping": 0.20654737750262592,
    "Trouble Sleeping": 0.1681746248182978,
    "Race": 0.12169952228654958,
    "Number of Doctors Visited": 0.11353810110469066,
    "Gender": 0.11331708162616767,
    "Prescription Sleep Medication": 0.0893960279195913,
    "Stress Keeps Patient from Sleeping": 0.0815791924581104,
    "Medication Keeps Patient from Sleeping": 0.06039109856284044,
    "Bathroom Needs Keeps Patient from Sleeping": 0.045356973721126244
  }
}
```


> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
