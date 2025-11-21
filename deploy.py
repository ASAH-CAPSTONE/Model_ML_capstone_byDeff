import streamlit as st
import pickle
import pandas as pd

st.title("Model Trial - Rekomendasi Target Offer")

# Load model
try:
    with open('model_capstone_trial.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("Model berhasil dimuat!")
except:
    st.error("Model tidak ditemukan. Pastikan file 'model_capstone_trial.pkl' ada di folder yang sama.")
    st.stop()

st.subheader("Input Data Pengguna")

plan_type = st.selectbox("Plan Type", ["Basic", "Standard", "Premium"])
device_brand = st.selectbox("Device Brand", ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo", "Huawei"])

avg_data_usage_gb = st.number_input("Average Data Usage (GB)", min_value=0.0, step=0.1)
pct_video_usage = st.number_input("Video Usage (%)", min_value=0.0, max_value=100.0, step=1.0)
avg_call_duration = st.number_input("Average Call Duration (minutes)", min_value=0.0, step=1.0)
sms_freq = st.number_input("SMS Frequency per Month", min_value=0, step=1)
monthly_spend = st.number_input("Monthly Spend ($)", min_value=0.0, step=0.1)
topup_freq = st.number_input("Topup Frequency per Month", min_value=0, step=1)
travel_score = st.number_input("Travel Score", min_value=0.0, step=0.1)
complaint_count = st.number_input("Complaint Count", min_value=0, step=1)

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

if st.button("Prediksi Target Offer"):
    try:
        prediction = model.predict(input_data)
        st.subheader("Hasil Rekomendasi Offer")
        st.success(f"Target Offer yang disarankan: {prediction[0]}")
    except Exception as e:
        st.error(f"Error saat prediksi: {e}")
