class Estudiante:
    def __init__(self, carnet, nombre, apeliido, peso, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apeliido
        self.peso = peso
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio
    
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}, Carnet: {self.carnet}, Peso: {self.peso}, Estatura: {self.estatura}, Sexo: {self.sexo}, Promedio: {self.promedio}"
        