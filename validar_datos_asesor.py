import tkinter as tk
from tkinter import messagebox
import subprocess  # Para ejecutar main.py

# Función para validar y guardar datos
def validar_y_guardar():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    genero = genero_var.get()

    if len(telefono) != 9 or not telefono.isdigit():
        messagebox.showerror("Error", "El número de teléfono debe tener 9 dígitos.")
    elif not validar_correo(correo):
        messagebox.showerror("Error", "Formato de correo electrónico no válido.")
    else:
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        # Ejecutar el archivo main.py
        subprocess.Popen(['python', 'main.py'])  # Ejecuta el archivo main.py
        root.destroy()  # Cierra la ventana actual

# Función para validar el formato de correo electrónico
def validar_correo(correo):
    return '@' in correo and '.' in correo

# Crear la interfaz de la ventana de validación de datos del asesor
root = tk.Tk()
root.title("Datos del Asesor")

tk.Label(root, text="Nombre y Apellido:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Número telefónico (+56):").grid(row=1, column=0, padx=10, pady=10)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Correo Electrónico:").grid(row=2, column=0, padx=10, pady=10)
entry_correo = tk.Entry(root)
entry_correo.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Género:").grid(row=3, column=0, padx=10, pady=10)
genero_var = tk.StringVar()
genero_var.set("Masculino")  # Valor por defecto
tk.Radiobutton(root, text="Masculino", variable=genero_var, value="Masculino").grid(row=3, column=1)
tk.Radiobutton(root, text="Femenino", variable=genero_var, value="Femenino").grid(row=3, column=2)

btn_guardar = tk.Button(root, text="Guardar", command=validar_y_guardar)
btn_guardar.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
