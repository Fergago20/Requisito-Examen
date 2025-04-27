import tkinter as tk
from tkinter import messagebox
import dao as dao
import clase as c

administrar = dao.Daoestudiante()

def agregar():
    def guardar_estudiante():
        carnet = entry_carnet.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        try:
            peso = float(entry_peso.get())
            estatura = float(entry_estatura.get())
            promedio = float(entry_promedio.get())
        except ValueError:
            messagebox.showerror("Error", "Peso, estatura y promedio deben ser números.")
            return
        sexo = entry_sexo.get()
        estudiante = c.Estudiante(carnet, nombre, apellido, peso, estatura, sexo, promedio)
        administrar.agregar_estudiante(estudiante)
        messagebox.showinfo("Éxito", f"Estudiante {nombre} agregado.")
        agregar_window.destroy()

    agregar_window = tk.Toplevel(root)
    agregar_window.title("Agregar Estudiante")

    tk.Label(agregar_window, text="Carnet:").grid(row=0, column=0)
    entry_carnet = tk.Entry(agregar_window)
    entry_carnet.grid(row=0, column=1)

    tk.Label(agregar_window, text="Nombre:").grid(row=1, column=0)
    entry_nombre = tk.Entry(agregar_window)
    entry_nombre.grid(row=1, column=1)

    tk.Label(agregar_window, text="Apellido:").grid(row=2, column=0)
    entry_apellido = tk.Entry(agregar_window)
    entry_apellido.grid(row=2, column=1)

    tk.Label(agregar_window, text="Peso:").grid(row=3, column=0)
    entry_peso = tk.Entry(agregar_window)
    entry_peso.grid(row=3, column=1)

    tk.Label(agregar_window, text="Estatura:").grid(row=4, column=0)
    entry_estatura = tk.Entry(agregar_window)
    entry_estatura.grid(row=4, column=1)

    tk.Label(agregar_window, text="Sexo:").grid(row=5, column=0)
    entry_sexo = tk.Entry(agregar_window)
    entry_sexo.grid(row=5, column=1)

    tk.Label(agregar_window, text="Promedio:").grid(row=6, column=0)
    entry_promedio = tk.Entry(agregar_window)
    entry_promedio.grid(row=6, column=1)

    tk.Button(agregar_window, text="Guardar", command=guardar_estudiante).grid(row=7, column=0, columnspan=2)

def buscar():
    def buscar_estudiante():
        carnet = entry_carnet.get()
        estudiante = administrar.buscar_estudiante(carnet)
        if estudiante:
            messagebox.showinfo("Resultado", str(estudiante))
        else:
            messagebox.showerror("Error", "Estudiante no encontrado.")
        buscar_window.destroy()

    buscar_window = tk.Toplevel(root)
    buscar_window.title("Buscar Estudiante")

    tk.Label(buscar_window, text="Carnet:").grid(row=0, column=0)
    entry_carnet = tk.Entry(buscar_window)
    entry_carnet.grid(row=0, column=1)

    tk.Button(buscar_window, text="Buscar", command=buscar_estudiante).grid(row=1, column=0, columnspan=2)

def eliminar():
    def eliminar_estudiante():
        carnet = entry_carnet.get()
        if administrar.eliminar_estudiante(carnet):
            messagebox.showinfo("Éxito", f"Estudiante con carnet {carnet} eliminado.")
        else:
            messagebox.showerror("Error", "Estudiante no encontrado.")
        eliminar_window.destroy()

    eliminar_window = tk.Toplevel(root)
    eliminar_window.title("Eliminar Estudiante")

    tk.Label(eliminar_window, text="Carnet:").grid(row=0, column=0)
    entry_carnet = tk.Entry(eliminar_window)
    entry_carnet.grid(row=0, column=1)

    tk.Button(eliminar_window, text="Eliminar", command=eliminar_estudiante).grid(row=1, column=0, columnspan=2)

def mostrar():
    estudiantes = administrar.obtener_estudiantes()
    if estudiantes:
        estudiantes_str = "\n".join(str(est) for est in estudiantes)
        messagebox.showinfo("Estudiantes", estudiantes_str)
    else:
        messagebox.showinfo("Estudiantes", "No hay estudiantes registrados.")

def ordenar(parametro):
    administrar.bubble_sort(parametro)
    estudiantes = administrar.obtener_estudiantes()
    estudiantes_str = "\n".join(str(est) for est in estudiantes)
    messagebox.showinfo("Estudiantes Ordenados", estudiantes_str)

root = tk.Tk()
root.title("Gestión de Estudiantes")

tk.Button(root, text="Agregar Estudiante", command=agregar).pack(pady=5)
tk.Button(root, text="Buscar Estudiante", command=buscar).pack(pady=5)
tk.Button(root, text="Eliminar Estudiante", command=eliminar).pack(pady=5)
tk.Button(root, text="Mostrar Estudiantes", command=mostrar).pack(pady=5)
tk.Button(root, text="Ordenar por Nombre", command=lambda: ordenar("nombre")).pack(pady=5)
tk.Button(root, text="Ordenar por Promedio", command=lambda: ordenar("promedio")).pack(pady=5)
tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

root.mainloop()