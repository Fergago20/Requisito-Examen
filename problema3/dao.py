class Daopaciente:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def obtener_pacientes(self):
        return self.pacientes
    def eliminar_paciente(self, nombre):
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                self.pacientes.remove(paciente)
                return True
        return False

    def filtrar_pacientes(self, prioridad):
        return filter(lambda p: p.prioridad == prioridad, self.pacientes)
    
    def primero(self):
        if self.pacientes:
            return self.pacientes[0]
        return None