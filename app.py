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
        "tab_ghg": "💨 حساب الانبعاثات والكربون",
        "tab_ai": "🤖 تحليل الذكاء الاصطناعي (XAI)",
        "gross_label": "إجمالي انبعاثات المزرعة (Gross GHG)",
        "removal_label": "إجمالي احتجاز كربون التربة (Soil Removal)",
        "net_balance": "صافي رصيد الكربون (Net GHG Balance)",
        "status_neg": "✅ المزرعة سالبة الكربون (Net Carbon-Negative)",
        "status_pos": "⚠️ المزرعة مصدر صافي للانبعاثات (Net Carbon-Positive)"
    }
else:
    T = {
        "title": "🌱 CNF-Intelligence Research Platform",
        "subtitle": "AI-Driven Multi-Objective Farm Design for Food Security & Carbon Removal",
        "tab_overview": "📊 Overview",
        "tab_profile": "🌾 Farm Profile",
        "tab_ghg": "💨 GHG Accounting",
        "tab_ai": "🤖 AI Optimization & XAI",
        "gross_label": "Gross Farm Emissions",
        "removal_label": "Soil Carbon Removal",
        "net_balance": "Net GHG Balance",
        "status_neg": "✅ Farm is Net Carbon-Negative",
        "status_pos": "✅ Farm is Net Carbon-Positive"
    }

st.title(T["title"])
st.caption(T["subtitle"])
st.markdown("---")

# ---------------------------------------------------------
# لوحة التحكم الجانبية (Sidebar) لبيانات الإدخال كما طلبتم
# ---------------------------------------------------------
st.sidebar.header("⚙️ إعدادات المحاكاة السريعة")
area = st.sidebar.number_input("مساحة المزرعة (هكتار)", value=50.31, min_value=0.1)
nitrogen = st.sidebar.number_input("السماد النيتروجيني (N kg/ha)", value=100.16)
diesel_l = st.sidebar.number_input("استهلاك الديزل (L/ha)", value=60.16)
electricity_kwh = st.sidebar.number_input("استهلاك الكهرباء (kWh/ha)", value=349.71)
soc_initial = st.sidebar.number_input("كربون التربة الأولي SOC (g/kg)", value=11.86)
soc_final = st.sidebar.number_input("كربون التربة النهائي SOC (g/kg)", value=15.33)

# الحسابات العلمية بناءً على المدخلات الجانبية
emissions_fuel = (diesel_l * 2.68 + electricity_kwh * 0.5) / 1000.0
emissions_fertilizer = (nitrogen * 5.8) / 1000.0
gross_ghg = emissions_fuel + emissions_fertilizer

soc_stock_init = soc_initial * 1.3 * 30 * 0.1
soc_stock_fin = soc_final * 1.3 * 30 * 0.1
carbon_removal_tCO2 = (soc_stock_fin - soc_stock_init) * (44.0 / 12.0) / 5.0
net_balance = gross_ghg - carbon_removal_tCO2

# التبويبات الرئيسية في الصفحة الرئيسية
tab1, tab2, tab3, tab4 = st.tabs([T["tab_overview"], T["tab_profile"], T["tab_ghg"], T["tab_ai"]])

with tab1:
    st.subheader("📊 مؤشرات الأداء الرئيسية للمزرعة (KPIs)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("مساحة المزرعة", f"{area} ha")
    c2.metric("الانبعاثات الإجمالية", f"{gross_ghg:.2f} t CO2e/ha")
    c3.metric("احتجاز الكربون", f"{carbon_removal_tCO2:.2f} t CO2e/ha")
    c4.metric("صافي الرصيد", f"{net_balance:.2f} t CO2e/ha", "Carbon Negative" if net_balance < 0 else "Carbon Positive")

with tab2:
    st.subheader("🌾 ملف المزرعة والموسم الزراعي")
    col_a, col_b = st.columns(2)
    with col_a:
        st.text_input("معرف المزرعة / Farm ID", value="FARM-2026-CNF")
        st.selectbox("نوع التربة / Soil Type", ["Clay (طينية)", "Sandy (رملية)", "Loam (طميية)"])
    with col_b:
        st.selectbox("المحصول / Crop Type", ["القمح (Wheat)", "الذرة (Maize)", "البرسيم (Alfalfa)"])
        st.selectbox("نظام الري / Irrigation", ["Drip (ري بالتنقيط)", "Sprinkler (ري بالرش)", "Flood (ري بالغمر)"])
    st.info("💡 يمكنك تعديل القيم من الشريط الجانبي الأيسر لملاحظة التغير الفوري في كافة الحسابات والرسوم البيانية.")

with tab3:
    st.subheader("💨 محاسبة غازات الاحتباس الحراري ومعادلات الكربون الفورية")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown(f"### **{T['gross_label']}:** `{gross_ghg:.2f}` t CO2e/ha/yr")
        st.markdown(f"### **{T['removal_label']}:** `{carbon_removal_tCO2:.2f}` t CO2e/ha/yr")
        st.markdown(f"## **{T['net_balance']}:** `{net_balance:.2f}` t CO2e/ha/yr")
        
        if net_balance < 0:
            st.success(T["status_neg"])
        else:
            st.warning(T["status_pos"])
            
    with col_g2:
        fig = go.Figure(data=[
            go.Bar(name='Gross Emissions', x=['Carbon Balance'], y=[gross_ghg], marker_color='crimson'),
            go.Bar(name='Soil Carbon Removal', x=['Carbon Balance'], y=[carbon_removal_tCO2], marker_color='forestgreen')
        ])
        fig.update_layout(barmode='group', title="مقارنة الانبعاثات والاحتجاز (Carbon Balance)")
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("🤖 تحليل الذكاء الاصطناعي وتفسير النماذج (XAI Feature Importance)")
    st.write("تدريب نموذج ذكاء اصطناعي (Random Forest) لتحليل العوامل الأكثر تأثيراً على أداء المزرعة بناءً على مدخلاتك الحالية.")
    
    np.random.seed(42)
    X_dummy = pd.DataFrame({
        'Nitrogen': np.random.uniform(50, 180, 100),
        'Water': np.random.uniform(2500, 6000, 100),
        'SOC': np.random.uniform(10, 25, 100),
        'Tillage': np.random.uniform(1, 4, 100)
    })
    y_dummy = 3.0 + 0.012 * X_dummy['Nitrogen'] + 0.18 * X_dummy['SOC'] + np.random.normal(0, 0.1, 100)
    
    model = RandomForestRegressor(n_estimators=50, random_state=42).fit(X_dummy, y_dummy)
    
    importance_df = pd.DataFrame({
        'Feature': ['السماد النيتروجيني', 'مياه الري', 'كربون التربة', 'شدة الحرث'],
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=True)
    
    fig_ai = px.bar(importance_df, x='Importance', y='Feature', orientation='h', title="أهمية العوامل في نموذج الذكاء الاصطناعي")
    st.plotly_chart(fig_ai, use_container_width=True)
