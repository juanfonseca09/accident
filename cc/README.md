# Análisis de fallecidos en siniestros de tránsito - Uruguay

Este proyecto analiza datos reales de fallecidos en siniestros de tránsito en Uruguay, con el objetivo de encontrar patrones en el tiempo, la ubicación y las características de las víctimas.

## Idea

La idea fue trabajar con datos reales y aplicar un flujo típico de análisis:

- Carga y limpieza de datos
- Uso de SQL para consultas
- Análisis en Python
- Generación de gráficos
- Interpretación de resultados

## Qué se hizo

- Se cargó un dataset en formato CSV
- Se creó una base de datos SQLite
- Se realizaron consultas SQL para agrupar información
- Se generaron gráficos con matplotlib
- Se extrajeron insights a partir de los datos

## Análisis realizados

- Fallecidos por mes
- Fallecidos por departamento
- Fallecidos por hora
- Fallecidos por sexo

## Insights

- Se observa un aumento de fallecidos hacia fin de año, con un pico en diciembre.
- Montevideo y Canelones concentran la mayor cantidad de casos, probablemente por su mayor población.
- Existen horarios críticos en la tarde-noche (18–20 hs), coincidiendo con momentos de mayor circulación.
- La mayoría de las víctimas son hombres, mostrando una diferencia marcada respecto a mujeres.

## Tecnologías

- Python (pandas, matplotlib)
- SQLite (SQL)

## Cómo ejecutar

```bash
python accidentes.py