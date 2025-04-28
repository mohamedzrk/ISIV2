from fastapi import FastAPI
from typing import List
import random

app = FastAPI()

@app.get("/vuelos")
def obtener_vuelos(origen: str, destino: str, fecha: str):
    vuelos = [
        {"proveedor": "Proveedor2", "origen": origen, "destino": destino, "precio": random.randint(100, 200)}
        for _ in range(2)
    ]
    return vuelos
