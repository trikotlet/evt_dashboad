import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")
st.title("📊 Дашборд по загруженным данным")

uploaded_file = st.file_uploader("Загрузите Excel-файл", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name=0)

    st.subheader("📋 Исходные данные")
    st.dataframe(df)

    st.sidebar.header("🔍 Фильтры")
    month = st.sidebar.selectbox("Месяц", options=df["Месяц"].dropna().unique())
    stream = st.sidebar.selectbox("Стрим", options=["Все"] + df["Стрим"].dropna().unique().tolist())

    filtered_df = df[df["Месяц"] == month]
    if stream != "Все":
        filtered_df = filtered_df[filtered_df["Стрим"] == stream]

    st.subheader("📊 Отфильтрованные данные")
    st.dataframe(filtered_df)

    chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X("ФИО специалиста:N", sort='-y'),
        y="Стоимость, руб.:Q",
        tooltip=["ФИО специалиста", "Стоимость, руб."]
    ).properties(title="Стоимость по специалистам")

    st.altair_chart(chart, use_container_width=True)
