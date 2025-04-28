from fastapi import FastAPI, Query
from threading import Timer
import random

app = FastAPI()

cache = {}

def refrescar_cache():
    global cache
    # Refrescar la cache simulada
    cache = {
        ("MAD", "BCN", "2024-06-01"): [
            {"proveedor": "Cache", "origen": "MAD", "destino": "BCN", "precio": random.randint(90, 110)}
        ]
    }
    Timer(600, refrescar_cache).start()  # Refresca cada 10 minutos

@app.on_event("startup")
def startup_event():
    refrescar_cache()

@app.get("/cache")
def obtener_cache(origen: str, destino: str, fecha: str):
    return cache.get((origen, destino, fecha), [])
