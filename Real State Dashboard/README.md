\# Real Estate Dashboard - Arriendos en Teusaquillo, Bogotá



Dashboard interactivo en Python que analiza los datos de arriendos extraídos por el bot de UiPath (`Real State Bot`).



\## Qué muestra

\- Precio promedio y mediano de los avisos

\- Precio promedio por metro cuadrado (COP/m²)

\- Gráfico de dispersión de precio vs área

\- Ranking de avisos con menor precio por m²



\## Tecnologías

\- Python 3.11

\- Streamlit

\- Pandas

\- Plotly



\## Cómo ejecutarlo

1\. Clona este repositorio

2\. Instala las dependencias:

&#x20;  pip install -r requirements.txt

3\. Ejecuta:

&#x20;  streamlit run app.py



\## Flujo completo

1\. El bot de UiPath extrae precio y área de los avisos y genera `Resultados.csv`

2\. El dashboard limpia los datos, calcula el precio por m² y los visualiza



\## Autora

Andrea Bur

