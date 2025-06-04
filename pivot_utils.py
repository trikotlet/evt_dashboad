import streamlit as st
import pandas as pd

def build_pivot_table(df, index_field, value_field, columns_field="Специальность", aggfunc="sum"):
    try:
        pivot = df.pivot_table(
            index=index_field,
            columns=columns_field,
            values=value_field,
            aggfunc=aggfunc,
            fill_value=0
        )

        for col in ["Аналитик", "Разработчик"]:
            if col not in pivot.columns:
                pivot[col] = 0

        pivot["Общий итог"] = pivot[["Аналитик", "Разработчик"]].sum(axis=1)

        # Добавим строку "Общий итог"
        total_row = pd.DataFrame(pivot.sum(numeric_only=True)).T
        total_row.index = ["Общий итог"]

        full_table = pd.concat([pivot, total_row])
        return full_table

    except Exception as e:
        st.error(f"Ошибка построения сводной таблицы: {e}")
        return pd.DataFrame()
