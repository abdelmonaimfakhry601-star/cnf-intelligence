import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="CNF-Intelligence Research Platform",
    page_icon="🌱",
    layout="wide"
)

lang = st.sidebar.selectbox("🌐 اختر اللغة / Select Language", ["العربية", "English"])

if lang == "العربية":
    T = {
        "title": "🌱 منصة CNF-Intelligence لإدارة وتحليل المزارع سالبة الكربون",
        "subtitle": "إطار ذكاء اصطناعي متعدد الأهداف لتصميم المزرعة، تحسين الإنتاجية، وتقليل الانبعاثات",
        "tab_overview": "📊 نظرة عامة",
        "tab_profile": "🌾 ملف المزرعة",
        "tab_ghg": "💨 حساب الانبعاثات",
        "tab_ai": "🤖 تحليل الذكاء الاصطناعي (XAI)",
    }
else:
    T = {
        "title": "🌱 CNF-Intelligence Research Platform",
        "subtitle": "AI-Driven Multi-Objective Farm Design for Food Security & Carbon Removal",
        "tab_overview": "📊 Overview",
        "tab_profile": "🌾 Farm Profile",
        "tab_ghg": "💨 GHG Accounting",
        "tab_ai": "🤖 AI Optimization & XAI",
    }

st.title(T["title"])
st.caption(T["subtitle"])
st.markdown("---")

st.sidebar.header("⚙️ إعدادات المحاكاة الزراعية")
area = st.sidebar.number_input("مساحة المزرعة (هكتار)", value=50.0, min_value=0.1)
nitrogen = st.sidebar.number_input("السماد النيتروجيني (N kg/ha)", value=100.0)
diesel_l = st.sidebar.number_input("استهلاك الديزل (L/ha)", value=60.0)
electricity_kwh = st.sidebar.number_input("استهلاك الكهرباء (kWh/ha)", value=350.0)
soc_initial = st.sidebar.number_input("كربون التربة الأولي SOC (g/kg)", value=12.0)
soc_final = st.sidebar.number_input("كربون التربة النهائي SOC (g/kg)", value=15.5)

emissions_fuel = (diesel_l * 2.68 + electricity_kwh * 0.5) / 1000.0
emissions_fertilizer = (nitrogen * 5.8) / 1000.0
gross_ghg = emissions_fuel + emissions_fertilizer

soc_stock_init = soc_initial * 1.3 * 30 * 0.1
soc_stock_fin = soc_final * 1.3 * 30 * 0.1
carbon_removal_tCO2 = (soc_stock_fin - soc_stock_init) * (44.0 / 12.0) / 5.0
net_balance = gross_ghg - carbon_removal_tCO2

tab1, tab2, tab3, tab4 = st.tabs([T["tab_overview"], T["tab_profile"], T["tab_ghg"], T["tab_ai"]])

with tab1:
    st.subheader("📊 مؤشرات الأداء الرئيسية للمزرعة (KPIs)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("مساحة المزرعة", f"{area} ha")
    c2.metric("الانبعاثات الإجمالية", f"{gross_ghg:.2f} t CO2e/ha")
    c3.metric("احتجاز الكربون", f"{carbon_removal_tCO2:.2f} t CO2e/ha")
    c4.metric("صافي الرصيد", f"{net_balance:.2f} t CO2e/ha", "Carbon Negative" if net_balance < 0 else "Carbon Positive")

with tab2:
    st.subheader("🌾 بيانات الموسم الزراعي")
    st.info("قم بمراجعة إعدادات المدخلات من الشريط الجانبي الأيسر.")
    st.write(f"- السماد النيتروجيني المستخدم: {nitrogen} كجم/هكتار")
    st.write(f"- نوع التربة: تربة طينية ميسرة للتحليل العضوي")

with tab3:
    st.subheader("💨 محاسبة غازات الاحتباس الحراري (IPCC)")
    st.markdown(f"### **إجمالي الانبعاثات:** `{gross_ghg:.2f}` t CO2e/ha/yr")
    st.markdown(f"### **إجمالي الاحتجاز:** `{carbon_removal_tCO2:.2f}` t CO2e/ha/yr")
    st.markdown(f"## **صافي الرصيد:** `{net_balance:.2f}` t CO2e/ha/yr")
    if net_balance < 0:
        st.success("✅ المزرعة سالبة الكربون (Net Carbon-Negative)")
    else:
        st.warning("⚠️ المزرعة مصدر صافي للانبعاثات")

with tab4:
    st.subheader("🤖 تحليل الذكاء الاصطناعي (XAI)")
    X_dummy = pd.DataFrame({
        'Nitrogen': np.random.uniform(50, 180, 100),
        'Water': np.random.uniform(2500, 6000, 100),
        'SOC': np.random.uniform(10, 25, 100),
    })
    y_dummy = 3.0 + 0.012 * X_dummy['Nitrogen'] + 0.18 * X_dummy['SOC']
    model = RandomForestRegressor(n_estimators=30, random_state=42).fit(X_dummy, y_dummy)
    imp = pd.DataFrame({'Feature': ['السماد النيتروجيني', 'مياه الري', 'كربون التربة'], 'Importance': model.feature_importances_})
    fig = px.bar(imp, x='Importance', y='Feature', orientation='h', title="أهمية المتغيرات في النموذج")
    st.plotly_chart(fig, use_container_width=True)
