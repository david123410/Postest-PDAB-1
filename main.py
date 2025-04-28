from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

# Inisialisasi FastAPI
app = FastAPI(title="Average Health Prediction API")

# Load model dan scaler
try:
    with open("model_rfr.pkl", "rb") as f:
        model = pickle.load(f)

    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    # Load feature names langsung dari model
    model_feature_names = list(model.feature_names_in_)

except Exception as e:
    raise RuntimeError(f"Failed to load model or scaler: {e}")

# Skema input
class Patient(BaseModel):
    Number_Of_Doctors_Visited: int
    Physical_Health: int
    Mental_Health: int
    Dental_Health: int
    Stress_Keeps_Patient_from_Sleeping: int
    Medication_Keeps_Patient_from_Sleeping: int
    Pain_Keeps_Patient_from_Sleeping: int
    Bathroom_Needs_Keeps_Patient_from_Sleeping: int
    Trouble_Sleeping: int
    Prescription_Sleep_Medication: int
    Gender: int
    Race: int

# Fungsi kategorisasi gender
def categorize_gender(gender: int) -> int:
    if gender == 2:
        return 1
    elif gender == 1:
        return 0
    else:
        raise ValueError(f"Invalid gender value: {gender}. Expected 1 (Male) or 2 (Female).")

# Preprocessing input
def preprocess_input(data: Patient):
    try:
        df = pd.DataFrame([{
            "Number of Doctors Visited": data.Number_Of_Doctors_Visited,
            "Stress Keeps Patient from Sleeping": data.Stress_Keeps_Patient_from_Sleeping,
            "Medication Keeps Patient from Sleeping": data.Medication_Keeps_Patient_from_Sleeping,
            "Pain Keeps Patient from Sleeping": data.Pain_Keeps_Patient_from_Sleeping,
            "Bathroom Needs Keeps Patient from Sleeping": data.Bathroom_Needs_Keeps_Patient_from_Sleeping,
            "Trouble Sleeping": data.Trouble_Sleeping,
            "Prescription Sleep Medication": data.Prescription_Sleep_Medication,
            "Gender": categorize_gender(data.Gender),
            "Race": data.Race
        }])

        # Urutkan sesuai fitur model
        df = df[model_feature_names]

        # Pastikan semua float
        df = df.astype(float)

        # Scaling
        df_scaled = scaler.transform(df)
        return df_scaled
    except Exception as e:
        raise ValueError(f"Error during preprocessing input: {e}")

# Endpoint prediksi + feature importance
@app.post("/predict")
def predict_and_feature_importance(data: Patient):
    try:
        # Hitung manual average health (untuk perbandingan)
        average_health = (data.Physical_Health + data.Mental_Health + data.Dental_Health) / 3

        # Preprocessing
        processed = preprocess_input(data)
        model_prediction = model.predict(processed)[0]

        # Feature Importance
        importances = model.feature_importances_
        feature_importance = dict(zip(model_feature_names, importances))
        feature_importance_sorted = dict(sorted(feature_importance.items(), key=lambda item: item[1], reverse=True))

        # Return hasil
        return {
            "manual_average_health": float(average_health),
            "model_prediction": float(model_prediction),
            "feature_importance": feature_importance_sorted
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
