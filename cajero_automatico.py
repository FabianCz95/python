"""
### Simulador de Cajero Automático
Requisitos:
Operaciones básicas:
- Consultar saldo: Muestra el saldo actual.
- Depositar: Permite agregar una cantidad al saldo.
- Retirar: Permite retirar dinero del saldo, validando que no se exceda el saldo disponible.

Validaciones:
- Evita retirar cantidades mayores al saldo.
- Maneja errores como entradas no numéricas o negativas.

Extras opcionales:
- Registra el historial de transacciones (depositos, retiros, consultas).
- Salida ordenada del programa con confirmación.

Estructura sugerida:
- Variables: saldo para almacenar el saldo actual.
- Funciones: consultar_saldo, depositar, retirar, menu_principal..
"""
import datetime
saldo = 0
movimientos = []

def iniciar_cajero():

    menu = """
    1) Consultar saldo.
    2) Consultar movimientos.
    3) Depositar efectivo.
    4) Retirar efectivo
    0) Salir
        """
    while True :
        try:
            texto = int(input(f"Ingresa el codigo de alguna opción: {menu}"))
            if texto == 1:
                consultar_saldo()
            elif texto == 2:
                consultar_movimientos()
            elif texto == 3:
                realizar_transaccion("Ingrese la cantidad que desea depositar: ", "Deposito")
            elif texto == 4:
                realizar_transaccion("Ingrese la cantidad que desea retirar: ", "Retiro")
            elif texto == 0:
                confirmacion = input("¿Estás seguro de que quieres salir? (S/N): ").lower()
                if confirmacion == "s":
                    print("Gracias por visitarnos!")
                    break
            else :
                print("Seleccione un codigo válido")
        except:
            print("Por favor, ingrese un codigo permitido")

def consultar_saldo():
    global saldo
    print(f"El saldo actual de la cuenta es de: ${saldo:.2f}")

def realizar_transaccion(mensaje,tipo):
    global saldo
    while True :
        try:
            monto = float(input(mensaje))
            if monto <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue

            if tipo == "Deposito":
                saldo += monto
                movimientos.append({"fecha": datetime.datetime.now(), "tipo": tipo, "monto": monto})
                print(f"Se ha depositado ${monto:.2f} en tu cuenta")
            elif tipo == "Retiro":
                if monto > saldo:
                    print("No puedes retirar más del saldo disponible.")
                else:
                    saldo -= monto
                    movimientos.append({"fecha": datetime.datetime.now(), "tipo": tipo, "monto": -monto})
                    print(f"Se ha retirado ${monto:.2f} de tu cuenta")
            break
        except:
            print("Por favor, ingrese una cantidad válida.")

def consultar_movimientos():
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        print("Historial de movimientos:") 
        for mov in movimientos :
            print(f"{mov["fecha"]} - {mov["tipo"]} - ${mov["monto"]:.2f}")
        return
    
iniciar_cajero()

