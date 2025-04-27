import tkinter as tk
from tkinter import messagebox
import clase as c
import dao as d

control = d.Daopaciente()

def agregar_paciente():
    def guardar_paciente():
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        sintoma = entry_sintoma.get()
        prioridad = int(entry_prioridad.get())
        paciente = c.Paciente(nombre, edad, sintoma, prioridad)
        control.agregar_paciente(paciente)
        messagebox.showinfo("Éxito", f"Paciente {nombre} agregado.")
        ventana_agregar.destroy()

    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Paciente")

    tk.Label(ventana_agregar, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Edad:").grid(row=1, column=0)
    entry_edad = tk.Entry(ventana_agregar)
    entry_edad.grid(row=1, column=1)

    tk.Label(ventana_agregar, text="Síntoma:").grid(row=2, column=0)
    entry_sintoma = tk.Entry(ventana_agregar)
    entry_sintoma.grid(row=2, column=1)

    tk.Label(ventana_agregar, text="Prioridad:").grid(row=3, column=0)
    entry_prioridad = tk.Entry(ventana_agregar)
    entry_prioridad.grid(row=3, column=1)

    tk.Button(ventana_agregar, text="Guardar", command=guardar_paciente).grid(row=4, column=0, columnspan=2)

def mostrar_pacientes():
    pacientes = control.obtener_pacientes()
    if not pacientes:
        messagebox.showinfo("Información", "No hay pacientes registrados.")
        return

    ventana_mostrar = tk.Toplevel(root)
    ventana_mostrar.title("Lista de Pacientes")

    for i, p in enumerate(pacientes):
        tk.Label(ventana_mostrar, text=f"Nombre: {p.nombre}, Edad: {p.edad}, Síntoma: {p.sintoma}, Prioridad: {p.prioridad}").grid(row=i, column=0)

def atender_paciente():
    def eliminar_paciente():
        nombre = entry_nombre.get()
        if control.eliminar_paciente(nombre):
            messagebox.showinfo("Éxito", f"Paciente {nombre} eliminado.")
        else:
            messagebox.showerror("Error", f"Paciente {nombre} no encontrado.")
        ventana_atender.destroy()

    ventana_atender = tk.Toplevel(root)
    ventana_atender.title("Atender Paciente")

    tk.Label(ventana_atender, text="Nombre del paciente:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana_atender)
    entry_nombre.grid(row=0, column=1)

    tk.Button(ventana_atender, text="Eliminar", command=eliminar_paciente).grid(row=1, column=0, columnspan=2)

def filtrar_pacientes():
    def mostrar_filtrados():
        prioridad = int(entry_prioridad.get())
        pacientes_filtrados = control.filtrar_pacientes(prioridad)
        if not pacientes_filtrados:
            messagebox.showinfo("Información", "No hay pacientes con esa prioridad.")
        else:
            ventana_filtrados = tk.Toplevel(root)
            ventana_filtrados.title("Pacientes Filtrados")
            for i, p in enumerate(pacientes_filtrados):
                tk.Label(ventana_filtrados, text=f"Nombre: {p.nombre}, Edad: {p.edad}, Síntoma: {p.sintoma}").grid(row=i, column=0)
        ventana_filtrar.destroy()

    ventana_filtrar = tk.Toplevel(root)
    ventana_filtrar.title("Filtrar Pacientes")

    tk.Label(ventana_filtrar, text="Prioridad:").grid(row=0, column=0)
    entry_prioridad = tk.Entry(ventana_filtrar)
    entry_prioridad.grid(row=0, column=1)

    tk.Button(ventana_filtrar, text="Filtrar", command=mostrar_filtrados).grid(row=1, column=0, columnspan=2)

def mostrar_primer_paciente():
    primer_paciente = control.primero()
    if primer_paciente:
        messagebox.showinfo("Primer Paciente", f"Nombre: {primer_paciente.nombre}, Edad: {primer_paciente.edad}, Síntoma: {primer_paciente.sintoma}")
    else:
        messagebox.showinfo("Información", "No hay pacientes registrados.")

root = tk.Tk()
root.title("Gestión de Pacientes")

tk.Button(root, text="Agregar Paciente", command=agregar_paciente).pack(pady=5)
tk.Button(root, text="Mostrar Pacientes", command=mostrar_pacientes).pack(pady=5)
tk.Button(root, text="Atender Paciente", command=atender_paciente).pack(pady=5)
tk.Button(root, text="Filtrar Pacientes por Prioridad", command=filtrar_pacientes).pack(pady=5)
tk.Button(root, text="Mostrar Primer Paciente", command=mostrar_primer_paciente).pack(pady=5)
tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

root.mainloop()