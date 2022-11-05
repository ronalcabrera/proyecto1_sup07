from fastapi import FastAPI
import pandas as pd

df = pd.read_csv('csv/netflix.csv')

# Cambio el tipo de dato a fecha
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Ordeno los valores por fecha de manera ascendente
df = df.sort_values(by=['date_added'])

# Reemplazo el valor 'Not Given' por None
df['director'] = df['director'].replace('Not Given', None)

# Creo nuevos Dataframes con el filtro por año de salida: 2019, 2020, 2021
release_2019 = df[df['release_year']==2019]
release_2020 = df[df['release_year']==2020]
release_2021 = df[df['release_year']==2021]

# Ahora los convierto en diccionario
release_2019.reset_index().to_dict(orient="index")
release_2020.reset_index().to_dict(orient="index")
release_2021.reset_index().to_dict(orient="index")

app = FastAPI()

@app.get("/2019")
async def index():
        return release_2019

@app.get("/2020")
async def index():
        return release_2020

@app.get("/2021")
async def index():
        return release_2021