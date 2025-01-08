from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import RocCurveDisplay
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import catboost as cb
import pandas as pd

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

print(df.columns)

# Dividir características (X) y objetivo (y)
predictores = ["MF_Director_encoded", "MF_Pais_encoded", "MF_Genero_encoded", "MF_Protagonistas_encoded",
               "MF_Idioma_encoded", "MF_Producción_encoded", "MF_Guion_encoded", "MF_Música_encoded", "MF_Fotografía_encoded",
               "MF_Vestuario_encoded", "MF_Productora_encoded", "st_Duración", "st_Presupuesto", "st_Recaudación"]

X = df[predictores]
y = df["Ganador"].astype("category").cat.codes

print(X)
print(y)

df_combined = X.copy()
df_combined["Ganador"] = y  # Añadir la columna de y (objetivo)

plt.figure(figsize=(10, 8))
sns.heatmap(df_combined.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor de las Correlaciones entre X e y")
plt.show()

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de Árbol de Decisión
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)
print(classification_report(y_test, dt_pred))
cm = confusion_matrix(y_test, dt_pred)
print("Matriz de cofusión:")
print(cm)

plt.figure(figsize=(15, 10))
plot_tree(dt_model, filled=True, feature_names=X.columns, class_names=[str(i) for i in y.unique()], rounded=True)
plt.show()

plt.figure(figsize=(10, 6))
plt.barh(X_train.columns, dt_model.feature_importances_, align="center")
plt.title("Árbol de Decisión - Importancia de las Características")
plt.show()

# Modelo de Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
print(classification_report(y_test, rf_pred))
cm = confusion_matrix(y_test, rf_pred)
print("Matriz de cofusión:")
print(cm)

plt.figure(figsize=(15, 10))
plot_tree(rf_model.estimators_[0], filled=True, feature_names=X.columns, class_names=[str(i) for i in y.unique()])
plt.show()

plt.figure(figsize=(10, 6))
plt.barh(X_train.columns, rf_model.feature_importances_, align="center")
plt.title("Random Forest - Importancia de las Características")
plt.show()

# Modelo de CatBoost (Gradient Boosting)
cat_model = cb.CatBoostClassifier(random_state=42, verbose=0)
cat_model.fit(X_train, y_train)

cat_pred = cat_model.predict(X_test)
print(classification_report(y_test, cat_pred))
cm = confusion_matrix(y_test, cat_pred)
print("Matriz de cofusión:")
print(cm)

plt.figure(figsize=(10, 6))
plt.barh(X_train.columns, cat_model.feature_importances_, align="center")
plt.title("CatBoost - Importancia de las Características")
plt.show()

# Curva ROC para todos los modelos
plt.figure(figsize=(8, 6))
RocCurveDisplay.from_estimator(dt_model, X_test, y_test, name="Árbol de Decisión")
plt.plot([0, 1], [0, 1], "k--", label="Aleatorio (AUC = 0.5)")
plt.title("Curva ROC para Árbol de Decisión")
plt.xlabel("Falsos Positivos")
plt.ylabel("Verdaderos Positivos")
plt.legend(loc="lower right")

RocCurveDisplay.from_estimator(rf_model, X_test, y_test, name="Random Forest")
plt.plot([0, 1], [0, 1], "k--", label="Aleatorio (AUC = 0.5)")
plt.title("Curva ROC para Random Forest")
plt.xlabel("Falsos Positivos")
plt.ylabel("Verdaderos Positivos")
plt.legend(loc="lower right")

RocCurveDisplay.from_estimator(cat_model, X_test, y_test, name="CatBoost")
plt.plot([0, 1], [0, 1], "k--", label="Aleatorio (AUC = 0.5)")
plt.title("Curva ROC para CatBoost")
plt.xlabel("Falsos Positivos")
plt.ylabel("Verdaderos Positivos")
plt.legend(loc="lower right")

plt.show()
