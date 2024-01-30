class MateriaVista:
    def mostrar_menu(self):
        print("\n1. Crear Materia")
        print("2. Actualizar Materia")
        print("3. Borrar Materia")
        print("4. Consultar Materia")
        print("5. Salir")

    def obtener_datos_materia(self):
        nombre = input("Nombre de la materia: ")
        nro_creditos = int(input("Número de créditos: "))
        carrera = input("Carrera: ")
        aula = input("Aula: ")
        return nombre, nro_creditos, carrera, aula

    def obtener_id_materia(self):
        return int(input("Ingrese el ID de la materia: "))

    def mostrar_materia(self, materia):
        print("\nID:", materia[0])
        print("Nombre:", materia[1])
        print("Número de créditos:", materia[2])
        print("Carrera:", materia[3])
        print("Aula:", materia[4])
