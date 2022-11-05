from fastapi import FastAPI
from proyecto import dic2019, dic2020, dic2021

app = FastAPI()

@app.get("")
async def index():
        return {"Hola bb":"dame dinero"}

@app.get("/2019")
async def index():
        return dic2019

@app.get("/2020")
async def index():
        return dic2020

@app.get("/2021")
async def index():
        return dic2021