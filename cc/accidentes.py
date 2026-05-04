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

plt.figure()
plt.plot(df_mes["MES"], df_mes["total"])
plt.title("Fallecidos por mes")
plt.savefig("mes.png")
plt.close()

top_dep = df_dep.head(10)
plt.figure()
plt.bar(top_dep["DEPARTAMENTO"], top_dep["total"])
plt.xticks(rotation=45)
plt.title("Top departamentos")
plt.savefig("departamentos.png")
plt.close()

plt.figure()
plt.plot(df_hora["HORA"], df_hora["total"])
plt.title("Fallecidos por hora")
plt.savefig("hora.png")
plt.close()

plt.figure()
plt.bar(df_sexo["SEXO"], df_sexo["total"])
plt.title("Fallecidos por sexo")
plt.savefig("sexo.png")
plt.close()