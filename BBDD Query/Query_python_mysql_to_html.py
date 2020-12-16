import pymysql

############### CONFIGURAR ESTO ###################

# Conexión de base de datos.
conexion = "127.0.0.1"  # aquí pondremos nuestra dirección de la base de datos de Amazon web services
usuario = "alumne"  # usuario de la conexión
password = "alumne"  # contraseña
BBDD = "proyecto"  # base de datos a la cual nos vamos a conectar
db = pymysql.connect(conexion, usuario, password, BBDD)
##################################################

# query_sql = "SELECT p.idpartida,p.condiciones_victoria, p.ganador_partida,p.duracion FROM partida p "
query_sql = """SELECT t.idpartida AS Partida, COUNT(*) AS Cartas, SUM(valor) AS 'Valor Total'
                FROM
                    turnos t,
                    cartas c
                WHERE
                    t.carta_inicial = c.idcartas
                    GROUP BY t.idpartida
                    ORDER BY t.idturnos;"""


def query_to_xml(outfileName, query_sql):
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
                outfile.write('       <{}>{}</{}>\n'.format(cursor.description[index][0], row[index],
                                                            cursor.description[index][0]))
            outfile.write('\n  </row>\n')

        outfile.write('</mydata>\n')
        outfile.close()


def query_to_html(outfileName, query_sql):
    print("Informe sobre las partidas")
    with open(outfileName, "w") as outfile:
        db = pymysql.connect(conexion, usuario, password, BBDD)
        cursor = db.cursor()
        cursor.execute(query_sql)
        rows = cursor.fetchall()
        outfile.write('<!DOCTYPE html>\n<html lang="es" dir="ltr">\n')
        outfile.write(' <head>\n    <meta charset="utf-8">\n    <title></title>\n    '
                      '<link href="css/style.css" rel="stylesheet">\n  </head>\n')
        outfile.write(' <body>\n')
        outfile.write('     <table border="1">\n')
        outfile.write('         <caption>{}</caption>\n'.format(query_sql))
        outfile.write('         <thead>\n           <tr>\n')
        for index in range(len(cursor.description)):
            outfile.write('             <th>{}</th>\n'.format(cursor.description[index][0]))
        outfile.write('           </tr>\n         </thead>\n')
        outfile.write('         <tbody>\n')
        for row in rows:
            outfile.write('             <tr>\n')
            for data in row:
                outfile.write('                 <td>{}</td>\n'.format(data))
            outfile.write('             </tr>\n')
        outfile.write('            </tbody>\n')
        outfile.write('         </table>\n')
        outfile.write(' </body>\n</html>')


query_to_xml("Resultadoquery.xml", query_sql)
query_to_html("ResultadoQuery.html", query_sql)
db.close()
