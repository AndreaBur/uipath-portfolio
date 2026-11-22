# Real Estate Bot - Búsqueda de apartamentos en arriendo

Bot RPA desarrollado en UiPath Studio que automatiza la búsqueda de apartamentos en arriendo en Teusaquillo, Bogotá, y exporta los resultados a un archivo CSV.

## Qué hace
- Abre el portal inmobiliario Ciencuadras en Chrome
- Aplica los filtros: arriendo, 1 habitación y 1 baño
- Ordena los resultados de menor a mayor precio
- Recorre los 20 avisos de la primera página
- Extrae el precio y el área (m²) de cada aviso usando expresiones regulares (Regex)
- Guarda los datos en una DataTable y los exporta a `Resultados.csv`

## Tecnologías
- UiPath Studio
- For Each UI Element, Get Text, Build Data Table, Add Data Row, Write CSV
- Regex en VB.NET

## Cómo ejecutarlo
1. Clona este repositorio
2. Abre `project.json` en UiPath Studio
3. Ajusta la ruta del archivo en la actividad **Write CSV** a tu equipo
4. Ejecuta `Main.xaml`

## Resultado
Archivo `Resultados.csv` con las columnas `Precio` y `Area`.

## Aprendizajes
- Automatización de navegador web con selectores
- Cómo extraer datos cuando la página no separa los campos (Get Text + Regex)
- Uso de `CurrentElement` para recorrer elementos de una lista
- Construcción y exportación de DataTables

## Autora
Andrea Bur
