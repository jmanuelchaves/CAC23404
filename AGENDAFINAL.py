import os #importa el módulo 
archivo = open("agenda.txt", "w") #Para que se cree en la misma carpeta hacer click derecho-->"Open with Code"
archivo.close()
from validaciones import validar_contacto, validar_numero, limpiar_terminal
from opcionesmenu import limpiar_terminal, consultarcontacto, agregarcontacto, eliminarcontacto, todosloscontactos, opcionsistema



agenda = {}

print  ("#"*50)
print  ("            BIENVENIDO A LA AGENDA 2023")
print  ("#"*50)

opcionsistema(agenda)
