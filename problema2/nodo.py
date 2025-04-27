class Nodo:
    def __init__(self, lugar, tiempo):
        self.lugar = lugar
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f"Lugar: {self.lugar}, Tiempo: {self.tiempo}"