from pydantic import BaseModel

class Fiesta(BaseModel):
    nombre: str
    fecha: str
    lugar: str

class Invitado(BaseModel):
    nombre: str
    fiestas_registrado: list[str] = []