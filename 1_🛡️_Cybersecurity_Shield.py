import streamlit as st
import time

st.set_page_config(page_title="Cybersecurity Shield & Threat Monitor", page_icon="🛡️", layout="wide")

st.title("🛡️ وحدة الأمن السيبراني وحماية منصة CNF-Intelligence")
st.write("مراقبة التهديدات السيبرانية، محاولات الاختراق، وفحص حالة جدار الحماية (Firewall) والسحابة الرقمية.")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 حالة النظام الأمني الحالية")
    
    # محاكاة فحص الأمان
    threat_level = st.selectbox("محاكاة حالة الأمان في النظام:", ["آمن تماماً (Secure)", "محاولة اختراق مشبوهة (Suspicious Activity)", "هجوم سيبراني نشط (Active Cyber Attack)"])
    
    if "آمن تماماً" in threat_level:
        status_color = "green"
        status_text = "النظام مؤمن بالكامل - لا توجد أي تهديدات مرصودة."
        light_html = '<div style="width: 60px; height: 60px; background-color: #2ecc71; border-radius: 50%; box-shadow: 0 0 20px #2ecc71; margin: 10px auto;"></div>'
    elif "مشبوهة" in threat_level:
        status_color = "orange"
        status_text = "تحذير: تم رصد محاولات فحص ثغرات (Port Scanning) من مصدر مجهول."
        light_html = '<div style="width: 60px; height: 60px; background-color: #f39c12; border-radius: 50%; box-shadow: 0 0 20px #f39c12; margin: 10px auto; animation: blink 1s infinite;"></div>'
    else:
        status_color = "red"
        status_text = "⚠️ تنبيه خطر أمني! هجوم DDoS أو محاولة حقن بيانات غير مصرح بها قيد الحظر الفوري."
        light_html = '<div style="width: 60px; height: 60px; background-color: #e74c3c; border-radius: 50%; box-shadow: 0 0 30px #e74c3c; margin: 10px auto; animation: blink 0.5s infinite;"></div>'

with col2:
    st.subheader("🔴 مؤشر الإنذار السيبراني")
    st.markdown("<p style='text-align: center; font-weight: bold;'>حالة اللمبة التنبيهية:</p>", unsafe_allow_html=True)
    st.markdown(light_html, unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: {status_color}; font-weight: bold;'>{threat_level}</p>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📜 سجل الأحداث الأمنية (Security Audit Logs)")
log_data = {
    "التوقيت": ["10:45 AM", "11:12 AM", "11:20 AM", "11:22 AM"],
    "نوع الحدث": ["تسجيل دخول ناجح", "محاولة اتصال بـ API", "فحص جدار الحماية", "تأمين الجلسة السحابية"],
    "المصدر": ["Admin IP (Local)", "Cloud Streamlit Node", "Firewall Shield", "SSL Certificate"],
    "الحالة": ["مسموح", "مسموح", "تم التصدي والفلترة", "نشط وآمن"]
}
st.table(log_data)
