# transaccion_poo_v1.py
# Lee transacciones de un archivo, suma los montos y filtra por tipo CREDITO.
# Cada linea del archivo tiene: ClienteID, Tipo, Monto
# Para ejecutar: python transaccion_poo_v1.py


# 1) Clase: define los datos de una transaccion
class Transaccion:

    # Guarda el cliente, el tipo y el monto de cada transaccion
    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = int(monto)

    # Devuelve la transaccion como texto
    def obtener_informacion(self):
        return f"{self.cliente_id} - {self.tipo} - ${self.monto:,}"


# 2) Lee el archivo y crea una lista de transacciones
def leer_y_almacenar_datos(nombre_archivo):
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() == "":   # salta lineas vacias
                continue
            cliente_id, tipo, monto = linea.strip().split(",")
            if int(monto) > 0:   # solo guarda montos validos
                transaccion = Transaccion(cliente_id.strip(), tipo.strip(), monto)
                transacciones.append(transaccion)
    return transacciones


# 3) Suma el monto de todas las transacciones
def calcular_monto_total(transacciones):
    total = 0
    for transaccion in transacciones:
        total = total + transaccion.monto
    return total


# 4) Deja solo las transacciones de un tipo
def filtrar_por_tipo(transacciones, tipo_filtro):
    lista_filtrada = []
    for transaccion in transacciones:
        if transaccion.tipo == tipo_filtro:
            lista_filtrada.append(transaccion)
    return lista_filtrada


# 5) Da formato de pesos a un numero
def formatear_pesos(valor):
    return "$" + f"{valor:,}"


# 6) Funcion principal: ejecuta todo en orden 
def ejecutar_sistema():
    transacciones = leer_y_almacenar_datos("transacciones.txt")

    print("--- Todas las transacciones ---")
    for transaccion in transacciones:
        print(transaccion.obtener_informacion())

    total = calcular_monto_total(transacciones)
    print("\nMonto total de las transacciones:", formatear_pesos(total))

    print("\n--- Solo CREDITO ---")
    creditos = filtrar_por_tipo(transacciones, "CREDITO")
    for transaccion in creditos:
        print(transaccion.obtener_informacion())


# Iniciar el programa
ejecutar_sistema()
