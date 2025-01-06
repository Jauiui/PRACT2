import pandas as pd
import re

# Leer el archivo CSV
df = pd.read_csv('peliculas.csv')

print(df['Protagonistas'].head())

def procesar_protagonistas(protagonistas):
    lista = protagonistas.split(', ')
    if re.match(r'^\d*\s*personas?$', lista[0], re.IGNORECASE):
        lista = lista[1:]  # Omitir el primer elemento
    return lista[:4]  # Tomar los primeros 4 después del filtro

def limpiar_columna(df, nombre_columna):
    
    df[nombre_columna] = df[nombre_columna].fillna('')

    if nombre_columna == 'Protagonistas':
        columna_limitada = df[nombre_columna].apply(procesar_protagonistas)
    else:
        columna_limitada = df[nombre_columna].str.split(', ').apply(lambda x: x[:4])

    # Expandir los protagonistas a columnas
    columna_limitada = columna_limitada.apply(pd.Series)

    # Renombrar columnas dinámicamente
    columna_limitada.columns = [f'{nombre_columna}_{i+1}' for i in range(columna_limitada.shape[1])]
    print(type(columna_limitada))
    df = pd.concat([df, columna_limitada], axis=1)
    df.drop(columns=[nombre_columna], inplace=True)
    return df

df = limpiar_columna(df, "Protagonistas")
df = limpiar_columna(df, "Producción")
df = limpiar_columna(df, "Guion")
df = limpiar_columna(df, "Música")
df = limpiar_columna(df, "Fotografía")
df = limpiar_columna(df, "Vestuario")
df = limpiar_columna(df, "Productora")

df.to_csv('peliculas2.csv', index=False, encoding='utf-8')
#protagonistas_expandido.to_csv('peliculas3.csv', index=False, encoding='utf-8')