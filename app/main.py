from fastapi import FastAPI
from proyecto import release_2019, release_2020, release_2021

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