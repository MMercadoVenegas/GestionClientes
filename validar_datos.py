import tkinter as tk
from tkinter import messagebox

def obtener_si_no(mensaje, entry):
    respuesta = entry.get().strip().lower()
    if respuesta in ['si', 's']:
        return True
    elif respuesta in ['no', 'n']:
        return False
    else:
        messagebox.showerror("Error", "Valor inválido, intente otra vez con si/no")
        return None

def obtener_numero(mensaje, entry):
    try:
        numero = int(entry.get().strip())
        if 0 <= numero <= 999:
            return numero
        else:
            messagebox.showerror("Error", "Número inválido, ingrese un valor entre 0 y 999")
            return None
    except ValueError:
        messagebox.showerror("Error", "Valor inválido, ingrese un número entero")
        return None
    
def singular_o_plural(cantidad, singular, plural):
    return singular if cantidad == 1 else plural

