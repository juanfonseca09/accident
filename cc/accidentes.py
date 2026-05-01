import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

df = pd.read_csv("fallecidos-nueva-2019.csv", encoding="latin-1")
df.columns = df.columns.str.strip().str.upper()
df["FECHAYHORA"] = pd.to_datetime(df["FECHAYHORA"], errors="coerce")
df["MES"] = df["FECHAYHORA"].dt.month
df["HORA"] = df["FECHAYHORA"].dt.hour

conn = sqlite3.connect("fallecidos.db")
df.to_sql("fallecidos", conn, if_exists="replace", index=False)
query_mes = """
SELECT MES, COUNT(*) as total
FROM fallecidos
GROUP BY MES
ORDER BY MES
"""
df_mes = pd.read_sql(query_mes, conn)
query_dep = """
SELECT DEPARTAMENTO, COUNT(*) as total
FROM fallecidos
GROUP BY DEPARTAMENTO
ORDER BY total DESC
"""
df_dep = pd.read_sql(query_dep, conn)
query_hora = """
SELECT HORA, COUNT(*) as total
FROM fallecidos
GROUP BY HORA
ORDER BY HORA
"""
df_hora = pd.read_sql(query_hora, conn)
query_sexo = """
SELECT SEXO, COUNT(*) as total
FROM fallecidos
GROUP BY SEXO
"""
df_sexo = pd.read_sql(query_sexo, conn)

print("\nFallecidos por mes:")
print(df_mes)
print("\nTop departamentos:")
print(df_dep.head())
print("\nFallecidos por hora:")
print(df_hora)
print("\nFallecidos por sexo:")
print(df_sexo)

conn.close()