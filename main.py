import tkinter as tk
from tkinter import messagebox, scrolledtext
from validar_datos import singular_o_plural, obtener_si_no, obtener_numero


def agregar_asterisco(frame, texto):
    label_texto = tk.Label(frame, text=texto, anchor='w')
    label_texto.pack(side=tk.LEFT)
    label_asterisco = tk.Label(frame, text=" *", fg="red", anchor='w')
    label_asterisco.pack(side=tk.LEFT)
    
def calcular_renta():
    try:
        valor_arriendo = int(entry_valor_arriendo.get())
        req_ren = valor_arriendo * 2.8
        messagebox.showinfo("Resultado", f"Renta líquida igual o superior a 2.8 veces el valor del arriendo, ${req_ren:,.0f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor de arriendo válido")

def obtener_datos():
    try:
        valor_arriendo = int(entry_valor_arriendo.get())
        valor_ggcc = int(entry_valor_ggcc.get())
        metros_cuad_t = float(entry_metros_cuad_t.get()) 
        metros_cuad_u = float(entry_metros_cuad_u.get()) 
        cant_hab = int(entry_cant_hab.get())
        cant_banos = int(entry_cant_banos.get())

        mascota = obtener_si_no("¿Se aceptan mascotas? si/no: ", entry_mascota)
        estacionamiento = obtener_si_no("¿Cuenta con estacionamiento? si/no: ", entry_estacionamiento)
        bodega = obtener_si_no("¿Tiene bodega? si/no: ", entry_bodega)
        terraza = obtener_si_no("¿Cuenta con terraza? si/no: ", entry_terraza)
        amoblado = obtener_si_no("¿Está amoblada? si/no: ", entry_amoblado)

        if estacionamiento:
            nro_est = obtener_numero("Ingresar el N° de estacionamiento", entry_nro_est)
            mensaje_estacionamiento = f"-Tiene estacionamiento N°: {nro_est}."
        else:
            mensaje_estacionamiento = "-No tiene estacionamiento."

        if bodega:
            nro_bodega = obtener_numero("Ingrese el N° de bodega", entry_nro_bodega)
            mensaje_bodega = f"-Tiene bodega N°: {nro_bodega}."
        else:
            mensaje_bodega = "-No tiene bodega."

        hab_plural = singular_o_plural(cant_hab, "Habitación", "Habitaciones")
        banos_plural = singular_o_plural(cant_banos, "Baño", "Baños")

        ventana_resultados = tk.Toplevel(root)
        ventana_resultados.title("Resultados")

        text_resultado = scrolledtext.ScrolledText(ventana_resultados, width=80, height=20, wrap=tk.WORD)
        text_resultado.pack(padx=10, pady=10)
        text_resultado.insert(tk.END, f"""
        Renta líquida igual o superior a 2.8 veces el valor del arriendo, ${valor_arriendo * 2.8:,.0f}

        Características de la propiedad:
        -Arriendo: ${valor_arriendo:,.0f}.
        -GGCC: ${valor_ggcc:,.0f}.
        -{cant_hab} {hab_plural}.
        -{cant_banos} {banos_plural}.
        {'-Admite mascotas.' if mascota else '-No admite mascotas.'}
        {mensaje_estacionamiento}.
        {mensaje_bodega}.
        -Superficie de {metros_cuad_t} m2 totales, {metros_cuad_u} m2 útiles.
        {'-Tiene terraza.' if terraza else '-No tiene terraza.'}
        {'-Amoblada.' if amoblado else '-Sin amoblar.'}
        """)
        text_resultado.config(state=tk.DISABLED)

        def copiar_al_portapapeles():
            root.clipboard_clear()
            root.clipboard_append(text_resultado.get("1.0", tk.END))
            messagebox.showinfo("Copiar al portapapeles", "El texto ha sido copiado al portapapeles")

        btn_copiar = tk.Button(ventana_resultados, text="Copiar al Portapapeles", command=copiar_al_portapapeles)
        btn_copiar.pack(padx=10, pady=10)

    except ValueError:
        messagebox.showerror("Error", "Verifique que todos los campos estén correctamente llenos")


root = tk.Tk()
root.title("Calculadora de Renta")

# Crear y colocar los widgets en la ventana
frame_valor_arriendo = tk.Frame(root)
frame_valor_arriendo.grid(row=0, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_valor_arriendo, "Ingresar valor de arriendo:")
entry_valor_arriendo = tk.Entry(root)
entry_valor_arriendo.grid(row=0, column=1, padx=10, pady=10)

frame_valor_ggcc = tk.Frame(root)
frame_valor_ggcc.grid(row=1, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_valor_ggcc, "Ingresar valor de Gastos comunes:")
entry_valor_ggcc = tk.Entry(root)
entry_valor_ggcc.grid(row=1, column=1, padx=10, pady=10)

frame_metros_cuad_t = tk.Frame(root)
frame_metros_cuad_t.grid(row=2, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_metros_cuad_t, "Ingresar metros cuadrados totales:")
entry_metros_cuad_t = tk.Entry(root)
entry_metros_cuad_t.grid(row=2, column=1, padx=10, pady=10)

frame_metros_cuad_u = tk.Frame(root)
frame_metros_cuad_u.grid(row=3, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_metros_cuad_u, "Ingresar metros cuadrados útiles:")
entry_metros_cuad_u = tk.Entry(root)
entry_metros_cuad_u.grid(row=3, column=1, padx=10, pady=10)

frame_cant_hab = tk.Frame(root)
frame_cant_hab.grid(row=4, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_cant_hab, "Ingresar cantidad de habitaciones:")
entry_cant_hab = tk.Entry(root)
entry_cant_hab.grid(row=4, column=1, padx=10, pady=10)

frame_cant_banos = tk.Frame(root)
frame_cant_banos.grid(row=5, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_cant_banos, "Ingresar cantidad de baños:")
entry_cant_banos = tk.Entry(root)
entry_cant_banos.grid(row=5, column=1, padx=10, pady=10)

frame_mascota = tk.Frame(root)
frame_mascota.grid(row=6, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_mascota, "¿Se aceptan mascotas? si/no:")
entry_mascota = tk.Entry(root)
entry_mascota.grid(row=6, column=1, padx=10, pady=10)

frame_estacionamiento = tk.Frame(root)
frame_estacionamiento.grid(row=7, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_estacionamiento, "¿Cuenta con estacionamiento? si/no:")
entry_estacionamiento = tk.Entry(root)
entry_estacionamiento.grid(row=7, column=1, padx=10, pady=10)

label_nro_est = tk.Label(root, text="N° de estacionamiento:", anchor='w')
label_nro_est.grid(row=8, column=0, padx=10, pady=10, sticky='w')
entry_nro_est = tk.Entry(root)
entry_nro_est.grid(row=8, column=1, padx=10, pady=10)

frame_bodega = tk.Frame(root)
frame_bodega.grid(row=9, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_bodega, "¿Tiene bodega? si/no:")
entry_bodega = tk.Entry(root)
entry_bodega.grid(row=9, column=1, padx=10, pady=10)

label_nro_bodega = tk.Label(root, text="N° de bodega:", anchor='w')
label_nro_bodega.grid(row=10, column=0, padx=10, pady=10, sticky='w')
entry_nro_bodega = tk.Entry(root)
entry_nro_bodega.grid(row=10, column=1, padx=10, pady=10)

frame_terraza = tk.Frame(root)
frame_terraza.grid(row=11, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_terraza, "¿Cuenta con terraza? si/no:")
entry_terraza = tk.Entry(root)
entry_terraza.grid(row=11, column=1, padx=10, pady=10)

frame_amoblado = tk.Frame(root)
frame_amoblado.grid(row=12, column=0, padx=10, pady=10, sticky='w')
agregar_asterisco(frame_amoblado, "¿Está amoblada? si/no:")
entry_amoblado = tk.Entry(root)
entry_amoblado.grid(row=12, column=1, padx=10, pady=10)

btn_calcular_renta = tk.Button(root, text="Calcular Renta", command=calcular_renta)
btn_calcular_renta.grid(row=13, column=0, padx=10, pady=10)

btn_obtener_datos = tk.Button(root, text="Obtener Datos", command=obtener_datos)
btn_obtener_datos.grid(row=13, column=1, padx=10, pady=10)

root.mainloop()