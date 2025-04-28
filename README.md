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
  "Name": "John Doe",
  "Pclass": 2,
  "Sex": "male",
  "Age": 30,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 13.5,
  "Embarked": "S"
}
```

## ✅ Contoh Output

```json
{
  "name": "John Doe",
  "prediction": 1,


  "result": "Survived"
}
```


> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
