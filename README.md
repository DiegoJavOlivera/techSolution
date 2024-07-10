TechSolution Project
Descripción
Este proyecto es parte de un parcial universitario desarrollado por Diego Javier Olivera para la empresa TechSolution. Es un programa hecho en Python que ofrece diversas funcionalidades para la gestión y visualización de datos.

Características
Visualización de Tablas: Utiliza PrettyTable para mostrar datos en formato de tabla.
Gestión de Fechas y Tiempos: Utiliza datetime para manejar y mostrar datos relacionados con fechas y tiempos.
Requisitos
Para ejecutar este proyecto, necesitas tener instalado Python 3.x y las siguientes bibliotecas:

PrettyTable
datetime
Puedes instalarlas usando pip:

bash
Copiar código
pip install prettytable
Instalación
Clona este repositorio:
bash
Copiar código
git clone https://github.com/tu_usuario/tu_proyecto.git
Navega al directorio del proyecto:
bash
Copiar código
cd tu_proyecto
Instala las dependencias necesarias:
bash
Copiar código
pip install -r requirements.txt
Uso
A continuación se muestran ejemplos de cómo usar el programa:

Visualización de Tablas
python
Copiar código
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Nombre", "Descripción", "Fecha de Inicio", "Fecha de Fin", "Presupuesto", "Estado"]

# Añadir filas a la tabla
table.add_row(["Proyecto A", "Descripción A", "2024-01-01", "2024-12-31", "$1000000", "Activo"])

print(table)
Gestión de Fechas y Tiempos
python
Copiar código
from datetime import datetime

# Obtener la fecha y hora actual
now = datetime.now()
print("Fecha y Hora Actual:", now)

# Formatear la fecha
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Fecha Formateada:", formatted_date)
Contacto
Para más información, puedes contactarme a través de mi correo electrónico: diegolivera93@gmail.com

