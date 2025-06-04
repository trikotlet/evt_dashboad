import pandas as pd
import io
import streamlit as st

def export_table_to_excel(df, sheet_name="Sheet1"):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=True, sheet_name=sheet_name)
    processed_data = output.getvalue()
    return processed_data

def render_export_button(df, label="📥 Скачать в Excel", filename="table_export.xlsx", sheet_name="Sheet1"):
    excel_data = export_table_to_excel(df, sheet_name=sheet_name)
    st.download_button(
        label=label,
        data=excel_data,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
