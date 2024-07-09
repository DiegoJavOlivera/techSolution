import os
import json
from validaciones import *
from constantes import *

def parseo_csv(path_csv):
    """Esta funcion parsea el csv y crea una lista de diccionarios para ser utilizado en el programa

    Args:
        path_csv (str): Recibe una ruta donde se encuentra el csv que tiene que leer
    """
    if os.path.exists(path_csv):
        with open(path_csv, "r",encoding="utf-8") as archivo:
            encabezado = archivo.readline().strip().split(",")
            for fila in archivo:
                valores = fila.strip().split(",")
                diccionario = {}
                for i, valor_encabezado in enumerate(encabezado):
                    diccionario[valor_encabezado] = valores[i]
                LISTA_PROYECTOS.append(diccionario)
        return LISTA_PROYECTOS

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def parsear_lista_csv(lista_proyectos: list[dict]):
    """Esta función convierte una lista de diccionarios de proyectos a un archivo CSV.

    Args:
        lista_proyectos (list[dict]): Lista de diccionarios con proyectos.

    Return:
        None: Retorna None para verificar.
    """
    PATH_csv = "./data/proyectos.csv"
    with open(PATH_csv, "w", encoding="utf-8") as archivo:
        encabezados = list(lista_proyectos[0].keys())
        archivo.write(",".join(encabezados) + "\n")
        for proyecto in lista_proyectos:
            valores = []
            for val in encabezados:
                valores.append(str(proyecto[val]))
            archivo.write(",".join(valores) + "\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def parsear_json_lista():
    """Esta función lee un archivo JSON que contiene proyectos finalizados y 
    los añade a la lista global LISTA_PROYECTOS.

    Returns:
        bool: Retorna True para verificar que la operación se realizó con éxito.
    """
    PATH_json = "./data/Proyectos_finalizados.json"

    with open(PATH_json, "r", encoding="utf-8") as archivo:
        proyectos_finalizados = json.load(archivo)
        LISTA_PROYECTOS.append(proyectos_finalizados)
    return True

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def parsear_lista_json(lista_proyectos: list[dict]):
    """Esta función convierte una lista de diccionarios de proyectos a un archivo JSON.

    Args:
        lista_proyectos (list[dict]): Lista de diccionarios con proyectos.

    Return:
        bool: Retorna True para verificar.
    """
    PATH_json = "./data/Proyectos_finalizados.json"
    proyectos_cancelados = []
    for proyectos in lista_proyectos:
        if proyectos["Estado"] == "Finalizado":
            proyectos_cancelados.append(proyectos)

    with open(PATH_json, "w", encoding="utf-8") as archivo:
        json.dump(proyectos_cancelados, archivo, ensure_ascii=False, indent=4)

    return True

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def leer_numero_reporte(path_txt: str) -> int:
    """Lee el número de reporte desde un archivo.

    Args:
        path_txt (str): La ruta del archivo que contiene el número de reporte.

    Returns:
        elementos_reportes(int): El número de reporte leído del archivo. Si no existe, retorna 1.
    """
    if os.path.exists(path_txt):
        with open(path_txt, "r", encoding="utf-8") as archivo:
            numero_reporte = int(archivo.read().strip())
        return numero_reporte
    else:
        return 1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def escribir_numero_reporte(path_txt: str, numero_reporte: int):
    """Escribe el número de reporte en un archivo.

    Args:
        path_txt (str): La ruta del archivo donde se escribirá el número de reporte.
        numero_reporte (int): El número de reporte a escribir.
    """
    with open(path_txt, "w", encoding="utf-8") as archivo:
        archivo.write(str(numero_reporte))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def generar_reporte_presupuesto(lista_proyectos: list[dict]):
    """Genera un reporte de proyectos cuyo presupuesto supera un límite especificado.
    
    Args:
        lista_proyectos (list[dict]): Lista de diccionarios que contienen información de los proyectos.
    
    El reporte incluye:
    - Fecha de solicitud del reporte.
    - Cantidad de proyectos que superan el presupuesto límite.
    - Listado detallado de los proyectos que superan el presupuesto.

    El número de reporte se guarda en un archivo de texto para que sea incremental en cada ejecución del programa.
    """
    path_numero_reporte = "data/informes_presupuesto/contador_reportes/numero_reporte_presupuesto.txt"
    numero_reporte = leer_numero_reporte(path_numero_reporte)
    presupuesto_limite = int(input("Ingrese el presupuesto límite: "))

    fecha_solicitud = obtener_fecha_actual()

    presupuestos_mayores = []
    for proyecto in lista_proyectos:
        if proyecto["Presupuesto"] > presupuesto_limite:
            presupuestos_mayores.append(proyecto)
    if presupuestos_mayores:
        cantidad_presupuestos_mayores = len(presupuestos_mayores)
        os.makedirs("data/informes_presupuesto/", exist_ok=True)
        nombre_archivo = f"data/informes_presupuesto/reporte_de_Presupuesto#{numero_reporte}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Reporte #{numero_reporte}\n")
            archivo.write(f"Fecha de solicitud: {fecha_solicitud}\n")
            archivo.write(f"Cantidad de proyectos que superan el presupuesto: {cantidad_presupuestos_mayores}\n\n")
            archivo.write("Listado de proyectos que superan el presupuesto:\n")
            for proyecto in presupuestos_mayores:
                archivo.write(f"ID: {proyecto["id"]}, Nombre: {proyecto["Nombre del Proyecto"]}, Presupuesto: {proyecto["Presupuesto"]}\n")
        
        print(f"SE HA GENERADO EL REPORTE NUMERO #{numero_reporte} CON EXITO. SE HAN ENCONTRADO {cantidad_presupuestos_mayores} PROYECTOS QUE SUPERAN EL PRESUPUESTO.")
        
        numero_reporte += 1
        escribir_numero_reporte(path_numero_reporte, numero_reporte)
    else:
        print("NO SE ENCONTRARON PROYECTOS QUE SUPEREN EL PRESUPUESTO.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def generar_reporte_proyecto(lista_proyectos:list[dict]):
    path_reporte_proyecto = "data/informes_proyectos/contador_proyectos/numero_reporte_proyecto.txt"
    numero_reporte_proyecto = leer_numero_reporte(path_reporte_proyecto)

    fecha_solicitud = obtener_fecha_actual()
    
    obtener_nombre_proyecto = buscar_proyecto_por_nombre("Ingrese el nombre del proyecto que desea para generar un reporte, respetando sus acentos: ")
    obtener_proyecto = buscar_proyecto_id_str(obtener_nombre_proyecto,lista_proyectos,"Nombre del Proyecto")

    if isinstance(obtener_proyecto, dict):
        proyectos_mayores = []
        for proyecto in lista_proyectos:
            if proyecto["Presupuesto"] > obtener_proyecto["Presupuesto"]:
                proyectos_mayores.append(proyecto)
            
        cantidad_presupuestos_mayores = len(proyectos_mayores)

        os.makedirs("data/informes_proyectos",exist_ok=True)
        nombre_archivo = f"data/informes_proyectos/reporte_de_Proyecto#{numero_reporte_proyecto}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Reporte #{numero_reporte_proyecto}\n")
            archivo.write(f"Fecha de solicitud: {fecha_solicitud}\n")
            archivo.write("Datos del proyecto buscado: \n")
            archivo.write(f"ID: {obtener_proyecto["id"]}, Nombre: {obtener_proyecto["Nombre del Proyecto"]}, Presupuesto: {obtener_proyecto["Presupuesto"]}\n")
            if proyectos_mayores:
                archivo.write("--------------------------------------------------------------------------------------------------------------------------------------------------\n")
                archivo.write("Archivos con presupuesto superiores al buscado:\n\n")
                for iterarador_proyectos in proyectos_mayores:
                    archivo.write(f"ID: {iterarador_proyectos["id"]}, Nombre: {iterarador_proyectos["Nombre del Proyecto"]}, Presupuesto: {iterarador_proyectos["Presupuesto"]}\n")

        print(f"SE HA GENERADO EL REPORTE NUMERO #{numero_reporte_proyecto} CON EXITO. SE HAN ENCONTRADO {cantidad_presupuestos_mayores} PROYECTOS QUE SUPERAN EL PRESUPUESTO BUSCADO POR NOMBRE.\n")

        numero_reporte_proyecto += 1
        escribir_numero_reporte(path_reporte_proyecto,numero_reporte_proyecto)
    else:
        print("NO SE ENCONTRO EL PROYECTO, VUELVA A INTENTARLO\n")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------