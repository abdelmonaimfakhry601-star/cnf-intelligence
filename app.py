import streamlit as st

st.set_page_config(
    page_title="CNF-Intelligence Research Platform",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 منصة CNF-Intelligence لإدارة وتحليل المزارع سالبة الكربون")
st.write("مرحباً بك! التطبيق يعمل الآن بنجاح وسيتم إضافة باقي الوحدات العلمية تباعاً.")

# تجربة حقل بسيط
area = st.number_input("مساحة المزرعة (هكتار):", value=10.0)
st.success(f"المساحة المحددة هي: {area} هكتار")
