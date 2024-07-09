
from archivos import *
from validaciones import *
from proyectos import *
from submenu import *



def presentacion():
    print("********************************************************")
    print("***********  Bienvenidos a TechSolution   **************")
    print("********************************************************")

def imprimir_menu():
    presentacion()
    print("Menu de opciones: seleccione una opcion numerica para comenzar."
            "\n1. Ingresar proyecto"
            "\n2. Modificar proyecto"
            "\n3. Cancelar un proyecto"
            "\n4. Comprobar proyectos"
            "\n5. Mostrar todos"
            "\n6. Calcular presupuesto promedio"
            "\n7. Buscar proyecto por nombre"
            "\n8. Ordenar proyectos"
            "\n9. Retomar proyecto"
            "\n10. Ingresar presupuesto para generar reporte"
            "\n11. Realizar un informa con el nombre de un proyecto"
            "\n12. Salir"
            "\n13. Obtener los proyectos cancelados con menor presupuesto, en su descripcion tiene que tener la palabra desarrllo"
            "\n14. Top 3 de proyectos activos con menor presupuesto")

def menu_tipo_orden_lista():
    """print("Menu de ordenamiento, seleccione un tipo de orden: "
            "\n1. Ordenar por nombre de mayor a menor"
            "\n2. Ordenar por nombre de menor a mayor"
            "\n3. Ordenar por presupuesto de mayor a menor"
            "\n4. Ordenar por presupuesto de menor a mayor"
            "\n5. Ordenar por fecha de inicio de mayor a menor"
            "\n6. Ordenar por fecha de inicio de menor a mayor")

    """
    print("Menu de ordenamiento, seleccione un tipo de orden: "
            "\n1. Ordenar por nombre de A a la Z"
            "\n2. Ordenar por nombre de la Z a  la A"
            "\n3. Ordenar por presupuesto de mayor a menor"
            "\n4. Ordenar por presupuesto de menor a mayor"
            "\n5. Ordenar por fecha de inicio mas Alta a mas Antigua"
            "\n6. Ordenar por fecha de inicio mas Antigua a mas Alta")

def mostrar_menu():
    lista_parseada = parseo_csv("data\Proyectos.csv")
    parsear_lista_json(lista_parseada)
    datos_normalizado = normalizar_datos(lista_parseada)
    if datos_normalizado == True:
        print("Datos normalizados listo para usar")
        while True:
            normalizar_datos(lista_parseada)
            imprimir_menu()
            
            ingreso_opcion = ingresar_opcion("Opcion: ")
            
            match ingreso_opcion:
                case 1:
                    limpiar_consola()
                    nuevo_proyecto = crear_proyecto()
                    parsear_lista_csv(lista_parseada)
                    if nuevo_proyecto == True:
                        print("El proyecto se a creado con exito")
                case 2:
                    limpiar_consola()
                    imprimir_todos_proyectos(lista_parseada)
                    modificar_proyecto = sub_menu_modificaciones(lista_parseada)
                case 3:
                    id_proyecto_cancelar = cancelar_proyecto()
                    if id_proyecto_cancelar == True:
                        limpiar_consola()
                        print("El estado del projecto fue cambiado a cancelado\n\n")
                        parsear_lista_json(lista_parseada)
                        parsear_lista_csv(lista_parseada)
                    else:
                        limpiar_consola()
                        print("El proyecto no a podido cancelarse\n\n")
                case 4:
                    proyectos_vencidos = validar_fecha_actual_superior(lista_parseada)
                    if proyectos_vencidos:
                        limpiar_consola()
                        parsear_lista_json(lista_parseada)
                        parsear_lista_csv(lista_parseada)
                        print("Los proyectos vencidos fueron modificados y cambiados a finalizado\n\n")
                case 5:
                    limpiar_consola()
                    imprimir_todos_proyectos(lista_parseada)
                case 6:
                    resultado_promedio_presupuesto = promedio_presupuestos_proyectos(lista_parseada)
                    limpiar_consola()
                    print(f"El promedio de todos los proyectos cargados es de: {resultado_promedio_presupuesto}\n\n")
                case 7:
                    limpiar_consola()
                    imprimir_todos_proyectos(lista_parseada)
                    nombre_proyecto = buscar_proyecto_por_nombre("Ingrese el nombre del proyecto que desea buscar, respetando sus acentos: ")
                    busqueda_proyecto_nombre = buscar_proyecto_id_str(nombre_proyecto,lista_parseada,"Nombre del Proyecto")
                    if isinstance(busqueda_proyecto_nombre,dict):
                        limpiar_consola()
                        imprimir_proyecto(busqueda_proyecto_nombre)
                    else:
                        limpiar_consola()
                        print("El proyecto que intenta buscar no se encuentre, intentelo nuevamente y verifique el nombre")
                case 8:
                    limpiar_consola()
                    menu_tipo_orden_lista()
                    ingreso_opcion_orden = ingresar_opcion("Opcion: ")
                    match ingreso_opcion_orden:
                        case 1: 
                            limpiar_consola()
                            lista_ordenada_may_men_nombre = ordenar_lista_diccionarios(lista_parseada,True,"Nombre del Proyecto")
                            imprimir_todos_proyectos(lista_ordenada_may_men_nombre)
                        case 2:
                            limpiar_consola()
                            lista_ordenada_men_may_nombre = ordenar_lista_diccionarios(lista_parseada,False,"Nombre del Proyecto")
                            imprimir_todos_proyectos(lista_ordenada_men_may_nombre)
                        case 3:
                            limpiar_consola()
                            lista_ordenada_presupuesto_may_menor = ordenar_lista_diccionarios(lista_parseada,False,"Presupuesto")
                            imprimir_todos_proyectos(lista_ordenada_presupuesto_may_menor)
                        case 4:
                            limpiar_consola()
                            lista_ordenada_presupuesto_men_may = ordenar_lista_diccionarios(lista_parseada,True,"Presupuesto")
                            imprimir_todos_proyectos(lista_ordenada_presupuesto_men_may)
                        case 5:
                            limpiar_consola()
                            lista_ordenada_fecha_inicio_may_men = ordenar_fechas(lista_parseada,False)
                            imprimir_todos_proyectos(lista_ordenada_fecha_inicio_may_men)
                        case 6:
                            limpiar_consola()
                            lista_ordenada_fecha_inicio_men_may = ordenar_fechas(lista_parseada, True)
                            imprimir_todos_proyectos(lista_ordenada_fecha_inicio_men_may)
                        case _:
                            limpiar_consola()
                            print("La opcion ingresada es incorrecta")
                case 9:
                    limpiar_consola()
                    imprimir_todos_proyectos(lista_parseada)
                    retomar_proyecto(lista_parseada)
                    parsear_lista_json(lista_parseada)
                    parsear_lista_csv(lista_parseada)
                
                case 10:
                    limpiar_consola()
                    imprimir_todos_proyectos(lista_parseada)
                    generar_reporte_presupuesto(lista_parseada)
                case 11:
                    limpiar_consola()
                    imprimir_todos_proyectos(lista_parseada)
                    generar_reporte_proyecto(lista_parseada)
                case 12:
                    limpiar_consola()
                    parsear_lista_json(lista_parseada)
                    parsear_lista_csv(lista_parseada)
                    finalizar_programa()
                case 13:
                    pass