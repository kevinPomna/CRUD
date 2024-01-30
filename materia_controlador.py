from materia_modelo import MateriaModelo
from materia_vista import MateriaVista

class MateriaControlador:
    def __init__(self):
        self.modelo = MateriaModelo("materias.db")
        self.vista = MateriaVista()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre, nro_creditos, carrera, aula = self.vista.obtener_datos_materia()
                self.modelo.crear_materia(nombre, nro_creditos, carrera, aula)
            elif opcion == '2':
                id = self.vista.obtener_id_materia()
                nombre, nro_creditos, carrera, aula = self.vista.obtener_datos_materia()
                self.modelo.actualizar_materia(id, nombre, nro_creditos, carrera, aula)
            elif opcion == '3':
                id = self.vista.obtener_id_materia()
                self.modelo.borrar_materia(id)
            elif opcion == '4':
                id = self.vista.obtener_id_materia()
                materia = self.modelo.consultar_materia(id)
                if materia:
                    self.vista.mostrar_materia(materia)
                else:
                    print("La materia no existe.")
            elif opcion == '5':
                print("¡Adiós!")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    controlador = MateriaControlador()
    controlador.ejecutar()
