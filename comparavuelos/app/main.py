from fastapi import FastAPI, Query
import httpx
import asyncio

app = FastAPI()

PROVEEDORES = [
    "http://proveedor1vuelos:8001/vuelos",
    "http://proveedor2vuelos:8002/vuelos",
    "http://proveedor3vuelos:8003/vuelos"
]

CACHE = "http://cachevuelos:8004/cache"

@app.get("/buscar")
async def buscar_vuelos(origen: str, destino: str, fecha: str):
    async with httpx.AsyncClient() as client:
        # Consultar la cache primero
        cache_response = await client.get(CACHE, params={"origen": origen, "destino": destino, "fecha": fecha})
        if cache_response.status_code == 200 and cache_response.json():
            return {"fuente": "cache", "vuelos": cache_response.json()}

        # Si no hay cache, consultar proveedores en paralelo
        tasks = [client.get(url, params={"origen": origen, "destino": destino, "fecha": fecha}) for url in PROVEEDORES]
        responses = await asyncio.gather(*tasks)

        vuelos = []
        for response in responses:
            if response.status_code == 200:
                vuelos.extend(response.json())

        # Opcional: aplicar filtros, ordenamientos, etc.
        vuelos.sort(key=lambda x: x["precio"])

        return {"fuente": "proveedores", "vuelos": vuelos}
