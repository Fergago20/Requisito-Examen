import nodo as N

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar(self, lugar, tiempo):
        if self.cabeza is None:
            self.cabeza = N.Nodo(lugar, tiempo)
            self.cola = self.cabeza
        else:
            nuevo_nodo = N.Nodo(lugar, tiempo)
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, lugar):
        if self.cabeza is None:
            return False

        if self.cabeza.lugar == lugar:
            self.cabeza = self.cabeza.siguiente
            return True

        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.lugar == lugar:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return True
            nodo_actual = nodo_actual.siguiente

        return False

    
    def tiempo_total(self):
        if self.cabeza is None:
            return 0
        tiempos = []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            tiempos.append(nodo_actual.tiempo)
            nodo_actual = nodo_actual.siguiente
        total = sum([int(tiempo.split(':')[0]) * 60 + int(tiempo.split(':')[1]) for tiempo in tiempos])
        horas = total // 60
        minutos = total % 60
        return f"{horas:02}:{minutos:02}"

    def ruta_total(self):
        if self.cabeza is None:
            return []
        ruta= []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            ruta.append([nodo_actual.lugar, nodo_actual.tiempo])
            nodo_actual = nodo_actual.siguiente
        return ruta

    def agregar_inicio(self, lugar, tiempo):
        if self.cabeza is None:
            self.cabeza = N.Nodo(lugar, tiempo)
            self.cola = self.cabeza
            return
        nuevo_nodo= N.Nodo(lugar, tiempo)
        nuevo_nodo.siguiente= self.cabeza
        self.cabeza= nuevo_nodo
        if self.cola is None:
            self.cola= nuevo_nodo