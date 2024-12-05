# Variables
# nombre = "Fabian"
# edad = 10
# altura = 1.91
# esEstudiante = True

# if edad >= 18:
#     print("Es mayor de edad!")
# else:
#     print("No es mayor de edad :'(")

# for i in range(edad):
#     print(i)
#     i += 1

# contador = 10
# while contador > 0:
#     print(contador)
#     contador -= 1

# frutas = [1,2,3,4,5]

# alumno = {
#     "nombre": nombre,
#     "edad": edad,
#     "altura": altura,
#     "esEstudiante": esEstudiante
# }

# def multi(a,b):
#     return print(a * b)

# multi(15,2)


## Ejercicio 1: Calculadora de Promedios ###
calificaciones = []

def calculador_promedios(calificaciones) :  
    promedio = sum(calificaciones)/len(calificaciones)
    estado = "Aprobado" if promedio > 6 else "Reprobado"
    print(f"Estado: {estado}, calificación:  {promedio}")

for i in range(5):
    calificacion = int(input("Ingresa la calificación del alumno " + str(i) + "\n"))
    calificaciones.append(calificacion)

calculador_promedios(calificaciones)

## Ejercicio 2: Inventario de Tienda ###
inventario = {}
def agregar_producto(nombre, cantidad, precio):
    if cantidad > 0 and precio > 0 :
        inventario[nombre] = {
            "cantidad": int(cantidad),
            "precio": float(precio)
        }
    else:
        print("La cantidad y/o precio son menores que 0")


def mostrar_inventario(diccionario) :
    if not diccionario :
        print("El inventario esta vacío")
        return

    for nombre,datos in diccionario.items() :
        print(f"{nombre}: Cantidad = {datos['cantidad']}, Precio = {datos['precio']:.2f}")
    total_inventario(inventario)

def total_inventario(diccionario) :
    total = 0
    for i in diccionario.values():
        total += i["cantidad"] * i["precio"]
    print(f'Valor total del inventario: ${total}') 
    
agregar_producto('celular', 1, 10.2)
agregar_producto('cafe', 4, 4.3)
agregar_producto('tablet', 2, 8.8)

mostrar_inventario(inventario)

## Ejercicio 3: Contador de Palabras
"""
Escribe una función llamada contar_palabras que tome una cadena de texto y devuelva un diccionario con la frecuencia de cada palabra.

Usa el método split() para dividir la cadena en palabras.
Usa un diccionario para contar las ocurrencias de cada palabra.
Prueba la función con una oración como: "python es genial y python es divertido".
"""
import string
texto_con_palabras = "python es genial y python es divertido"

def contar_palabras(texto) :
    palabras = texto.lower().translate(str.maketrans("","",string.punctuation)).split()
    diccionario = {}
    for palabra in palabras :
        diccionario[palabra] = diccionario.get(palabra, 0) +1    
    return diccionario
        
resultado = contar_palabras(texto_con_palabras)
print(resultado)

"""
### Ejercicio 4: Números Primos en un Rango
Escribe una función llamada encontrar_primos 
    que reciba dos números, inicio y fin, 
    y devuelva una lista de todos los números primos en ese rango 
    (incluyendo inicio y fin si son primos).
    

Un número es primo si solo es divisible por 1 y por sí mismo.
Usa un bucle for para iterar entre inicio y fin, y otro bucle anidado o una condición para verificar si cada número es primo.
Prueba la función con un rango de 10 a 50 y muestra el resultado.
"""
def encontrar_primos(inicio, fin):
    inicio, fin = min(inicio, fin), max(inicio, fin)
    numeros_primos = []

    for num in range(inicio, fin + 1) :
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            numeros_primos.append(num)
    return numeros_primos

print(encontrar_primos(10, 50))

"""
### Ejercicio 5: Gestión de Estudiantes
Crea un programa que permita gestionar estudiantes y sus calificaciones.

Crea un diccionario llamado estudiantes, 
    donde cada clave sea el nombre de un estudiante y 
    su valor sea una lista de calificaciones.
Escribe una función agregar_calificacion que reciba el nombre del estudiante y una calificación, y la añada a su lista de calificaciones.
Escribe una función promedio_estudiante que reciba el nombre de un estudiante y calcule su promedio de calificaciones.
Escribe una función promedio_general que calcule el promedio de todos los estudiantes.
Prueba el programa agregando estudiantes, asignando calificaciones y calculando los promedios.
"""
estudiantes = {}

def agregar_calificacion(nombre,calificacion) :
    if nombre not in estudiantes :
        estudiantes[nombre] = []
    estudiantes[nombre].append(calificacion)
    return

def promedio_estudiante(nombre) :
    if nombre in estudiantes :
        promedio = sum(estudiantes[nombre])/len(estudiantes[nombre])
        print(f"El promedio de {nombre} es {promedio}")
        return promedio
    else :
        print(f"El alumno no existe en la base de datos")
        return None

def promedio_general(diccionario) :
    promedio_general = 0
    for x in diccionario.keys() :
        promedio_general += promedio_estudiante(x)
    promedio_general = promedio_general/len(diccionario)
    print(f"El promedio general de todo el alumnado es de {promedio_general}")
    return promedio_general

agregar_calificacion("fabian",9)
agregar_calificacion("fabian",8)
agregar_calificacion("fabian",10)
agregar_calificacion("eliza",10)
agregar_calificacion("eliza",10)
agregar_calificacion("eliza",10)
promedio_general(estudiantes)

"""
### Ejercicio 6: Conversor de Unidades
Escribe un programa que convierta entre unidades de medida (metros, kilómetros, centímetros).

Define un diccionario con factores de conversión (por ejemplo, 1 metro a kilómetros es 0.001, a centímetros es 100, etc.).
Crea una función convertir_unidad que tome tres parámetros: la cantidad, la unidad original y la unidad deseada, y devuelva la cantidad convertida.
Usa un bucle para permitir al usuario hacer varias conversiones hasta que decida salir.
"""
factores_conversion = {
    "kilometros": {
        "kilometros": 1,
        "metros": 1000,
        "centimetros": 100000
    },
    "metros": {
        "kilometros": 0.001,
        "metros": 1,
        "centimetros": 100
    },
    "centimetros": {
        "kilometros": 0.00001,
        "metros": 0.01,
        "centimetros": 1
    }
}

def codificador(num):
    return {
        "1": "kilometros",
        "2": "metros",
        "3": "centimetros",
        "9": True,
        "0": False
    }.get(num)

def convertir_unidad(cantidad,unidad_original,unidad_deseada):
    new_cant = cantidad * factores_conversion[unidad_original][unidad_deseada]
    print(f"Los {cantidad, unidad_original} se convierten a {new_cant, unidad_deseada}")
    return new_cant
        

def conversion_unidades() :
    continuar = True
    opciones =  """
    1) Kilometros.
    2) Metros.
    3) Centimetros.
    """
    salir = """
    9) Continuar
    0) Salir
    """

    while continuar :
        cant = int(input(f"Defina la cantidad que desea convertir: "))
        unit_original = codificador(input(f"Ingrese el codigo del tipo de unidad que desea convertir{opciones}"))
        unit_deseada = codificador(input(f"Ingrese el codigo del tipo de unidad a la que desea convertir{opciones}"))

        if unit_original in factores_conversion and unit_deseada in factores_conversion[unit_original] :
            convertir_unidad(cant,unit_original, unit_deseada) 
        else :
            print("Los codigos no fueron definidos correctamente")
        continuar = codificador(input(f"Desea realizar otra conversión: {salir}"))


conversion_unidades()

"""
### Ejercicio 7: Sistema de Tienda Virtual Simplificada
Crea una función registrar_producto para añadir productos a un catálogo de tienda con nombre, precio y stock.
Define una función agregar_al_carrito que permita al usuario añadir productos al carrito si hay suficiente stock disponible.
Crea una función finalizar_compra que calcule el total de los productos en el carrito, reste el stock comprado del inventario y vacíe el carrito al finalizar.
Prueba el sistema simulando una compra de dos o más productos.
"""
catalogo = {}
carrito = {}

def registrar_producto(nombre,precio,stock) :
    if nombre not in catalogo :
        catalogo[nombre] = {
            "precio" : 0.00,
            "stock" : 0
        }
    catalogo[nombre]["precio"] = precio
    catalogo[nombre]["stock"] += stock
    

registrar_producto("celular",1000,5)
registrar_producto("celular",1000,5)
registrar_producto("ps5",5000,3)
registrar_producto("impresora",300,5)

# Define una función agregar_al_carrito que permita al usuario añadir productos al carrito si hay suficiente stock disponible.
def agregar_al_carrito(nombre, cant) :
    if nombre in catalogo :
        if catalogo[nombre]["stock"] < cant :
            return print("No hay stock suficiente")
            
        if nombre in carrito and carrito[nombre]["precio"] == catalogo[nombre]["precio"] :
            carrito[nombre]["cant"] += cant
            return
        else :
            carrito[nombre] = {
                "precio" : catalogo[nombre]["precio"],
                "cant" : cant
            }
            return
    else :
        return print("El articulo no existe en el catalogo")

agregar_al_carrito("celular",1)
agregar_al_carrito("celular",2)
agregar_al_carrito("ps5",1)
agregar_al_carrito("impresora",3)

# Crea una función finalizar_compra que calcule el total de los productos en el carrito, 
# reste el stock comprado del inventario y vacíe el carrito al finalizar.

def finalizar_compra(dicc) :
    total = 0
    for articulo in dicc :
        total += dicc[articulo]["precio"] * dicc[articulo]["cant"]
        catalogo[articulo]["stock"] -= dicc[articulo]["cant"]
    
    print(f"El total de los productos es de: {total}")
    dicc.clear()

finalizar_compra(carrito)
