import os
import json
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
        if proyectos["Estado"] == "Finalizados":
            proyectos_cancelados.append(proyectos)

    with open(PATH_json, "w", encoding="utf-8") as archivo:
        json.dump(proyectos_cancelados, archivo, ensure_ascii=False, indent=4)

    return True