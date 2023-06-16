import os #importa el módulo 

agenda1 = {}


def validar_contacto(contacto):
    os.system("cls") #Limpia la terminal con el import os
    while contacto.strip() == "": #el método STRIP ayuda a eliminar los espacios en blanco, valida que no se ingrese un valor vacío 
        print ("No ingresó ningún valor")
        contacto = input("Ingrese nuevamente el nombre por favor").capitalize()
    return contacto
 

def validar_numero(telefono):
    os.system("cls")
    while not telefono.isdigit():#is digit consulta que se ingresen digitos numéricos
        print ("Solo se aceptan números")
        telefono = (input("Ingrese nuevamente el teléfono por favor"))
    return telefono


def consultarcontacto(agenda):
    os.system("cls") #Limpia la terminal con el import os
    contacto = input("Qué nombre quisiera consultar? ").capitalize()
    contacto_validado = validar_contacto(contacto)#Toma el valor ingresado válido
    if contacto_validado in agenda:
        telefono = agenda[contacto_validado] #SE LE ASIGNA LA VARIABLE TELEFONO AL VALUE Y CONTACTO A LA KEY
        print (f"El teléfono de {contacto_validado} es : {telefono}")
    else:
        print (f"El contacto no se encuentra en la agenda")
    opcionsistema()

def agregarcontacto(agenda):
        os.system("cls")
        contacto = input("Qué nombre quisiera agregar?").capitalize()
        contacto_validado = validar_contacto(contacto)#Toma el valor ingresado válido
        if contacto_validado not in agenda:
            telefono = (input(f"Ingrese el número de teléfono del contacto {contacto_validado} "))
            telefono_validado = validar_numero(telefono)
            agenda1[contacto_validado] = telefono_validado #SELE ASIGNA EL VALUE TELEFONO
            print (f"El teléfono del nuevo contacto {contacto_validado} es : {telefono_validado}")
        else:    
            print("El nombre ya se encuentra en la Agenda")
        opcionsistema()

def eliminarcontacto(agenda):
    os.system("cls")
    contacto = input("Qué nombre quisiera eliminar?").capitalize()
    contacto_validado = validar_contacto(contacto)
    if contacto_validado not in agenda:
        print (f"El contacto no se encuentra en la agenda")
    else:
        agenda1.pop(contacto_validado)
        print (f"El contacto {contacto_validado} se eliminó correctamente")
        print ("La nueva lista en la agenda es la siguiente: ")
        print (agenda1)
    opcionsistema()

def todosloscontactos(agenda):
    os.system("cls")
    print ("Esta es la lista de todos los contactos: ")
    for todo in agenda.items():
        print(todo)
    opcionsistema()



def opcionsistema():
    print("""Ingrese la opción que desea realizar:
     [1] Buscar contacto
     [2] Agregar contacto
     [3] Eliminar contacto
     [4] Mostrar todos los contactos
     [5] Salir del programa""")
    
    opciones = input()

    
    match opciones:
        case "1": 
            consultarcontacto(agenda1)
        case "2": 
            agregarcontacto(agenda1)
        case "3": 
            eliminarcontacto(agenda1)
        case "4": 
            todosloscontactos(agenda1)
        case "5":
            print("Gracias por utilizar AGENDA 2023. ¡VUELVA PRONTO!")
        case _ :
            print("""OPCIÓN INCORRECTA.
        Por favor seleccione opcion correcta""")
            opcionsistema()
            


print  ("#"*50)
print  ("            BIENVENIDO A LA AGENDA 2023")
print  ("#"*50)

opcionsistema()