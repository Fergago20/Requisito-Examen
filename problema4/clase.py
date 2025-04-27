class Nodo:
    def __init__(self, accion):
        self.accion= accion
        self.siguiente = None
        self.anterior = None
    def __str__(self):
        return f"Accion: {self.accion}"