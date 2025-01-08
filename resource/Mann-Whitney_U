from scipy.stats import mannwhitneyu
from scipy import stats

currentDir = os.getcwd()
filename = "peliculas_clean.csv"
filePath = os.path.join(currentDir, filename)
df = pd.read_csv(filePath, encoding="utf-8")

columns_to_encode = [
    "MF_Director", "MF_Pais", "MF_Genero", "MF_Protagonistas",
    "MF_Idioma", "MF_Producción", "MF_Guion", "MF_Música",
    "MF_Fotografía", "MF_Vestuario", "MF_Productora"
]

# Aplicar Frequency Encoding a cada una de las columnas
for column in columns_to_encode:
    frequency_encoding = df[column].value_counts() / len(df)
    df[column + "_encoded"] = df[column].map(frequency_encoding)

print("\nResultado de la prueba de Mann-Whitney U para las muestras nominados y ganadores mediante la variable st_Presupuesto:")
nominados = df[df["Ganador"] == 0]["st_Presupuesto"].dropna()
ganadores = df[df["Ganador"] == 1]["st_Presupuesto"].dropna()  

print(f"Número de muestras para 0 (nominados): {len(nominados)}")
print(f"Número de muestras para 1 (ganadores): {len(ganadores)}")

stat_nominados, p_value_nominados = stats.shapiro(nominados)
stat_ganadores, p_value_ganadores = stats.shapiro(ganadores)

print(f"Prueba de normalidad para nominados: Estadístico = {stat_nominados}, p-value = {p_value_nominados}")
print(f"Prueba de normalidad para ganadores: Estadístico = {stat_ganadores}, p-value = {p_value_ganadores}")

alpha = 0.05
if p_value_nominados < alpha:
    print("Los nominados NO siguen una distribución normal.")
else:
    print("Los nominados siguen una distribución normal.")
    
if p_value_ganadores < alpha:
    print("Los ganadores NO siguen una distribución normal.")
else:
    print("Los ganadores siguen una distribución normal.")

stat_levene, p_value_levene = stats.levene(nominados, ganadores)
print(f"Prueba de homocedasticidad (Levene): Estadístico = {stat_levene}, p-value = {p_value_levene}")

if p_value_levene < alpha:
    print("Las varianzas son diferentes (No se cumple homocedasticidad).")
else:
    print("Las varianzas son iguales.")

stat, p_value = mannwhitneyu(nominados, ganadores)
print(f"Estadístico U: {stat}")
print(f"Valor p: {p_value}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula: Las distribuciones son diferentes.")
else:
    print("No rechazamos la hipótesis nula: Las distribuciones son similares.")

print("\nResultado de la prueba de Mann-Whitney U para las muestras nominados y ganadores mediante la variable st_Duración:")
nominados = df[df["Ganador"] == 0]["st_Duración"].dropna()
ganadores = df[df["Ganador"] == 1]["st_Duración"].dropna()  

print(f"Número de muestras para 0 (nominados): {len(nominados)}")
print(f"Número de muestras para 1 (ganadores): {len(ganadores)}")

stat_nominados, p_value_nominados = stats.shapiro(nominados)
stat_ganadores, p_value_ganadores = stats.shapiro(ganadores)

print(f"Prueba de normalidad para nominados: Estadístico = {stat_nominados}, p-value = {p_value_nominados}")
print(f"Prueba de normalidad para ganadores: Estadístico = {stat_ganadores}, p-value = {p_value_ganadores}")

if p_value_nominados < alpha:
    print("Los nominados NO siguen una distribución normal.")
else:
    print("Los nominados siguen una distribución normal.")
    
if p_value_ganadores < alpha:
    print("Los ganadores NO siguen una distribución normal.")
else:
    print("Los ganadores siguen una distribución normal.")

stat_levene, p_value_levene = stats.levene(nominados, ganadores)
print(f"Prueba de homocedasticidad (Levene): Estadístico = {stat_levene}, p-value = {p_value_levene}")

if p_value_levene < alpha:
    print("Las varianzas son diferentes (No se cumple homocedasticidad).")
else:
    print("Las varianzas son iguales.")

stat, p_value = mannwhitneyu(nominados, ganadores)
print(f"Estadístico U: {stat}")
print(f"Valor p: {p_value}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula: Las distribuciones son diferentes.")
else:
    print("No rechazamos la hipótesis nula: Las distribuciones son similares.")

print("\nResultado de la prueba de Mann-Whitney U para las muestras nominados y ganadores mediante la variable st_Recaudación:")
nominados = df[df["Ganador"] == 0]["st_Recaudación"].dropna()
ganadores = df[df["Ganador"] == 1]["st_Recaudación"].dropna()  

print(f"Número de muestras para 0 (nominados): {len(nominados)}")
print(f"Número de muestras para 1 (ganadores): {len(ganadores)}")

stat_nominados, p_value_nominados = stats.shapiro(nominados)
stat_ganadores, p_value_ganadores = stats.shapiro(ganadores)

print(f"Prueba de normalidad para nominados: Estadístico = {stat_nominados}, p-value = {p_value_nominados}")
print(f"Prueba de normalidad para ganadores: Estadístico = {stat_ganadores}, p-value = {p_value_ganadores}")

if p_value_nominados < alpha:
    print("Los nominados NO siguen una distribución normal.")
else:
    print("Los nominados siguen una distribución normal.")
    
if p_value_ganadores < alpha:
    print("Los ganadores NO siguen una distribución normal.")
else:
    print("Los ganadores siguen una distribución normal.")

stat_levene, p_value_levene = stats.levene(nominados, ganadores)
print(f"Prueba de homocedasticidad (Levene): Estadístico = {stat_levene}, p-value = {p_value_levene}")

if p_value_levene < alpha:
    print("Las varianzas son diferentes (No se cumple homocedasticidad).")
else:
    print("Las varianzas son iguales.")

stat, p_value = mannwhitneyu(nominados, ganadores)
print(f"Estadístico U: {stat}")
print(f"Valor p: {p_value}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula: Las distribuciones son diferentes.")
else:
    print("No rechazamos la hipótesis nula: Las distribuciones son similares.")

print("\nResultado de la prueba de Mann-Whitney U para las muestras nominados y ganadores mediante la variable MF_Idioma_encoded:")
nominados = df[df["Ganador"] == 0]["MF_Idioma_encoded"].dropna()
ganadores = df[df["Ganador"] == 1]["MF_Idioma_encoded"].dropna()  

print(f"Número de muestras para 0 (nominados): {len(nominados)}")
print(f"Número de muestras para 1 (ganadores): {len(ganadores)}")

stat_nominados, p_value_nominados = stats.shapiro(nominados)
stat_ganadores, p_value_ganadores = stats.shapiro(ganadores)

print(f"Prueba de normalidad para nominados: Estadístico = {stat_nominados}, p-value = {p_value_nominados}")
print(f"Prueba de normalidad para ganadores: Estadístico = {stat_ganadores}, p-value = {p_value_ganadores}")

if p_value_nominados < alpha:
    print("Los nominados NO siguen una distribución normal.")
else:
    print("Los nominados siguen una distribución normal.")
    
if p_value_ganadores < alpha:
    print("Los ganadores NO siguen una distribución normal.")
else:
    print("Los ganadores siguen una distribución normal.")

stat_levene, p_value_levene = stats.levene(nominados, ganadores)
print(f"Prueba de homocedasticidad (Levene): Estadístico = {stat_levene}, p-value = {p_value_levene}")

if p_value_levene < alpha:
    print("Las varianzas son diferentes (No se cumple homocedasticidad).")
else:
    print("Las varianzas son iguales.")

stat, p_value = mannwhitneyu(nominados, ganadores)
print(f"Estadístico U: {stat}")
print(f"Valor p: {p_value}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula: Las distribuciones son diferentes.")
else:
    print("No rechazamos la hipótesis nula: Las distribuciones son similares.")
