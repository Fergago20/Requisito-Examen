import tkinter as tk
from tkinter import messagebox
import listaenlazada as le
from datetime import datetime

lista = le.ListaEnlazada()

def agregar_ruta():
    lugar = lugar_entry.get()
    tiempo_str = tiempo_entry.get()
    try:
        tiempo = datetime.strptime(tiempo_str, "%H:%M").strftime("%H:%M")
        lista.agregar(lugar, tiempo)
        messagebox.showinfo("Éxito", f"Ruta '{lugar}' agregada con tiempo {tiempo}.")
    except ValueError:
        messagebox.showerror("Error", "Formato de tiempo inválido. Use HH:MM.")
def eliminar_ruta():
    lugar = lugar_entry.get()
    if lista.eliminar(lugar):
        messagebox.showinfo("Éxito", f"Ruta '{lugar}' eliminada.")
    else:
        messagebox.showerror("Error", f"Ruta '{lugar}' no encontrada.")

def mostrar_tiempo_total():
    tiempo_total = lista.tiempo_total()
    messagebox.showinfo("Tiempo Total", f"Tiempo total: {tiempo_total}")

def mostrar_ruta_total():
    ruta = lista.ruta_total()
    ruta_str = "\n".join([f"Lugar: {lugar}, Tiempo: {tiempo}" for lugar, tiempo in ruta])
    messagebox.showinfo("Ruta Total", ruta_str if ruta_str else "No hay rutas.")

def agregar_ruta_inicio():
    lugar = lugar_entry.get()
    tiempo_str = tiempo_entry.get()
    try:
        tiempo = datetime.strptime(tiempo_str, "%H:%M")
        lista.agregar_inicio(lugar, tiempo)
        messagebox.showinfo("Éxito", f"Ruta '{lugar}' agregada al inicio.")
    except ValueError:
        messagebox.showerror("Error", "Formato de tiempo inválido. Use HH:MM.")

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Rutas")

# Crear widgets
lugar_label = tk.Label(root, text="Lugar:")
lugar_label.grid(row=0, column=0, padx=5, pady=5)
lugar_entry = tk.Entry(root)
lugar_entry.grid(row=0, column=1, padx=5, pady=5)

tiempo_label = tk.Label(root, text="Tiempo (HH:MM):")
tiempo_label.grid(row=1, column=0, padx=5, pady=5)
tiempo_entry = tk.Entry(root)
tiempo_entry.grid(row=1, column=1, padx=5, pady=5)

agregar_btn = tk.Button(root, text="Agregar Ruta", command=agregar_ruta)
agregar_btn.grid(row=2, column=0, padx=5, pady=5)

eliminar_btn = tk.Button(root, text="Eliminar Ruta", command=eliminar_ruta)
eliminar_btn.grid(row=2, column=1, padx=5, pady=5)

mostrar_tiempo_btn = tk.Button(root, text="Mostrar Tiempo Total", command=mostrar_tiempo_total)
mostrar_tiempo_btn.grid(row=3, column=0, padx=5, pady=5)

mostrar_ruta_btn = tk.Button(root, text="Mostrar Ruta Total", command=mostrar_ruta_total)
mostrar_ruta_btn.grid(row=3, column=1, padx=5, pady=5)

agregar_inicio_btn = tk.Button(root, text="Agregar Ruta al Inicio", command=agregar_ruta_inicio)
agregar_inicio_btn.grid(row=4, column=0, padx=5, pady=5)

salir_btn = tk.Button(root, text="Salir", command=root.quit)
salir_btn.grid(row=4, column=1, padx=5, pady=5)

# Iniciar bucle de la aplicación
root.mainloop()