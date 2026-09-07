import pandas as pd


#PARTE 1
df = pd.read_csv("src/4-proyecto_pipeline_basico/hollywood.csv")

columnas = [
    "Movie",
    "LeadStudio",
    "Genre",
    "RottenTomatoes",
    "AudienceScore",
    "WorldGross",
    "Budget",
    "Year"
]

df = df[columnas]

print(df.head())
# PARTE 1


# PARTE 2
# Para columnas de texto, reemplazar nulls
df["Genre"] = df["Genre"].fillna("Desconocido")
df["LeadStudio"] = df["LeadStudio"].fillna("Desconocido")

# Para columnas numéricas, reemplazar con la mediana
df["RottenTomatoes"] = df["RottenTomatoes"].fillna(df["RottenTomatoes"].median())
df["AudienceScore"] = df["AudienceScore"].fillna(df["AudienceScore"].median())

# Para columnas relevantes pero con datos poco significativos, eliminar filas
df = df.dropna(subset=["WorldGross", "Budget"])

print("\n\n\nConteo de nulos:\n", df.isnull().sum())
print("\n\n\nForma:\n", df.shape)
# PARTE 2


# PARTE 3
# Crear columna Ganancia
df["Profit"] = df["WorldGross"] - df["Budget"]

# Crear columna Exitosa
df["Successful"] = df["RottenTomatoes"] >= 60


print("\n\n\nColumnas nuevas:\n", df[["Movie", "Profit", "Successful"]].head())
print("\n\n\nConteo de películas exitosas y no exitosas:\n", df["Successful"].value_counts())
# PARTE 3 

# PARTE 4
print("\n\n\nTipos de las columnas:\n", df.dtypes)

# Ordenar por ganancia de mayor a menor
df_sorted = df.sort_values(by="Profit", ascending=False)


print("\n\n\n3 películas más rentables:\n", df_sorted[["Movie", "Profit"]].head(3))
# PARTE 4


# PARTE 5
genre_avg = df.groupby("Genre")["RottenTomatoes"].mean().round(1)
print("\n\n\nPromedio de RottenTomatoes por género:\n",genre_avg)

studio_avg = df.groupby("LeadStudio")["Profit"].mean().round(1)
print("\n\n\nPromedio de Ganancia por estudio:\n", studio_avg)
# PARTE 5

# PARTE 6
df.to_csv("src/4-proyecto_pipeline_basico/hollywood_clean.csv", index=False)
df_clean = pd.read_csv("src/4-proyecto_pipeline_basico/hollywood_clean.csv")
print("\n\n\nForma del nuevo data set:\n", df_clean.shape)
print("\n\n\nValores nulos del nuevo data set:\n", df_clean.isnull().sum().sum())
# PARTE 6