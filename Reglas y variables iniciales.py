'''-------------Introducción------------'''

'''El siete y medio es un juego de cartas que utiliza la baraja española de 40 cartas. El juego consiste en obtener
siete puntos y medio, o acercarse a esta puntuación lo más posible. Las cartas tienen, indistintamente de su palo,
el valor que indica su propio índice, excepto las figuras (sota, caballo y rey) que tienen una valor de medio punto
cada una. El objetivo es ganar los puntos apostados en cada tanda. En cada apuesta, cada jugador compite contra la
banca, para ganar la apuesta el objetivo es intentar sumar siete y medio o el número más cercano sin pasarse de
esta cantidad.'''

# Se puede definir la lista de cartas o generarla a partir de los numeros y los palos. Hay que ver si el indice de
# carta sera int o string

baraja_espanola_40 = [(1, 'Oros', 1), (1, 'Copas', 1), (1, 'Espadas', 1), (1, 'Bastos', 1),
                      (2, 'Oros', 2), (2, 'Copas', 2), (2, 'Espadas', 2), (2, 'Bastos', 2),
                      (3, 'Oros', 3), (3, 'Copas', 3), (3, 'Espadas', 3), (3, 'Bastos', 3),
                      (4, 'Oros', 4), (4, 'Copas', 4), (4, 'Espadas', 4), (4, 'Bastos', 4),
                      (5, 'Oros', 5), (5, 'Copas', 5), (5, 'Espadas', 5), (5, 'Bastos', 5),
                      (6, 'Oros', 6), (6, 'Copas', 6), (6, 'Espadas', 6), (6, 'Bastos', 6),
                      (7, 'Oros', 7), (7, 'Copas', 7), (7, 'Espadas', 7), (7, 'Bastos', 7),
                      ('sota', 'Oros', 0.5), ('sota', 'Copas', 0.5), ('sota', 'Espadas', 0.5), ('sota', 'Bastos', 0.5),
                      ('caballo', 'Oros', 0.5), ('caballo', 'Copas', 0.5), ('caballo', 'Espadas', 0.5), ('caballo', 'Bastos', 0.5),
                      ('rey', 'Oros', 0.5), ('rey', 'Copas', 0.5), ('rey', 'Espadas', 0.5), ('rey', 'Bastos', 0.5)]

# palo = 'Oros','Copas','Espadas','Bastos'
# cartas = '1','2','3','4','5','6','7','sota','caballo','rey'
# baraja_española_40 = []
# for i in cartas:
#     for j in palo:
#         carta = f'{i} de {j}'
#         baraja_española_40.append(carta)

'''El objetivo es ganar los puntos apostados en cada tanda. En cada apuesta, cada jugador
compite contra la banca, para ganar la apuesta el objetivo es intentar sumar siete y
medio o el número más cercano sin pasarse de esta cantidad.'''

apuesta = int               # Reglas apuesta: 20% puntos restantes redondeando hacia arriba, incrementa con el tiempo.

'''--------------------------Resumen del juego------------------------------'''

'''
-El número de jugadores debe estar entre 2 y 8.
-Se jugará un máximo de 30 manos.
-Cada jugador inicia la partida con 20 puntos.
-El programa reparte una carta a cada jugador. A partir de aquí, cada jugador realiza dos acciones:
    -En primer lugar, escoge cuantos puntos apuesta en esta jugada.
    -En segundo lugar, decide si quiere recibir más cartas del mazo. Si no quiere más cartas, se planta. Puede pedir 
     tantas cartas del mazo como crea conveniente y se puede plantar cuando quiera.
-Cuando todos han acabado de escoger cartas, el jugador que tiene siete y medio gana el doble de puntos de lo que había 
 apostado. En caso de que ningún jugador tenga siete y medio, el jugador que más se ha acercado a esta cantidad sin 
 pasarse, gana 1 punto. El resto de jugadores perderán tantos puntos como hayan apostado.
-El jugador que pierde todos sus puntos, queda eliminado de la partida.
-El jugador ganador es el que más puntos ha obtenido después de todas las
partidas jugadas.
'''

num_jugadores = input               # entre 2 y 8
jugadores = list                    # lista con los jugadores
usuario = input                     # Eleccion o creación?
turno = int                         # Máximo 30 turnos
puntos = int

'''----------------------------Desarrollo del juego---------------------------'''
'''
-Habrá un máximo de 8 jugadores
-Se podrán jugar 2 modalidades.
    -Todos los jugadores humanos.
    -1 jugador humano contra jugadores máquina.'''

modo_juego = '¿while + flag?'

'''
-Se reparten cartas del mazo a los jugadores para saber cómo quedan numerados, el número 1 el jugador con la carta más 
 alta y así sucesivamente.
-En caso de igualdad de números, la prioridad es oros copas espadas bastos.
-Se numeran los jugadores.
-El número 1 posee la banca.
-Cada jugador inicia la partida con 20 puntos.
-Habrá un máximo de 30 manos.
-Por turnos, el jugador con número más bajo primero, cada jugador:
    ● Realiza una apuesta dentro de un rango prefijado de 20% puntos restantes redondeado hacia arriba.
    ● Seguidamente debe decidir si desea recibir más cartas del mazo. Si no lo desea debe indicarlo diciendo que se 
      planta. Si por el contrario, desea cartas para intentar acercarse lo más posible a sumar siete y medio, podrá 
      pedir todas las que quiera de una en una pudiéndose plantar cuando quiera.
'''

prioridad_palo = 'por determinar'
prioridad_jugador = int             # orden de juego
banca = 'siempre es el jugador con prioridad 0 ( pone 1 pero seguramente se refiere al primero en orden )'
puntos_iniciales = 20
accion = input( 'Pasar o Robar' )

'''             Juega la banca

-Una vez hayan hecho las apuestas todos los jugadores, le llega el turno a la banca. Siquedara algún jugador que no se 
 hubiese pasado de siete y medio, y por lo tanto estátodavía en condiciones de poder ganar su apuesta, la banca 
 procederá a su vez a jugar.
-La banca no hace apuestas, simplemente recibe las de los jugadores, y juega como losdemás jugadores, plantándose (si 
 cree que así gana a todos o algunos de los jugadoresque quedan) o dándose cartas, de una en una, pero con todas sus 
 cartas boca arribahasta decidir plantarse.
'''

'''                Desarrollo
-La banca juega contra todos y cada uno de los jugadores, y por lo tanto si ella se ha pasado, deberá pagar a todos 
 aquellos jugadores que se hubieran plantado.
-Si la banca se ha plantado comprueba con cada jugador su jugada para ver a quién vence y con quién pierde. En cada 
 apuesta vence quien más se acerque a siete y medio.
-En caso de empate gana la banca; por lo tanto, si la banca tiene siete y medio gana automáticamente a todos los 
 jugadores.
-La banca debe pagar la cantidad apostada, a cada jugador con el que pierda, y a la inversa, cada jugador que pierda 
 con la banca debe pagarle a ésta lo apostado.
-Si un jugador tiene siete y medio (y la banca no) cobra el doble de lo apostado y además toma la banca en la mano 
 siguiente.
-El jugador que pierde sus puntos queda eliminado de la partida.
-La partida continúa hasta que un único jugador se hace con todos los puntos en juego, quedando los demás eliminados, o 
 bien hasta que se disputa el máximo de manos fijadas para la partida, que puede ser 15 ó 30, en cuyo caso el vencedor 
 es quien acumula mayor cantidad de puntos al final de la partida.
-La cantidad de puntos a apostar en cada mano se escoge entre 4 posibilidades, con valores que se van incrementando 
 paulatinamente a medida que se desarrolla el juego.
-En las primeras manos las apuestas posibles oscilan entre 2 y 5, y suben hasta un rango entre 6 y 12 puntos cuando el 
 número de manos ya se acerca al máximo de 15 ó 30.
-Cuando el jugador que posee la banca es eliminado, con el número más bajo.
'''

'''Lógica de las apuestas
-Cuando un jugador decide recibir una carta, lo hará en función de las cartas que hay repartidas , y lo hará calculando 
 la probabilidad de pasarse si recibiese una nueva carta .
-Es decir, si un jugador tiene por ejemplo un cinco, calculará todas las posibles cartas que supongan pasarse de 7 y 
 medio así como el número total de cartas que quedan por salir, la división entre el número de cartas que supongan 
 pasarse de 7 y medio y el número de cartas que quedan por salir multiplicado por 100 nos da la probabilidad de 
 pasarnos de 7 y medio. Si quedan en 10 cartas que supusiesen pasarnos de 7 y medio y un total de 20 cartas por salir, 
 esta probabilidad sería (10/20)*100 = 50%.
-Un jugador nunca arriesgará si esta probabilidad supera una probabilidad especificada más abajo.'''

probabilidad_exito = 'formula que determina el comportamiento del bot'





'''--------------------------------------M03 Programación----------------------------------'''

'''
-Se creará un lista de tuplas de cartas, a la que llamaremos mazo, en orden oros copas bastos espadas.
-Cada tupla representará una carta y sus valores serán ( valor real, prioridad, valor en el juego )
-Se podría crear un diccionario, pero la lista facilita acceder al índice dado de la carta para repartirla, eliminarla 
 si es repartida a algún jugador y añadirla a la lista de cartas del jugador.
mazo = [ ( valor real, prioridad, valor en el juego ) , ( valor real, prioridad, valor en el juego ) ….]'''

# El mazo ya está definido al inicio de este documento.

'''--------------------------------------Modo Juego Manual----------------------------------------'''

'''
-Lista de jugadores:
-Se irá pidiendo el nombre de los jugadores hasta un límite de 8 y se irán añadiendo a una lista inicial de jugadores.
-Los nombres de los jugadores sólo contendrán letras y números, empezando siempre por una letra, y no contendrán 
 espacios.
-Se escogerá una carta aleatoriamente del mazo por cada jugador con la que se decidirá el orden de prioridad de los 
 jugadores.
-La carta más alta determinará el jugador con mayor prioridad, la segunda más alta el segundo jugador con mayor 
 prioridad y así sucesivamente.
-En caso de cartas con valor real igual, gana la carta con mayor prioridad.
-El jugador con mayor prioridad pasará a ser la banca.
-Se creará la lista “jugadores” donde se insertarán los jugadores por orden de prioridad.


-Para cada jugador
-Un diccionario con clave su nombre y valor = lista de elementos:
    1. -Una lista de tuplas con las cartas que tiene el jugador, donde cada tupla representa una carta. 
       -El elemento 0 será la primera carta.
       -Todas las cartas se imprimirán en cada tirada para que podamos ver las cartas que han salido a los distintos 
        jugadores.
    2. -El estado del jugador en la mano actual, por defecto al principio de cada mano, será “jugando”.
    3. -Estado del jugador en la partida, “jugando” si tiene puntos, “eliminado” si no tiene puntos
    4. -Prioridad del jugador, 0 la banca, 1 primer jugador, ….
    5. -Puntos acumulados en la mano, lo que suman sus cartas, si su estado en la mano no es eliminado será menor o 
        igual a 7,5, en caso contrario, su estado en la mano será “eliminado”
    6. -Puntos apostados en la mano actual.
    7. -Puntos que le restan al jugador, nunca podrán ser negativos, si es cero y pierde dicha mano, su “estado partida” 
        pasará a ser “eliminado”.
    8. -Contador mano actual, empieza valiendo 1'''

mano = list
estado = 'jugando', 'plantado', 'eliminado'             # Una de las opciones
estado_partida = 'jugando', 'eliminado'                 # una de las opciones
puntos_mano = float
puntos_apostados = int
puntos_restantes = int                                  # Ojo con la opcion si apuesta all sera 0 pero no eliminado
contador_turno = int
jugador = dict                                          # {Jugador : [mano], estado, estado_partida, puntos_mano,
                                                        # puntos_apostados, puntos_restantes, contador_mano}

''' Continua en pag 8,9,10 del pdf definido el bucle paso a paso'''