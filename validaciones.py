import os #importa el módulo 

def limpiar_terminal():
    """Limpia la terminal según el sistema operativo"""
    if  os.name == "nt":  # Comprobar si el sistema operativo es Windows
        os.system("cls")
    else:  # Para sistemas basados en Unix (Linux, macOS)
        os.system("clear")

def validar_contacto(contacto):
    limpiar_terminal()
    while contacto.strip() == "": #el método STRIP ayuda a eliminar los espacios en blanco, valida que no se ingrese un valor vacío 
        print ("No ingresó ningún valor")
        contacto = input("Ingrese nuevamente el nombre por favor").capitalize()
    return contacto
 

def validar_numero(telefono):
    limpiar_terminal()
    while not telefono.isdigit():#is digit consulta que se ingresen digitos numéricos
        print ("Solo se aceptan números")
        telefono = (input("Ingrese nuevamente el teléfono por favor"))
    return telefono
