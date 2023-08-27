import csv
import pyperclip

# Ruta del archivo CSV
csv_file = 'data.csv'  # Reemplaza con la ruta de tu archivo CSV

# Nombre de la tabla en MySQL
table_name = 'docentes_cursos'  # Reemplaza con el nombre de la tabla en MySQL

# Abre el archivo CSV y lee los datos
with open(csv_file, 'r',encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    columnas = [] # Lista para almacenar los nombres de las columnas

    # Lee la primera fila (encabezados)
    headers = next(csv_reader)

    # Genera el script SQL
    sql_script = f"INSERT INTO {table_name} ("
    # Imprime los encabezados
    #for header in headers:
    columnas.append(headers[0])
    sql_script += headers[0] + ','
    columnas.append(headers[1])
    sql_script += headers[1] 
        #print("Encabezado:", header)
    sql_script = sql_script.rstrip(',')
    sql_script += ") VALUES\n"
    
    for row in csv_reader:
        cantColumnas = len(columnas)
        #sql_script += "     ("
        for valor in range(1,len(row)):
            #verificar si valor es nulo o no tiene nada
            if(row[valor] != ''):

                sql_script += f"     ({row[0]},"
            if row[valor] == '':
                sql_script = sql_script.rstrip(',')
                continue

            if row[valor].isdigit():
                sql_script += f"{row[valor]}),\n"
            else:
                sql_script += f"'{row[valor]}'),\n"
            

        sql_script = sql_script.rstrip(',') # Elimina la coma final de los valores de la ultima columna


    # Elimina la coma y el salto de línea finales
    sql_script = sql_script.rstrip(',\n')
    sql_script += ";"

# Imprime el script SQL resultante
print(sql_script)
# copiar la variavle sql_script al portapapels  

pyperclip.copy(sql_script)
