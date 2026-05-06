import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

df = pd.read_csv("fallecidos-nueva-2019.csv", encoding="latin-1")
df.columns = df.columns.str.strip().str.upper()
df["FECHAYHORA"] = pd.to_datetime(df["FECHAYHORA"], errors="coerce")
df["MES"] = df["FECHAYHORA"].dt.month
df["HORA"] = df["FECHAYHORA"].dt.hour

cn = sqlite3.connect("fallecidos.db")
df.to_sql("fallecidos", cn, if_exists="replace", index=False)

df_mes = pd.read_sql("""
SELECT MES, COUNT(*) as total
FROM fallecidos
GROUP BY MES
ORDER BY MES
""", cn)

df_dep = pd.read_sql("""
SELECT DEPARTAMENTO, COUNT(*) as total
FROM fallecidos
GROUP BY DEPARTAMENTO
ORDER BY total DESC
""", cn)

df_hora = pd.read_sql("""
SELECT HORA, COUNT(*) as total
FROM fallecidos
GROUP BY HORA
ORDER BY HORA
""", cn)

df_sexo = pd.read_sql("""
SELECT SEXO, COUNT(*) as total
FROM fallecidos
GROUP BY SEXO
""", cn)

cn.close()

df_mes.to_csv("fallecidos_por_mes.csv", index=False)
df_dep.to_csv("fallecidos_por_departamento.csv", index=False)
df_hora.to_csv("fallecidos_por_hora.csv", index=False)
df_sexo.to_csv("fallecidos_por_sexo.csv", index=False)