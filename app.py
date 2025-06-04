import streamlit as st
import pandas as pd
from tabs.pivot_utils import build_pivot_table

st.set_page_config(layout="wide")
st.title("📊 Ежемесячный дашборд")

uploaded_file = st.file_uploader("Загрузите Excel-файл", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name=0)

    tabs = st.tabs([
        "🧭 По направлениям (ч/д)",
        "💸 По направлениям (руб.)",
        "👨‍💼 По CoStream (ч/д)",
    ])

    with tabs[0]:
        st.subheader("🧭 Ресурсы по Направлению в ч/д")
        table = build_pivot_table(df, "Направление", "Факт, ч/д")
        st.dataframe(table.style.format("{:.2f}"), use_container_width=True)

    with tabs[1]:
        st.subheader("💸 Стоимость по Направлению")
        table = build_pivot_table(df, "Направление", "Стоимость, руб.")
        st.dataframe(table.style.format("{:,.0f}"), use_container_width=True)

    with tabs[2]:
        st.subheader("👨‍💼 Ресурсы по CoStream в ч/д")
        table = build_pivot_table(df, "CoStream", "Факт, ч/д")
        st.dataframe(table.style.format("{:.2f}"), use_container_width=True)

else:
    st.info("Пожалуйста, загрузите Excel-файл для начала работы.")
