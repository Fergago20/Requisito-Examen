import clase as c
class Daoestudiante:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def obtener_estudiantes(self):
        return self.estudiantes

    def buscar_estudiante(self, carnet):
        for estudiante in self.estudiantes:
            if estudiante.carnet == carnet:
                return estudiante
        return None

    def eliminar_estudiante(self, nombre):
        estudiante = self.buscar_estudiante(nombre)
        if estudiante:
            self.estudiantes.remove(estudiante)
            return True
        return False
    def bubble_sort(self, parametro):
        n = len(self.estudiantes)
        for i in range(n):
            for j in range(0, n-i-1):
                if getattr(self.estudiantes[j], parametro) > getattr(self.estudiantes[j+1], parametro):
                    self.estudiantes[j], self.estudiantes[j+1] = self.estudiantes[j+1], self.estudiantes[j]