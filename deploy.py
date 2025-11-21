import pickle
import pandas as pd

# Load model
try:
    with open('model_capstone_trial.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model berhasil dimuat!\n")
except:
    print("Model tidak ditemukan. Pastikan file 'model_capstone_trial.pkl' ada di folder yang sama.")
    exit()

print("=== Input Data Pengguna ===")

# Input fitur
plan_type = input("Plan Type (Basic/Standard/Premium): ")
device_brand = input("Device Brand (Samsung/Apple/Xiaomi/Oppo/Vivo/Huawei): ")

avg_data_usage_gb = float(input("Average Data Usage (GB): "))
pct_video_usage = float(input("Video Usage (%): "))
avg_call_duration = float(input("Average Call Duration (minutes): "))
sms_freq = int(input("SMS Frequency per Month: "))
monthly_spend = float(input("Monthly Spend ($): "))
topup_freq = int(input("Topup Frequency per Month: "))
travel_score = float(input("Travel Score: "))
complaint_count = int(input("Complaint Count: "))

# Bentuk dataframe
input_data = pd.DataFrame([{
    "plan_type": plan_type,
    "device_brand": device_brand,
    "avg_data_usage_gb": avg_data_usage_gb,
    "pct_video_usage": pct_video_usage,
    "avg_call_duration": avg_call_duration,
    "sms_freq": sms_freq,
    "monthly_spend": monthly_spend,
    "topup_freq": topup_freq,
    "travel_score": travel_score,
    "complaint_count": complaint_count
}])

# Prediksi
try:
    prediction = model.predict(input_data)
    print("\n=== HASIL REKOMENDASI OFFER ===")
    print("Target Offer yang disarankan:", prediction[0])

except Exception as e:
    print(f"Error saat prediksi: {e}")
