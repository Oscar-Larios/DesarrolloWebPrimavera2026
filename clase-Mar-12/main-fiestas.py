from fastapi import FastAPI
from utils import generar_guid
from models import Fiesta, Invitado

app = FastAPI()

fiestas_en_memoria = {} 
invitados_en_memoria = {}

###########################################
#                 Fiestas                 #
###########################################

@app.post("/Fiesta")
def crear_fiesta(fiesta: Fiesta):
    id_generado = generar_guid()
    fiestas_en_memoria[id_generado] = {
        "id": id_generado, 
        "nombre": fiesta.nombre,
        "fecha": fiesta.fecha,
        "lugar": fiesta.lugar,
        "activo": True
    }
    return fiestas_en_memoria[id_generado]

@app.get("/Fiestas")
def read_fiestas(tipo: str | None = None):
    if tipo == "activas":
        return [fiesta for fiesta in fiestas_en_memoria.values() if fiesta["activo"]==True]
    elif tipo == "canceladas":
        return [fiesta for fiesta in fiestas_en_memoria.values() if fiesta["activo"]==False]
    return list(fiestas_en_memoria.values())

@app.get("/Fiestas/{id}")
def read_fiesta_id(id: str):
    return fiestas_en_memoria.get(id, {"error": "Fiesta no encontrada"})

@app.post("/Fiesta/{id}")
def cancelar_fiesta(id: str):
    if id in fiestas_en_memoria:
        fiestas_en_memoria[id]["activo"] = False
        return {"mensaje": "Fiesta cancelada"}
    return {"error": "Fiesta no encontrada"}

@app.get("/Fiesta/{id}/Invitados")
def obtener_invitados_fiesta(id: str):
    if id in fiestas_en_memoria:
        invitados_fiesta = []
        for invitado in invitados_en_memoria.values():
            if id in invitado["fiestas_registrado"]:
                invitados_fiesta.append(invitado)
        return invitados_fiesta

###########################################
#                 Invitados               #
###########################################

@app.post("/Invitado")
def crear_invitado(invitado: Invitado):
    id_generado = generar_guid()
    invitados_en_memoria[id_generado] = {
        "id": id_generado, 
        "nombre": invitado.nombre, 
        "fiestas_registrado": invitado.fiestas_registrado
    }
    return invitados_en_memoria[id_generado]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)