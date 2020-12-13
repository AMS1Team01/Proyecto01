import pymysql

############### CONFIGURAR ESTO ###################

# Conexión de base de datos.
conexion = "127.0.0.1"  # aquí pondremos nuestra dirección de la base de datos de Amazon web services
usuario = "root"  # usuario de la conexión
password = "toor"  # contraseña
BBDD = "proyecto"  # base de datos a la cual nos vamos a conectar
db = pymysql.connect(conexion, usuario, password, BBDD)
##################################################


# Cursor_descripcion:
#  (('idpartida', 3, None, 11, 11, 0, False), ('condiciones_victoria', 253, No.....
# es una tupla de tuplas, sólo nos interesa el primer campo que son las cabeceras de las tablas

# tipo rows =  <class 'tuple'>
# ((1, '30 Rondas max. Gana la puntuacion mas alta.', 2, '1'), (2, '30 Rondas max. Gana la puntuacion mas alta.', 6, '3')
# tupla de tuplas, cada tupla es una de las filas de la consulta.None

#query_sql = "SELECT p.idpartida,p.condiciones_victoria, p.ganador_partida,p.duracion FROM partida p "
query_sql = "select * from partida"

def query_to_xml(outfileName,query_sql):
    print("Informe sobre las partidas")
    with open(outfileName, "w") as outfile:
        db = pymysql.connect(conexion, usuario, password, BBDD)
        cursor = db.cursor()
        cursor.execute(query_sql)
        rows = cursor.fetchall()
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<mydata>\n')
        for row in rows:
            outfile.write('  <row>\n')
            for index in range(len(row)):
                # print("cursor[index][0] = {}, row[index] = {} ".format(cursor.description[index][0],row[index]))

                outfile.write('       <{}>{}</{}>\n'.format(cursor.description[index][0],row[index],cursor.description[index][0]))
            outfile.write('\n  </row>\n')

        outfile.write('</mydata>\n')
        outfile.close()
query_to_xml("Resultadoquery.xml",query_sql)
# desconectamos
db.close()