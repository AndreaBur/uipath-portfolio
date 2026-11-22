from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Real Estate Dashboard", layout="wide")
st.title("Dashboard de arriendos - Teusaquillo, Bogotá")
st.caption("Datos extraídos con un bot de UiPath y analizados con Python")

# Cargar y limpiar datos
df = pd.read_csv(Path(__file__).parent / "Resultados.csv")
df["Precio"] = df["Precio"].astype(str).str.replace(".", "", regex=False).astype(float)
df["Area"] = df["Area"].astype(float)
df["Precio_m2"] = df["Precio"] / df["Area"]

# Indicadores clave
col1, col2, col3 = st.columns(3)
col1.metric("Precio promedio", f"${df['Precio'].mean():,.0f}")
col2.metric("Precio mediano", f"${df['Precio'].median():,.0f}")
col3.metric("Precio promedio por m²", f"${df['Precio_m2'].mean():,.0f}")

# Gráfico de dispersión
fig = px.scatter(
    df,
    x="Area",
    y="Precio",
    color="Precio_m2",
    hover_data=["Precio_m2"],
    title="Precio vs área",
    labels={"Area": "Área (m²)", "Precio": "Precio (COP)", "Precio_m2": "COP por m²"},
)
st.plotly_chart(fig, use_container_width=True)

# Ranking de ofertas
st.subheader("Avisos con menor precio por m²")
ranking = df.sort_values("Precio_m2").reset_index(drop=True)
st.dataframe(ranking, use_container_width=True)
