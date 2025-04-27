import tkinter as tk
from tkinter import messagebox, simpledialog  # Importa simpledialog
import clase as c
import dao as d

versiones = d.ListaEnlazada()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Versiones")
        
        # Botones principales
        self.btn_agregar = tk.Button(root, text="Agregar Versión", command=self.agregar_version)
        self.btn_agregar.pack(pady=5)
        
        self.btn_eliminar = tk.Button(root, text="Eliminar Última Versión", command=self.eliminar_version)
        self.btn_eliminar.pack(pady=5)
        
        self.btn_mostrar = tk.Button(root, text="Mostrar Versiones", command=self.mostrar_versiones)
        self.btn_mostrar.pack(pady=5)
        
        self.btn_salir = tk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.pack(pady=5)
    
    def agregar_version(self):
        accion = simpledialog.askstring("Agregar Versión", "Ingrese la acción a realizar:")  # Usa simpledialog
        if accion:
            nodo = c.Nodo(accion)
            versiones.agregar(nodo)
            messagebox.showinfo("Éxito", f"Versión '{accion}' agregada.")
    
    def eliminar_version(self):
        if versiones.cabeza is None:
            messagebox.showwarning("Advertencia", "No hay versiones para eliminar.")
        else:
            versiones.eliminar_ultima()
            messagebox.showinfo("Éxito", "Última versión eliminada.")
    
    def mostrar_versiones(self):
        if versiones.cabeza is None:
            messagebox.showinfo("Información", "No hay versiones disponibles.")
            return
        
        self.ventana_versiones = tk.Toplevel(self.root)
        self.ventana_versiones.title("Versiones")
        
        self.nodo_actual = versiones.dar_cola()
        
        self.lbl_accion = tk.Label(self.ventana_versiones, text=f"Acción: {self.nodo_actual.accion}")
        self.lbl_accion.pack(pady=10)
        
        self.btn_siguiente = tk.Button(self.ventana_versiones, text="Siguiente Acción", command=self.siguiente_accion)
        self.btn_siguiente.pack(side=tk.LEFT, padx=5)
        
        self.btn_anterior = tk.Button(self.ventana_versiones, text="Acción Anterior", command=self.anterior_accion)
        self.btn_anterior.pack(side=tk.LEFT, padx=5)
        
        self.btn_cerrar = tk.Button(self.ventana_versiones, text="Cerrar", command=self.ventana_versiones.destroy)
        self.btn_cerrar.pack(side=tk.LEFT, padx=5)
    
    def siguiente_accion(self):
        if self.nodo_actual.siguiente is None:
            messagebox.showinfo("Información", "No hay siguiente acción.")
        else:
            self.nodo_actual = versiones.dar_siguiente(self.nodo_actual)
            self.lbl_accion.config(text=f"{self.nodo_actual.accion}")
    
    def anterior_accion(self):
        if self.nodo_actual.anterior is None:
            messagebox.showinfo("Información", "No hay acción anterior.")
        else:
            self.nodo_actual = versiones.dar_anterior(self.nodo_actual)
            self.lbl_accion.config(text=f"Acción: {self.nodo_actual.accion}")

# Crear la ventana principal
root = tk.Tk()
app = App(root)
root.mainloop()