import streamlit as st

st.set_page_config(page_title="Cybersecurity Shield & Threat Monitor", page_icon="🛡️", layout="wide")

st.title("🛡️ وحدة الأمن السيبراني وحماية منصة CNF-Intelligence")
st.write("مراقبة التهديدات السيبرانية، محاولات الاختراق، وفحص حالة جدار الحماية (Firewall) والسحابة الرقمية.")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 حالة النظام الأمني الحالية")
    threat_level = st.selectbox("محاكاة حالة الأمان في النظام:", ["آمن تماماً (Secure)", "محاولة اختراق مشبوهة (Suspicious Activity)", "هجوم سيبراني نشط (Active Cyber Attack)"])
    
    if "آمن تماماً" in threat_level:
        status_color = "green"
        light_html = '<div style="width: 70px; height: 70px; background-color: #2ecc71; border-radius: 50%; box-shadow: 0 0 25px #2ecc71; margin: 20px auto;"></div>'
    elif "مشبوهة" in threat_level:
        status_color = "orange"
        light_html = '<div style="width: 70px; height: 70px; background-color: #f39c12; border-radius: 50%; box-shadow: 0 0 25px #f39c12; margin: 20px auto;"></div>'
    else:
        status_color = "red"
        light_html = '<div style="width: 70px; height: 70px; background-color: #e74c3c; border-radius: 50%; box-shadow: 0 0 35px #e74c3c; margin: 20px auto;"></div>'

with col2:
    st.subheader("🔴 مؤشر الإنذار السيبراني")
    st.markdown(light_html, unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: {status_color}; font-weight: bold; font-size: 18px;'>{threat_level}</p>", unsafe_allow_html=True)
