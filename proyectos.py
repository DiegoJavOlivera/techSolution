from validaciones import *
from constantes import *

def crear_proyecto():
    fecha_inicio, fecha_fin = ingresar_fechas_proyecto()
    diccionario = {}
    diccionario["id"] = validar_id(LISTA_PROYECTOS)
    diccionario["Nombre del Proyecto"] = validar_ingreso_nombre_proyecto_descripcion("el nombre del proyecto", 30).capitalize()
    diccionario["Descripción"] = validar_ingreso_nombre_proyecto_descripcion("la descripcion del proyecto", 200).capitalize()
    diccionario["Fecha de inicio"] = fecha_inicio
    diccionario["Fecha de Fin"] = fecha_fin
    diccionario["Presupuesto"] = validar_presupuesto()
    diccionario["Estado"] = "Activo"
    LISTA_PROYECTOS.append(diccionario)
    
    return True 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------