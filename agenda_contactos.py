"""
2. Agenda de Contactos
Requisitos:
Gestión de contactos:
    Crear un contacto con nombre, teléfono y correo.
    Editar contactos existentes (buscar por nombre y actualizar datos).
    Eliminar contactos por nombre.
Buscar contactos:
    Permite buscar por nombre y muestra los detalles del contacto.
Persistencia:
    Guarda y carga los contactos desde un archivo (por ejemplo, en formato JSON o CSV).
Extras opcionales:
    Ordenar contactos al mostrarlos (por nombre).
    Validar formatos (por ejemplo, correos electrónicos o números de teléfono).
Estructura sugerida:
    Diccionario contactos para almacenar los datos (clave: nombre, valor: datos del contacto).
    Funciones: crear_contacto, editar_contacto, eliminar_contacto, buscar_contacto, guardar_contactos, cargar_contactos.
"""

def crear_contacto():
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el numero teléfonico: ")
    corre = input("Ingresa un correo Electronico")