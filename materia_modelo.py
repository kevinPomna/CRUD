import sqlite3

class MateriaModelo:
    def __init__(self, db_nombre):
        self.conexion = sqlite3.connect(db_nombre)
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS materias (id INTEGER PRIMARY KEY, nombre TEXT, nro_creditos INTEGER, carrera TEXT, aula TEXT)")
        self.conexion.commit()

    def crear_materia(self, nombre, nro_creditos, carrera, aula):
        self.cursor.execute("INSERT INTO materias (nombre, nro_creditos, carrera, aula) VALUES (?, ?, ?, ?)", (nombre, nro_creditos, carrera, aula))
        self.conexion.commit()

    def actualizar_materia(self, id, nombre, nro_creditos, carrera, aula):
        self.cursor.execute("UPDATE materias SET nombre=?, nro_creditos=?, carrera=?, aula=? WHERE id=?", (nombre, nro_creditos, carrera, aula, id))
        self.conexion.commit()

    def borrar_materia(self, id):
        self.cursor.execute("DELETE FROM materias WHERE id=?", (id,))
        self.conexion.commit()

    def consultar_materia(self, id):
        self.cursor.execute("SELECT * FROM materias WHERE id=?", (id,))
        return self.cursor.fetchone()
