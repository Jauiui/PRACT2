from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score
from sklearn.impute import KNNImputer
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np
import os

currentDir = os.getcwd()
filename = "../dataset/peliculas_clean.csv"
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

# Dividir características (X) y objetivo (y)
predictores = ["MF_Director_encoded", "MF_Pais_encoded", "MF_Genero_encoded", "MF_Protagonistas_encoded",
               "MF_Idioma_encoded", "MF_Producción_encoded", "MF_Guion_encoded", "MF_Música_encoded", "MF_Fotografía_encoded",
               "MF_Vestuario_encoded", "MF_Productora_encoded", "st_Duración", "st_Presupuesto", "st_Recaudación"]

X = df[predictores]
y = df["Ganador"].astype("category").cat.codes

imputer = KNNImputer(n_neighbors=3)

# Perform KNN imputation
X_imputed = imputer.fit_transform(X)

neighbors = NearestNeighbors(n_neighbors=4)  # min_samples = 4
neighbors_fit = neighbors.fit(X_imputed)
distances, indices = neighbors_fit.kneighbors(X_imputed)

# Ordenar distancias y graficar
distances = np.sort(distances[:, 3])  # k-th neighbor distance
plt.plot(distances)
plt.title("k-Distance Plot")
plt.xlabel("Puntos Ordenados")
plt.ylabel("Distancia al Vecino Más Cercano")
plt.show()

# Fit the pipeline
dbscan = DBSCAN(eps=1.5, min_samples=2)
clusters = dbscan.fit_predict(X_imputed)

sil_score = silhouette_score(X_imputed, dbscan.labels_)
print(f"Silhouette Score: {sil_score}")

#un puntaje de 0.6562727963202605, cercano a 1, indica una buena separación de clusters

db_index = davies_bouldin_score(X_imputed, dbscan.labels_)
print(f"Davies-Bouldin Index: {db_index}")
#un puntaje 1.1993081867403577 es un valor muy cercano a 1, que es el valor optimo

ch_score = calinski_harabasz_score(X_imputed, dbscan.labels_)
print(f"Calinski-Harabasz Index: {ch_score}")
#Un puntaje de 70.87615695157243

# Calcular puntajes de silhouette
if len(set(dbscan.labels_)) > 1:  # Al menos 2 clusters
    silhouette_vals = silhouette_samples(X_imputed, dbscan.labels_)
    
    y_lower, y_upper = 0, 0
    for i, cluster in enumerate(np.unique(dbscan.labels_)):
        cluster_silhouette_vals = silhouette_vals[dbscan.labels_ == cluster]
        cluster_silhouette_vals.sort()
        y_upper += len(cluster_silhouette_vals)
        plt.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_vals)
        y_lower += len(cluster_silhouette_vals)

    plt.axvline(silhouette_score(X_imputed, dbscan.labels_), color="red", linestyle="--")
    plt.title("Gráfico de Silhouette")
    plt.xlabel("Coeficiente de Silhouette")
    plt.ylabel("Clusters")
    plt.show()
else:
    print("No se puede calcular el gráfico de Silhouette: hay un solo cluster o solo ruido.")
