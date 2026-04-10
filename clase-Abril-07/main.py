# main.py
from fastapi import FastAPI
from models import Persona
from database import get_conn, init_db

app = FastAPI()
init_db()  # Crea la tabla al iniciar

@app.post("/calculate_imc/")
def calculate_imc(person: Persona):
    imc = person.peso / (person.talla ** 2)
    conn = get_conn()
    cursor = conn.execute(
        "INSERT INTO personas (nombre, peso, talla, imc) VALUES (?, ?, ?, ?)",
        (person.nombre, person.peso, person.talla, imc)
    )
    conn.commit()
    id_persona = cursor.lastrowid
    conn.close()
    return {"id": id_persona, "nombre": person.nombre,
            "peso": person.peso, "talla": person.talla, "imc": imc}

@app.get("/get_persona/{id_persona}")
def get_persona(id_persona: int):
    conn = get_conn()
    row = conn.execute(
        "SELECT * FROM personas WHERE id = ?", (id_persona,)
    ).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"error": "Persona no encontrada"}

@app.get("/get_all_personas/")
def get_all_personas():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM personas").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.put("/update_persona/{id_persona}")
def update_persona(id_persona: int, person: Persona):
    imc = person.peso / (person.talla ** 2)
    conn = get_conn()
    result = conn.execute(
        "UPDATE personas SET nombre=?, peso=?, talla=?, imc=? WHERE id=?",
        (person.nombre, person.peso, person.talla, imc, id_persona)
    )
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        return {"error": "Persona no encontrada"}
    return {"id": id_persona, "nombre": person.nombre,
            "peso": person.peso, "talla": person.talla, "imc": imc}

@app.delete("/delete_persona/{id_persona}")
def delete_persona(id_persona: int):
    conn = get_conn()
    result = conn.execute(
        "DELETE FROM personas WHERE id = ?", (id_persona,)
    )
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        return {"error": "Persona no encontrada"}
    return {"message": "Persona eliminada"}