from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

app = FastAPI()

diccionario_usuarios = {
    1: {"id": 1, "nombre": "Aldo", "edad": 58},
    2: {"id": 2, "nombre": "Claudia", "edad": 56},
    3: {"id": 3, "nombre": "Ivan", "edad": 25},
    4: {"id": 4, "nombre": "Andre", "edad": 23},
    5: {"id": 5, "nombre": "Bruno", "edad": 18}
}

@app.get("/info")
def read_root():
    return {
    "nombre": "Andre",
  "edad": 23,
  "color_favorito": "#008f39"
}

#DTO: Data Transfer Object
class UsuarioDTO(BaseModel):
    nombre: str
    edad: int

@app.post("/v1/usuario")
def crear_user_body(usuario: UsuarioDTO):
    id_usuario = len(diccionario_usuarios) + 1
    nuevo_usuario = {"nombre": usuario.nombre}
    diccionario_usuarios[id_usuario] = nuevo_usuario
    return diccionario_usuarios[id_usuario]




@app.post("/v1/usuario_incorrecto")
def crear_usuario(usuario_nombre: str, usuario_edad: int):
    nuevo_id = max(diccionario_usuarios.keys()) + 1
    nuevo_usuario = {"id": nuevo_id, "nombre": usuario_nombre, "edad": usuario_edad}
    diccionario_usuarios[nuevo_id] = nuevo_usuario
    return nuevo_usuario

@app.get("/v1/usuarios")
def read_usuarios():
    return diccionario_usuarios

@app.get("/v1/usuarios/{id}")
def read_usuario(id: int):

    return usuarios.get(id, {"error": "Usuario no encontrado"})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}