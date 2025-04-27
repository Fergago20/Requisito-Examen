import clase as c
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, accion):
        nuevo_nodo = c.Nodo(accion)
        if self.cabeza is None:
            self.cabeza= nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente= nuevo_nodo
            nuevo_nodo.anterior= self.cola
            self.cola= nuevo_nodo
        
    def eliminar_ultima(self):
        if self.cabeza is None:
            return None
        elif self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola= self. cola.anterior
            self.cola.siguiente= None
        
    def dar_anterior(self, nodo):
        return nodo.anterior
    
    def dar_siguiente(self, nodo):
        return nodo.siguiente
    
    def dar_cola(self):
        return self.cola