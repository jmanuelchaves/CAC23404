import os #importa el módulo 

from validaciones import validar_contacto, validar_numero, limpiar_terminal





def consultarcontacto(agenda):
    limpiar_terminal()
    contacto = input("Qué nombre quisiera consultar? ").capitalize()
    contacto_validado = validar_contacto(contacto)#Toma el valor ingresado válido
    if contacto_validado in agenda:
        telefono = agenda[contacto_validado] #SE LE ASIGNA LA VARIABLE TELEFONO AL VALUE Y CONTACTO A LA KEY
        print (f"El teléfono de {contacto_validado} es : {telefono}")
    else:
        print (f"El contacto no se encuentra en la agenda")


def agregarcontacto(agenda):
        limpiar_terminal()
        contacto = input("Qué nombre quisiera agregar?").capitalize()
        contacto_validado = validar_contacto(contacto)#Toma el valor ingresado válido
        if contacto_validado not in agenda:
            telefono = (input(f"Ingrese el número de teléfono del contacto {contacto_validado} "))
            telefono_validado = validar_numero(telefono)
            agenda[contacto_validado] = telefono_validado #SELE ASIGNA EL VALUE TELEFONO
            print (f"El teléfono del nuevo contacto {contacto_validado} es : {telefono_validado}")
        else:    
            print("El nombre ya se encuentra en la Agenda")


def eliminarcontacto(agenda):
    limpiar_terminal()
    contacto = input("Qué nombre quisiera eliminar?").capitalize()
    contacto_validado = validar_contacto(contacto)
    if contacto_validado not in agenda:
        print (f"El contacto no se encuentra en la agenda")
    else:
        agenda.pop(contacto_validado)
        print (f"El contacto {contacto_validado} se eliminó correctamente")
        print ("La nueva lista en la agenda es la siguiente: ")
        print (agenda)


def todosloscontactos(agenda):
    limpiar_terminal()
    print ("Esta es la lista de todos los contactos: ")
    print("Contacto === Teléfono")
    if agenda:
        for contacto,telefono in agenda.items():
            print(f"{contacto} === {telefono}")
    else:
        print("Inventario vacio")
    input("Presione una tecla para continuar..")



def opcionsistema(agenda):
    while True:
        print("""Ingrese la opción que desea realizar:
        [1] Buscar contacto
        [2] Agregar contacto
        [3] Eliminar contacto
        [4] Mostrar todos los contactos
        [5] Salir del programa""")
    
        opciones = input()

    
        match opciones:
            case "1": 
                consultarcontacto(agenda)
            case "2": 
                agregarcontacto(agenda)
            case "3": 
                eliminarcontacto(agenda)
            case "4": 
                todosloscontactos(agenda)
            case "5":
                print("Gracias por utilizar AGENDA 2023. ¡VUELVA PRONTO!")
                break
            case _ :
                print("""OPCIÓN INCORRECTA.
                Por favor seleccione opcion correcta""")