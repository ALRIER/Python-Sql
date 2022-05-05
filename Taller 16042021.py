import mysql.connector
from mysql.connector import Error


def crear_conexion(nombre_host, usuario, contrasena, basedatos):
    conexion = None
    try:
        conexion = mysql.connector.connect(
                host = nombre_host,
                user = usuario,
                passwd = contrasena,
                database = basedatos
                )        
    except Error as e:
        print("Error al establecer conexión: ",e)
    
    return conexion

def consulta_registros(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)        
        result = cursor.fetchall()        
        for row in result:
            print(row)
    except Error as e:
         print("Se ha presentado error: ",e)



print(""" 
      
 ¡Bienvenido!
 _  __                         _   _                                           
 | |/ /                        | | | |                                          
 | ' / ___  _ __  _ __ __ _  __| | | |     ___  _ __ ___ _ __  ____             
 |  < / _ \| '_ \| '__/ _` |/ _` | | |    / _ \| '__/ _ \ '_ \|_  /             
 | . \ (_) | | | | | | (_| | (_| | | |___| (_) | | |  __/ | | |/ /              
 |_|\_\___/|_| |_|_|  \__,_|\__,_| |______\___/|_|  \___|_| |_/___|             
 """)

con = crear_conexion('34.122.51.150','leandropajarof','leandropajarof','leandropajarof')

continuar = True

while continuar:
    
    print(""" 
              **************
              Menu principal
              **************
          """)
    print("Ingrese una opción:")
    print("Visualizar datos producción (1)")
    print("Visualizar datos de producción de un municipio (2)")
    print("Actualizar el valor de producción de un registro dado el ID del registro (3)")   
    print("Crear tabla reporte con los datos de la vista produccion_view (R)")    
    print("Salir (S o s)")
    
    opcion = input("Ingresa una opción: ")
    
    if opcion == "1":
        consulta_registros(con,'SELECT * FROM produccion')
    elif opcion == "2":
        print('Visualizar datos de producción de un municipio')        
    elif opcion == "3":
        print('Actualizar el valor de producción de un registro dado el ID del registro')
        #crear función que solicite la cedula del vendedor y lo eliminde de la tabla vendedores
    elif opcion == "R" or opcion == "r":
        print('Crear tabla reporte con nombre reporteprod con los datos de la vista produccion_view')
        #crear función que solicite la cedula y el nuevo nombre del vendedor y lo modifique            
    elif opcion == "S" or opcion == "s":
        continuar = False
    else:
        print("""
              
        Opción incorrecta, intente nuevamente
              
        """)
    
print("""
      ¡Hasta pronto!
 _  __                         _   _                                           
 | |/ /                        | | | |                                          
 | ' / ___  _ __  _ __ __ _  __| | | |     ___  _ __ ___ _ __  ____             
 |  < / _ \| '_ \| '__/ _` |/ _` | | |    / _ \| '__/ _ \ '_ \|_  /             
 | . \ (_) | | | | | | (_| | (_| | | |___| (_) | | |  __/ | | |/ /              
 |_|\_\___/|_| |_|_|  \__,_|\__,_| |______\___/|_|  \___|_| |_/___|             
 """)

        
con.close()        

# Crear informe en google datastudio con los datos de la tabla reporte que visualice:
# Producción por municipio
# Producción por tipo de cultivo
# El rendimiento por tipo de cultivo
# Tabla con el nombre del municipio, nombre del cultivo, área sembrada, rendimiento, producción
