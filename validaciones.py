import sys
import os
from datetime import datetime
from constantes import *
from prettytable import *


def limpiar_consola():
    """Esta funcion limpia la consola
    """
    os.system("cls")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def finalizar_programa():
    """Esta funcion finaliza el programa
    """
    print("programa finalizado")
    sys.exit()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_ingreso_nombre_proyecto_descripcion(nombre_descripcion: str, limite_caracter: int):
    """Esta funcion valida el ingreso del nombre del proyecto, que no contenga numeros ni puntos 

    Args:
        nombre_descripcion (str): Este argumento es el texto de lo que se quiera ingresar
        limite_caracter (int): Limite de caracteres, limite para lo que se quiere usar

    Returns:
        identificacion_proyecto_descripcion (str): en caso de ingresar bien el nombre, retorna el nombre 
    """
    identificacion_proyecto_descripcion = input(f"Ingrese {nombre_descripcion}: ")
    longitud_identificacion_proyecto_descripcion = len(identificacion_proyecto_descripcion)
    
    while not identificacion_proyecto_descripcion.replace(" ","").isalpha()  or longitud_identificacion_proyecto_descripcion > limite_caracter:
        print(f"Verificar que lo que se ingreso sea solo alfabetico y sea menor a {limite_caracter} caracteres")
        identificacion_proyecto_descripcion = input(f"Ingrese nuevamente {nombre_descripcion}: ")
        longitud_identificacion_proyecto_descripcion = len(identificacion_proyecto_descripcion)
    
    return identificacion_proyecto_descripcion

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_nombre(mensaje_nombre:str, cantidad_caracteres:int):
    """Esta funcion valida que el nombre ingresado sea no superior a la cantidad de caracteres que se quiera

    Args:
        mensaje_nombre (str): El mensaje puede ser el que se quiera para ingresar un nombre
        cantidad_caracteres (int): Cantidad en entera de caracteres que se quiera para el largo del nombre no lo supere

    Returns:
        descripcion_proyecto: En esta funcion si o si tiene que retornar un nombre de un proyecto bien ingresado
    """             
    while True:
        nombre_proyecto = input(mensaje_nombre)
        if nombre_proyecto.replace(" ","").isalpha() and len(nombre_proyecto) < cantidad_caracteres:
            return nombre_proyecto
        else:
            print("El nombre no debe contener numeros, intentelo nuevamente")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_descripcion(mensaje_descripcion:str,cantidad_caracteres:int):
    """Esta funcion valida que la descripcion del proyecto sea str y no mayor a la cantidad de caracteres que se desee

    Args:
        mensaje_nombre (str): Nombre de mensaje que se desee
        cantidad_caracteres (int): Cantidad de caracteres que se quiera que tenga la descripcion para que no lo supere

    Returns:
        descripcion_proyecto: Retorna si o si una descripcion de proyecto
    """
    while True:
        descripcion_proyecto = input(mensaje_descripcion)
        if descripcion_proyecto.replace(" ","") and len(descripcion_proyecto) < cantidad_caracteres:
            return descripcion_proyecto
        else:
            print("La descripcion del proyecto no debe contener ser mas de 200 caracteres, intentelo nuevamente")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def ingresar_opcion(mensaje:str):
    opcion = input(mensaje)
    if opcion.isnumeric() and '.' not in opcion and type(int(opcion)) == int:
        return int(opcion)
        
    else:
        return -1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_entero(numero: str):
    """Esta funcion valida si el numero ingresado es un entero o no

    Args:
        numero (str): El valor ingresado por argumento que debe ser entero asi retorna True, caso contrario manda un False

    Returns:
        Bool: Retorna numero en caso de ser True, False en caso contrarios
    """
    if   type(int(numero)) == int:
        return numero
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def ingresar_fechas_proyecto():
    """Esta funcion solicita 2 fechas , una de inicio y otra de fin de proyecto para luego compararlas
    y retornarlas convertidas de class a str

    Returns:
        tuple : una tupla con Fechas en formato str para que sean desempaquetadas para usarse o guarse como tupla
    """
    while True:
        fecha_inicio = ingresar_fecha("Ingrese la fecha de inicio del proyecto (Dia-Mes-YYYY:  ")
        fecha_fin= ingresar_fecha("Ingrese la fecha de finalizacion del proyecto (Dia/Mes/YYYY: ")

        if fecha_inicio < fecha_fin:
            return (fecha_inicio.strftime("%d-%m-%Y"), fecha_fin.strftime("%d-%m-%Y"))
        else:
            print("Error. La fecha de inicio no puede ser mayor o igual que la fecha de finalizacion, intente nuevamente")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def ingresar_fecha(mensaje_fecha:str):
    """Esta funcion le permite al usuario ingresar una fecha, si corresponde al formato dd-mm-YYYY esta bien, si esta mal ingresado se lo pedira nuevamente
        dia de 1 a 31, mes de 1 a 12 , año de 1980 a 2050   el rango 01-01-1980 || 31-12-2050
        tiene 2 opciones para ingresarla sino debe ingresar todas denuevo 
    Args:
        mensaje_fecha (str): mensaje para indicar como debe ingresar la fecha

    Returns:
        class: Retorna un objeto datatime 
    """
    while True:
        print(mensaje_fecha)
        dia = input("Ingresa el dia: ")
        if int(dia) < 1 or int(dia) > 31 and dia.isnumeric():
            dia = input("Error, debe ser de 1 a 31, Ingresa nuevamente el dia: ")
        mes = input("Ingresa el mes: ")
        if int(mes) < 1 or int(mes) > 12 and mes.isnumeric():
            mes = input("Error, debe ser de mes 1 a 12, Ingrese nuevamente el mes: ")
        anio = input("Ingresa el año en formato YYYY: ")
        if int(anio) < 1980 or int(anio) > 2050 and anio.isnumeric():
            anio = ("Error, debe ser de 4 digitos entre 1980 y 2050 ni mas ni menos, intente nuevamente: ")
        fecha_str = f"{dia}-" + f"{mes}-" + f"{anio}"
        try:
            fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
            return fecha
        except ValueError:
            print("Fecha invalida, asegurese de ingresar la fecha en el formato de: dia/mes/año(2000)")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def cambiar_estado(lista_proyecto:list[dict]):
    """Esta función permite al usuario seleccionar y modificar el estado de un proyecto.

    La función solicita al usuario ingresar un estado válido entre "Activo", "Cancelado" o "Finalizado".
    Si el estado ingresado no es válido, solicita al usuario ingresar nuevamente.

    Returns:
        str: El estado ingresado por el usuario en formato capitalizado ("Activo", "Cancelado" o "Finalizado").
    """
    estado = ["Activo", "Cancelado", "Finalizado"]
    ingreso_estado = input("Ingrese el estado que desea modificar, puede seleccionar entre Activo, Cancelado, Finalizado: ").capitalize()
    
    while ingreso_estado not in estado:
        ingreso_estado = input("Error: El estado ingresado no existe. Ingrese el estado nuevamente, puede seleccionar entre Activo, Cancelado, Finalizado: ").capitalize()
    if ingreso_estado == "Activo":
        cantidad_maxima_proyectos_activos = verificar_cantidad_proyectos(lista_proyecto)
        if cantidad_maxima_proyectos_activos == True:
            return ingreso_estado
        else:
            return False
    return ingreso_estado

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_id(proyectos: list[dict]):
    """Esta función busca el ID más grande dentro de una lista de diccionarios para ingresar uno nuevo y sumarle +1 al mismo.

    Args:
        proyectos (list[dict]): Lista de diccionarios.

    Returns:
        int: Retorna el ID máximo encontrado sumándole +1.
    """
    if len(proyectos) == 0:
        return 1
    else:
        id_maximo = 0
        for proyecto in proyectos:
            if id_maximo == 0:
                id_maximo = proyecto["id"]
            else:
                if id_maximo < proyecto["id"]:
                    id_maximo = proyecto["id"]

    return id_maximo + 1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_cantidad_proyectos(lista_proyectos:list[dict]):
    contador_proyectos = 0
    for empleados in lista_proyectos:
        contador_proyectos = contador_proyectos + 1

    if contador_proyectos < 50:
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscar_proyecto_por_nombre(mensaje):
    """
    Esta función solicita al usuario ingresar el nombre de un proyecto mediante un mensaje proporcionado.

    Args:
        mensaje (str): El mensaje que se le mostrará al usuario para que ingrese el nombre del proyecto.

    Returns:
        str: El nombre del proyecto ingresado por el usuario.
    """
    ingresar_nombre_proyecto = input(mensaje)
    return ingresar_nombre_proyecto

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscar_proyecto_id_str(valor: int | str, lista_proyectos: list[dict], key: str):
    """Esta función busca un valor en la lista de diccionarios para poder retornar el diccionario con el mismo.

    Args:
        valor (int | str): Valor del proyecto que intenta buscar, tanto como activo, cancelado o finalizado, puede ser un id tambien.
        lista_proyectos (list[dict]): Lista de diccionarios.
        key (str): La clave en el diccionario a buscar.

    Returns:
        dict | None: Retorna el diccionario encontrado con el mismo valor del que se le está buscando, o None si no se encuentra.
    """
    lista_repetidos = []
    for proyecto in lista_proyectos:
        if str(proyecto.get(key)) == str(valor):
            lista_repetidos.append(proyecto)
    if len(lista_repetidos) == 1:
        return lista_repetidos[0]
    elif len(lista_repetidos) == 0:
        return None
    else:
        imprimir_todos_proyectos(lista_repetidos)
        buscar_por_id = buscar_proyecto_por_nombre("Hay mas de un proyecto con el mismo nombre, indique por id el que esta buscando: ")
        buscar_id = buscar_proyecto_id_str(buscar_por_id,lista_repetidos,"id")
        return buscar_id

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_presupuesto():
    """Esta funcion valida el presupuesto ingresado llamando a una funcion Validar_entero para validar que sea un numero entero y verifica que el presupuesto no sea menor a $500.000 sin comas ni puntos, es un ejemplo

    Returns:
        int :  Retorna el presupuesto ingresado pero pasado a entero
    """

    ingreso_presupuesto = input("Ingrese el presupuesto: (no menor a $500000 y sin comas ni signos): ")
    validar_presupuesto = validar_entero(ingreso_presupuesto)
    while validar_presupuesto == False or int(ingreso_presupuesto) < 500000 :        
        ingreso_presupuesto = input("Error, Ingrese el presupuesto nuevamente: (no menor a $500000 y sin comas ni signos):  ")
        validar_presupuesto = validar_entero(ingreso_presupuesto)
        
    return int(ingreso_presupuesto)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def modificar_proyecto(key:int|str, proyecto:dict, valor:str,):
    """Esta funcion modifica un valor del proyecto recibido en diccionario

    Args:
        key (str): La key que se recibe debe ser string para identificar lo que se quiere modificar
        proyecto (dict): el diccionario se recibe de otra funcion que es -buscar proyecto ya que retorna un diccionario o un valor bool
        valor (int | str): El valor es ingresado en teclado por el usuario y se utiliza en este caso para cargar el nuevo valor 

    Returns:
        bool: retorna flag_modificado que es un bool si se realiza un cambio vuelve como true sino en su valor predeterminado que es el false
    """
    flag_modificado = False
    if proyecto:
        if key in proyecto:
            proyecto[key] = valor
            flag_modificado = True
        else:
            print(f"Clave '{key}' no encontrada en el proyecto.")
    else:
        print("El proyecto no existe.")
    
    return flag_modificado

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def cancelar_proyecto(lista_proyecto:list[dict]):
    """Esta funcion busca un diccionario con un id, al encontrarlo modifica su estado a cancelado

    Returns:
        Bool: Retorna un bool si lo encontro retorna True caso contrario False
    """
    id_proyecto_cancelar = input("Ingrese el id del proyecto que desea cancelar: ")
    validar_id_proyecto = validar_entero(id_proyecto_cancelar)
    if validar_id_proyecto:
        buscar_proyecto = buscar_proyecto_id_str(id_proyecto_cancelar,lista_proyecto,"id")
        if buscar_proyecto:
            buscar_proyecto["Estado"] = "Cancelado"
            return True
        else:
            return False


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def parsear_fecha_datetime(lista: list[dict], fecha_inicio_fin:str):
    """Esta función parsea la fecha guardada en el diccionario a una fecha de clase datetime.

    Args:
        lista (list[dict]): Recibe la lista de diccionarios.

    Returns:
        list[dict]: Retorna una lista con la fecha de fin transformada a clase datetime para poder ser comparada.
    """
    for diccionario in lista:
        fecha_fin = diccionario[fecha_inicio_fin]
        fecha_fin_datetime = datetime.strptime(fecha_fin, "%d-%m-%Y")
        diccionario[fecha_inicio_fin] = fecha_fin_datetime
    return lista

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def ordenar_fechas(lista_proyectos:list[dict],tipo_orden:bool):
    lista_fecha_datetime = parsear_fecha_datetime(lista_proyectos, "Fecha de inicio")
    ordenar_mayor_menor = ordenar_lista_diccionarios(lista_fecha_datetime,tipo_orden,"Fecha de inicio")
    lista_fecha_strtime = parsear_fecha_datetime_str(ordenar_mayor_menor,"Fecha de inicio")
    return lista_fecha_strtime
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def parsear_fecha_datetime_str(lista_proyectos: list[dict],fecha_inicio_fin:str):
    """Esta función vuelve a parsear la fecha de clase datetime a str.

    Args:
        lista_proyectos (list[dict]): Lista recibida por la función parsear_fecha_datetime.

    Returns:
        list[dict]: Retorna la lista con los valores de fecha de fin convertidos a str.
    """
    for proyecto in lista_proyectos:
        fecha_fin = proyecto[fecha_inicio_fin]
        fecha_fin_str = fecha_fin.strftime("%d-%m-%Y")
        proyecto[fecha_inicio_fin] = fecha_fin_str
    return lista_proyectos

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def validar_fecha_actual_superior(lista_proyectos: list[dict]):
    """Esta función funciona como el entorno donde se ejecutan las otras funciones
    parsear_fecha_datetime_str y parsear_fecha_datetime para poder verificar si los proyectos
    están vencidos y pasarlos a finalizados. Se compara con un .date() porque la fecha guardada es un objeto datetime
    y today .date es otro formato. Se utiliza eso para poder compararlos.

    Args:
        lista_proyectos (list[dict]): Lista que se encuentra en la base de datos.

    Returns:
        list[dict]: Lista con los estados modificados porque se cumplieron los plazos y están vencidos.
    """
    fecha_hoy = datetime.today().date()
    fechas_lista_datetime = parsear_fecha_datetime(lista_proyectos,"Fecha de Fin")
    for proyecto in fechas_lista_datetime:
        if proyecto["Fecha de Fin"].date() < fecha_hoy:
            proyecto["Estado"] = "Finalizado"
    lista_proyectos = parsear_fecha_datetime_str(fechas_lista_datetime,"Fecha de Fin")
    return lista_proyectos


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def imprimir_proyecto(proyecto_dict:dict):
    """Esta funcion muestra un proyecto en la consola recibido en la consola como un diccionario

    Args:
        proyecto_dict (dict): diccionario de proyecto con sus llaves y valores 
    """
    tabla = PrettyTable()
    encabezado = list(proyecto_dict.keys())
    valores = list(proyecto_dict.values())
    tabla.field_names = encabezado
    tabla.add_row(valores)
    print(tabla)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def imprimir_todos_proyectos(lista_proyectos: list[dict]):
    """Esta función imprime todos los proyectos por consola utilizando una librería llamada PrettyTable.

    Args:
        lista_proyectos (list[dict]): Recibe como argumento una lista de diccionarios.
    """

    tabla = PrettyTable()
    encabezado = list(lista_proyectos[0].keys())
    tabla.field_names = encabezado
    for proyecto in lista_proyectos:
        valores = list(proyecto.values())
        tabla.add_row(valores)

    print(tabla)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def normalizar_datos(lista_proyectos: list[dict]):
    """Esta función normaliza los datos de id y presupuestos. Cuando son cargados a las listas
    ingresan como str, esto los convierte a enteros para poder ser utilizados.

    Args:
        lista_proyectos (list[dict]): Lista donde se encuentran cargados los datos.

    Returns:
        bool: Retorna un bool True si se normalizó algún dato, False en caso contrario.
    """
    flag_dato_modificado = False
    for proyecto in lista_proyectos:
        if type(proyecto["id"]) != int:
            proyecto["id"] = int(proyecto["id"])
            flag_dato_modificado = True
        if isinstance(proyecto["Presupuesto"], str):
            proyecto["Presupuesto"] = int(proyecto["Presupuesto"])
            flag_dato_modificado = True
        
    return flag_dato_modificado

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def promedio_presupuestos_proyectos(lista_proyectos: list[dict]):
    """Esta función calcula el promedio de los presupuestos de los proyectos.

    Args:
        lista_proyectos (list[dict]): Lista con proyectos en diccionarios.

    Returns:
        int: Retorna el promedio de los presupuestos.
    """
    contador_proyectos = 0
    acumulador_presupuestos = 0
    for proyecto in lista_proyectos:
        acumulador_presupuestos += proyecto["Presupuesto"]
        contador_proyectos += 1
    if contador_proyectos == 0:
        return 0
    promedio_presupuestos = acumulador_presupuestos / contador_proyectos
    return int(promedio_presupuestos)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def ordenar_lista_diccionarios(lista_proyectos: list[dict], orden: bool, valor_a_ordenar: str):
    """Esta función ordena una lista de diccionarios en función de un valor especificado.

    Args:
        lista_proyectos (list[dict]): Lista de diccionarios a ordenar.
        orden (bool): True para ordenar de Menor a mayor, False para ordenar de Mayor a menor en presupuesto y fechas, en Nombre de proyecto es al revez.
        valor_a_ordenar (str): Clave del diccionario por la que se ordenará.

    Returns:
        list[dict]: Lista de diccionarios ordenada.
    """
    if valor_a_ordenar:
        for i in range(len(lista_proyectos)):
            for j in range(1, len(lista_proyectos)):
                if orden:
                    if lista_proyectos[j][valor_a_ordenar] < lista_proyectos[j-1][valor_a_ordenar]:
                        aux = lista_proyectos[j]
                        lista_proyectos[j] = lista_proyectos[j-1]
                        lista_proyectos[j-1] = aux
                else:
                    if lista_proyectos[j][valor_a_ordenar] > lista_proyectos[j-1][valor_a_ordenar]:
                        aux = lista_proyectos[j]
                        lista_proyectos[j] = lista_proyectos[j-1]
                        lista_proyectos[j-1] = aux
        return lista_proyectos
    else: 
        print("No indico el valor a ordenar")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def retomar_proyecto(lista_proyectos:list[dict]):
    """Esta funcion retoma todos los proyectos que esten Cancelados y los pasa a Activo

    Args:
        lista_proyectos (list[dict]): Lista de diccionarios para iterar y recorrer
    """
    maximos_activos = verificar_cantidad_proyectos(lista_proyectos)
    if maximos_activos == True:
        id_proyecto = int(input("Ingrese el ID del proyecto a retomar: "))
        for proyecto in lista_proyectos:
            if proyecto["id"] == id_proyecto:
                if proyecto["Estado"] == "Cancelado":
                    proyecto["Estado"] = "Activo"
                    limpiar_consola()
                    print("Proyecto retomado correctamente.")
                    print("Actualice la vista para ver reflejados los cambios con opcion 5")
                    return
                else:
                    print("El proyecto no se puede retomar porque no está cancelado.")
                    return
        print("ID de proyecto no encontrado.")
    else:
        print("Alcanzo la cantidad maxima de 50 proyectos activos, debe cancelar o finalizar proyectos para poder ingresar nuevos proyectos")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def obtener_fecha_actual():
    """Obtiene la fecha actual sin la hora.

    Returns:
        str: Fecha actual en formato 'dd-mm-aaaa'.
    """
    fecha_actual = datetime.today().date()
    return fecha_actual.strftime("%d-%m-%Y")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def imprimir_proyectos_palabras_desarrollo(lista_proyectos: list[dict]):
    """Imprime los proyectos que contienen la palabra "desarrollo" en su descripción y que están cancelados,
    mostrando aquellos con el menor presupuesto, o todos en caso de empate.

    Args:
        lista_proyectos (list[dict]): Lista de proyectos representados como diccionarios.
    """
    lista_proyectos_palabra_desarrollo = []
    ordenar_lista_diccionarios(lista_proyectos,True,"Presupuesto")
    for proyecto in lista_proyectos:
        lista_palabra_desarrollo = proyecto["Descripción"].split(" ")
        for palabra in lista_palabra_desarrollo:
            if palabra.lower() == "desarrollo" and proyecto["Estado"] == "Cancelado":
                lista_proyectos_palabra_desarrollo.append(proyecto)
    
    if len(lista_proyectos_palabra_desarrollo) == 0:
        print("Error, no se encontraron proyectos que en su descripción tengan la palabra Desarrollo y que estén cancelados.\n")
    else:
        proyecto_menor_presupuesto = lista_proyectos_palabra_desarrollo[0]
        lista_menor_presupuesto = [proyecto_menor_presupuesto]

        for i in range(1, len(lista_proyectos_palabra_desarrollo)):
            if lista_proyectos_palabra_desarrollo[i]["Presupuesto"] < proyecto_menor_presupuesto["Presupuesto"]:
                proyecto_menor_presupuesto = lista_proyectos_palabra_desarrollo[i]
                lista_menor_presupuesto = [proyecto_menor_presupuesto]
            elif lista_proyectos_palabra_desarrollo[i]["Presupuesto"] == proyecto_menor_presupuesto["Presupuesto"]:
                lista_menor_presupuesto.append(lista_proyectos_palabra_desarrollo[i])

        if len(lista_menor_presupuesto) == 1:
            imprimir_proyecto(proyecto_menor_presupuesto)
        else:
            imprimir_todos_proyectos(lista_menor_presupuesto)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def top_tres_proyectos_activos(lista_proyectos:list[dict]):
    """Imprime los tres proyectos activos con el menor presupuesto.

    Args:
        lista_proyectos (list[dict]): Lista de proyectos representados como diccionarios.

    """

    lista_proyectos_activos = []

    ordenar_lista_diccionarios(lista_proyectos,True,"Presupuesto")

    for proyectos in lista_proyectos:
        if proyectos["Estado"] == "Activo":
            lista_proyectos_activos.append(proyectos)
    
    top_3_proyectos = lista_proyectos_activos[:3]

    if len(lista_proyectos_activos) < 3:
        print("Error, no se encontraron al menos 3 proyectos activos")
    else:
        imprimir_todos_proyectos(top_3_proyectos)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------



def verificar_cantidad_proyectos(lista_proyectos:list[dict]):
    """
    Verifica si hay al menos 50 proyectos activos en una lista de proyectos.

    Args:
        lista_proyectos (list[dict]): Lista de proyectos representados como diccionarios.

    Returns:
        bool: True si hay menos de 50 proyectos activos, False si hay al menos 50 proyectos activos.
    """
    contador = 0
    for proyectos in lista_proyectos:
        if proyectos["Estado"] == "Activo":
            contador += 1
    if contador >= 50:
        return False
    else:
        return True

