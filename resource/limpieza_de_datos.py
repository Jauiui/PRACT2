import pandas as pd
from unidecode import unidecode
from sklearn.preprocessing import StandardScaler

currentDir = os.getcwd()
filename = "peliculas.csv"
filePath = os.path.join(currentDir, filename)
df = pd.read_csv(filePath, encoding="utf-8")

# Realizamos un análisis previo de la estructura y otros datos del dataframe
print("Dimensiones del DataFrame:")
print(df.shape)

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nEstadísticas descriptivas de columnas numéricas:")
print(df.describe())

print("\nEstadísticas de columnas categóricas:")
print(df.describe(include=["object"]))

# Eliminamos valores sin sentido
def remove_personas_from_protagonist(text):
    if isinstance(text, str):
        values = text.split(", ")
        filtered_values = [value for value in values if "persona" not in value.lower()]
        return ", ".join(filtered_values)
    return text

df["Protagonistas"] = df["Protagonistas"].apply(remove_personas_from_protagonist)

# Debido a que tenemos columnas con varios valores, vamos a elegir el valor más repetido a lo largo del dataframe para cada columna como
# representante de la columna per sé. Esto nos ayudará a un análisis más claro de los datos categóricos, simplificando los datos de manera útil
# para los ejercicios de clustering o regresión consiguientes. Además trando los valores de texto.
def get_frequent_value(column, freq_dict):
    if isinstance(column, str):
        truncated_values = [" ".join(value.split()[:2]) for value in column.split(", ")]
        truncated_values_normalized = [unidecode(value.lower()) for value in truncated_values]
        value_counts = {value: freq_dict.get(value, 0) for value in truncated_values_normalized}
        return max(value_counts.items(), key=lambda x: (x[1], -truncated_values_normalized.index(x[0])))[0] if value_counts else None
    return None

columns_to_process = ["Director", "Pais", "Genero", "Protagonistas", "Idioma", "Producción", "Guion", "Música", "Fotografía", "Vestuario", "Productora"]

freq_dicts = {}
for column in columns_to_process:
    all_values = df[column].str.split(", ").explode().value_counts()
    freq_dicts[column] = all_values.to_dict()

for column in columns_to_process:
    df[f"MF_{column}"] = df[column].apply(lambda x: get_frequent_value(x, freq_dicts[column]))

# Estandarizamos las variables numéricas
scaler = StandardScaler()

df["st_Duración"] = scaler.fit_transform(df[["Duración (Minutos)"]])
df["st_Presupuesto"] = scaler.fit_transform(df[["Presupuesto (Dólares)"]])
df["st_Recaudación"] = scaler.fit_transform(df[["Recaudación (Dólares)"]])

# Corregimos los tipos de datos necesarios
df["Año"] = df["Año"].str.extract(r"(\d{4})")
df["Año"] = pd.to_numeric(df["Año"])

columns_to_convert = ["MF_Director", "MF_Pais", "MF_Genero", "MF_Protagonistas",
                      "MF_Idioma", "MF_Producción", "MF_Guion", "MF_Música",
                      "MF_Fotografía", "MF_Vestuario", "MF_Productora"]

for column in columns_to_convert: # En python, lo equivalente a convertir en factor es category
    df[column] = df[column].astype("category")

print("\nTipos de datos:")
print(df.dtypes)

print("\nEstadísticas descriptivas de columnas numéricas:")
print(df.describe())

print("\nEstadísticas de columnas categóricas:")
print(df.describe(include=["object"]))

# Imprimir el resultado
print("\nDataframe limpiado:")
print(df)

df.head(20)

currentDir = os.getcwd()
filename = "peliculas_clean.csv"
filePath = os.path.join(currentDir, filename)
df.to_csv(filePath)
