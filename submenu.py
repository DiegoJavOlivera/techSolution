from proyectos import *
from validaciones import *
from constantes import *
from archivos import *



def imprimir_sub_menu_():
    """Esta funcion imprime el sub menu en consola
    """
    print("\n\n*******************************************")
    print("*** Bienvenido al menu de modificaciones ***")
    print("*******************************************\n\n")
    print("Seleccione una opcion numerica:\n1. Modificar nombre\n2. Modificar descripcion\n3. Modificar fecha\n4. Modificar presupuesto\n5. Cambiar de estado el proyecto\n6. Finalizar modificaciones")

def sub_menu_modificaciones(lista_proyectos):
    """Esta funcion imprime el submenu de opciones para que el usuario pueda realizar
    modificaciones en los proyectos que tenga ingresados, se hace el llamados de funciones
    para realizar la busqueda de uno , imprimirlo en consola y realizar modificaciones sobre ese mismo.
    Al finalizar pregunta si quiere volver al menu principal o si quiere seguir modificando

    Returns:
        bool: retorna un bool, si se realizo un cambio retorna True caso contrario False
    """
    flag_modificacion = False
    ingresar_id = ingresar_opcion("\nIngresar el id del proyecto a modificar: ")
    if ingresar_id:   
        dict_proyecto = buscar_proyecto_id_str(ingresar_id,lista_proyectos,"id")
        while True:    

            if not dict_proyecto:
                print("No se encontro el proyecto, intentelo nuevamente")
                break
            else:
                imprimir_proyecto(dict_proyecto)
                imprimir_sub_menu_()
            opcion_menu = ingresar_opcion("Ingrese una opcion: ")
            if opcion_menu:
                opcion_menu = int(opcion_menu)
                match opcion_menu:
                    case 1:
                        nombre_proyecto = validar_nombre("Ingrese el nombre del proyecto: ", 30).capitalize()
                        modificacion_proyecto = modificar_proyecto("Nombre del Proyecto", dict_proyecto ,nombre_proyecto)
                        if modificacion_proyecto == True:
                            limpiar_consola()
                            print("Se a modificado el nombre del proyecto")
                            flag_modificacion = True
                        else:
                            limpiar_consola()
                            print("No se a podido modificar el nombre del proyecto")
                    case 2:                        
                        descripcion_proyecto = validar_descripcion("Ingrese la nueva descripcion del proyecto: ", 200).capitalize()
                        modificacion_proyecto = modificar_proyecto("Descripción",dict_proyecto,descripcion_proyecto)
                        if modificacion_proyecto == True:
                            limpiar_consola()
                            print("Se a modificado la descripcion del proyecto")
                            flag_modificacion = True
                        else:
                            limpiar_consola()
                            print("No se a podido modificar la descripcion del proyecto")
                    case 3:
                        nueva_fecha_inicio, nueva_fecha_fin = ingresar_fechas_proyecto()
                        modificar_fecha_inicio = modificar_proyecto("Fecha de inicio",dict_proyecto,nueva_fecha_inicio)
                        modificar_fecha_fin = modificar_proyecto("Fecha de Fin",dict_proyecto,nueva_fecha_fin)
                        if modificar_fecha_inicio == True and modificar_fecha_fin == True:
                            limpiar_consola()
                            print("Las fechas se modificaron con exito")
                            flag_modificacion = True
                        else:
                            limpiar_consola()
                            print("No se pudieron modificar las fechas")
                    case 4:
                        ingreso_presupuesto_modificar = validar_presupuesto()
                        modificado_presupuesto_proyecto = modificar_proyecto("Presupuesto",dict_proyecto,ingreso_presupuesto_modificar)
                        if modificado_presupuesto_proyecto == True:
                            limpiar_consola()
                            print("El presupuesto se a modificado")
                            flag_modificacion = True
                        else: 
                            limpiar_consola()
                            print("No se a podido modificar el presupuesto")
                    case 5:
                        estado_ingresado = cambiar_estado(lista_proyectos)
                        if estado_ingresado:
                            modificar_estado = modificar_proyecto("Estado",dict_proyecto,estado_ingresado)
                            if modificar_estado == True:
                                limpiar_consola()
                                print("Se a modificado el estado del proyecto")
                                flag_modificacion = True
                            else:
                                limpiar_consola()
                                print("No se a podido modificar el estado del proyecto")
                        else:
                            limpiar_consola()
                            print("Debe cancelar o finalizar proyectos para poder pasar a activo, se alcanzaron los 50 activos")
                    case 6:
                        finalizar_modificacion = input("Elija una opcion: \n1. Continuar modificando\n2. Finalizar modificacion, guardar y volver al menu principal\nOpcion: ")
                        if finalizar_modificacion == "1":
                            limpiar_consola()
                            print("Continua modificando....")

                        elif finalizar_modificacion == "2":
                            limpiar_consola()
                            if flag_modificacion == True:
                                parsear_lista_csv(lista_proyectos)
                                parsear_lista_json(lista_proyectos)
                                return flag_modificacion
                            else:
                                return flag_modificacion
                        else:
                            print("Opcion incorrecta, seleccione otra nuevamente")
                    case _:
                        print("Opcion incorrecta, vuelva a intentarlo")
    else:
        print("El id ingresado es invalido, debe ser numerico")

def imprimir_sub_menu_ordenar():
    """Esta funcion imprime por consola el menu de ordenamieto
    """
    print("Menu ordenamiento\n1. Ordenar por nombre de proyecto de A a la Z\n2. Ordenar por nombre de proyecto de la Z a la A \n3. Ordenar por presupuesto de menor a mayor\n4. Ordenar por presupuesto de mayor a menor\n5. Ordenar por fecha de inicio de menor a mayor\n6. Ordenar por fecha de inicio de mayor a menor\n")

def sub_menu_ordenar(lista_proyectos: list[dict]):
    """Esta función ordena los proyectos para mostrarlos de mayor a menor o de la A a la Z
    según la opción ingresada y luego la muestra ordenada en la consola.

    Args:
        lista_proyectos (list[dict]): Lista de diccionarios con proyectos.
    """
    imprimir_sub_menu_ordenar()
    ingrese_opcion = ingresar_opcion("Ingrese una opción: ")
    if 0 < ingrese_opcion < 7:
        if ingrese_opcion == 1:
            lista_ordenada = ordenar_lista_diccionarios(lista_proyectos, True, "Nombre del Proyecto")
            imprimir_todos_proyectos(lista_ordenada)
        elif ingrese_opcion == 2:
            lista_ordenada = ordenar_lista_diccionarios(lista_proyectos, False, "Nombre del Proyecto")
            imprimir_todos_proyectos(lista_ordenada)
        elif ingrese_opcion == 3:
            lista_ordenada = ordenar_lista_diccionarios(lista_proyectos, True, "Presupuesto")
            imprimir_todos_proyectos(lista_ordenada)
        elif ingrese_opcion == 4:
            lista_ordenada = ordenar_lista_diccionarios(lista_proyectos, False, "Presupuesto")
            imprimir_todos_proyectos(lista_ordenada)
        elif ingrese_opcion == 5:
            lista_ordenada = ordenar_lista_diccionarios(lista_proyectos, True, "Fecha de inicio")
            imprimir_todos_proyectos(lista_ordenada)
        elif ingrese_opcion == 6:
            lista_ordenada = ordenar_lista_diccionarios(lista_proyectos, False, "Fecha de inicio")
            imprimir_todos_proyectos(lista_ordenada)
    else:
        print("Opción incorrecta, vuelva al menú e inténtelo nuevamente")

        