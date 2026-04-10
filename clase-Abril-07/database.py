# database.py
import sqlite3

DB_PATH = "imc.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS personas (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre  TEXT    NOT NULL,
            peso    REAL    NOT NULL,
            talla   REAL    NOT NULL,
            imc     REAL    NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Crea la BD al ejecutar el archivo directamente
if __name__ == "__main__":
    init_db()
    print("Base de datos 'imc.db' creada exitosamente ✓")