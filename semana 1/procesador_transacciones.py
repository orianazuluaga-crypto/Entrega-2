# procesador_transacciones.py
# Paso 1: Programacion Estructurada - PE
# Lee transacciones de un archivo y las procesa con funciones.
# Cada linea de transacciones.txt tiene:  ClienteID, Tipo, Monto
# Para ejecutar:  python procesador_transacciones.py


# 1) Leer el archivo y guardar las transacciones en una lista de diccionarios
def leer_y_almacenar_datos(nombre_archivo):
    lista_transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.split(",")   # separar por comas
            transaccion = {
                "cliente_id": partes[0].strip(),
                "tipo": partes[1].strip(),
                "monto": int(partes[2]),  # convertir el monto a numero
            }
            lista_transacciones.append(transaccion)
    return lista_transacciones

# 2) Sumar el monto de todas las transacciones
def calcular_monto_total(lista_transacciones):
    total = 0
    for transaccion in lista_transacciones:
        total = total + transaccion["monto"]
    return total

# 3) Dejar solo las transacciones de un tipo
def filtrar_por_tipo(lista_transacciones, tipo_filtro):
    lista_filtrada = []
    for transaccion in lista_transacciones:
        if transaccion["tipo"] == tipo_filtro:
            lista_filtrada.append(transaccion)
        else:
            pass  # las que no coinciden se ignoran
    return lista_filtrada

# 4) Dar formato de pesos a un numero
def formatear_pesos(valor):
    return "$" + f"{valor:,}"

# 5) Funcion principal que usa todas las demas
def ejecutar_sistema():
    transacciones = leer_y_almacenar_datos("transacciones.txt")

    total = calcular_monto_total(transacciones)
    print("Monto total de las transacciones:",formatear_pesos(total))

    creditos = filtrar_por_tipo(transacciones, "CREDITO")
    print("Transacciones de tipo CREDITO:")
    for transaccion in creditos:
        print(transaccion["cliente_id"], transaccion["tipo"], formatear_pesos(transaccion["monto"]))

# Iniciar el programa
ejecutar_sistema()