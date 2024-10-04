valor_arriendo = input ("Ingresar valor de arriendo: $")
valor_arriendo = int(valor_arriendo)
req_ren = valor_arriendo * 2.8

valor_ggcc = input ("Ingresar valor de Gastos comunes: $")
valor_ggcc = int(valor_ggcc)

metros_cuad_t = input ("Ingresar metros cuadrados totales: ")
metros_cuad_t = float(metros_cuad_t)

metros_cuad_u = input ("Ingresar metros cuadrados utiles: ")
metros_cuad_u = float(metros_cuad_u)

cant_hab = input ("Ingresar cantidad de habitaciones: ")
cant_banos = input ("Ingresar cantidad de baños: ")

def obtener_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ['si', 's']:
            return True
        elif respuesta in ['no', 'n']:
            return False
        else:
            print("Valor inválido, intente otra vez con si/no")

def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje).strip())
            if 0 <= numero <= 999:
                return numero
            else:
                print("Número inválido, ingrese un valor entre 0 y 999")
        except ValueError:
            print("Valor inválido, ingrese un número entero")                

mascota = obtener_si_no("¿Se aceptan mascotas? si/no: ")
mensaje_mascota = "-Admite mascotas." if mascota else "-No admite mascotas."

estacionamiento = obtener_si_no("¿Cuenta con estacionamiento? si/no: ")
if estacionamiento:
    nro_est = obtener_numero("Ingresar el N° de estacionamiento: ")
    mensaje_estacionamiento = f"-Tiene estacionamiento N°: {nro_est}."
else:
    mensaje_estacionamiento = "-No tiene estacionamiento."

bodega = obtener_si_no("¿Tiene bodega? si/no: ")
if bodega:
    nro_bodega = obtener_numero("Ingrese el N° de bodega: ")
    mensaje_bodega = f"-Tiene bodega N°: {nro_bodega}."
else:
    mensaje_bodega = "-No tiene bodega."

terraza = obtener_si_no("¿Cuenta con terrza? si/no: ")
mensaje_terraza = "-Tiene terraza." if terraza else "-No tiene terraza."

amoblado = obtener_si_no("¿Está amoblada? si/no: ")
mensaje_amoblado = "-Amoblada." if amoblado else "-Sin amoblar."

otros_req = []
hay_otros_req = obtener_si_no("Otros requisitos si/no: ")
if hay_otros_req:
    while True:
        requisito = input("Ingrese un requisito, presione enter para salir").strip()
        if requisito:
            otros_req.append(requisito)
        else:
            break

print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("A continuación te comparto la documentación requerida para ver esta propiedad:")
print (" ")
print(f"Renta líquida igual o superior a 2.8 veces el valor del arriendo, ${req_ren:,.0f}\n")
print (" ")
print ("Si eres dependiente:")
print (" ")
print ("-Copia o foto de carnet de identidad vigente por ambos lados.")
print ("-Copia o foto de Contrato de trabajo o certificado de antigüedad laboral, en los cuales se especifique tipo de contrato indefinido.")
print ("-3 últimas liquidaciones de sueldo.")
print ("-12 últimas cotizaciones de AFP.")
print (" ")
print ("Si eres independiente: ")
print (" ")
print ("-Copia o foto de carnet de identidad vigente por ambos lados.")
print ("-Formulario 22 (F22) de los 2 últimos años.")

#completar otros requisitos
if otros_req:
    print("\nOtros requisitos: ")
    for requisito in otros_req:
        print(f"-{requisito}")
    
print ("\nCaracterísticas de la propiedad: \n")
print (f"-Arriendo: ${valor_arriendo:,.0f}.")
print (f"-GGCC: ${valor_ggcc:,.0f}.")
print ("-" + cant_hab + " Habitaciones.")
print ("-" + cant_banos + " Baños.")
print (mensaje_mascota)
print (mensaje_bodega)
print (mensaje_estacionamiento)
print (f"-Superficie de {metros_cuad_t} m2 totales, {metros_cuad_u} m2 útiles.")
print (mensaje_terraza)
print (mensaje_amoblado)
