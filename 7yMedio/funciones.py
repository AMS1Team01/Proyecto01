
# Archivo con las funciones necesarias para el funcionamiento de nuestro programa 7YMedio.

import random
import xml.etree.ElementTree as ET                    # Se importa ElementTree para cargar los datos de los ficheros XML


def get_gonfig():
# Funcion para importar los datos de configuracion del juego desde XML y crer un diccionario con esas opciones.
    config_tree = ET.parse('Basic_Config_Game.xml')
    config_root = config_tree.getroot()
    lista_config = ['Num_Min_Players',
                    'Num_Max_Players',
                    'Num_Max_Rounds',
                    'Num_Initial_Points',
                    'Is_Allowed_Auto_Mode']
    carga_config = []
    dict_config = {}

    for config_xml_item in config_root:
        if config_xml_item in config_root[0:4]:
            carga_config.append(int(config_xml_item.text))
        elif config_xml_item == config_root[4]:
            carga_config.append(bool(config_xml_item.text))

    dict_config.update(zip(lista_config, carga_config))
    return dict_config

dict_palos = {'Oros': 4, 'Copas': 3, 'Espadas': 2, 'Bastos': 1 }              # Diccionario para almacenar la prioridad

def crear_mazo():
# Funcion para crear el mazo que usaremos en el juego a partir del fichero de cartas XML
    cartas_tree = ET.parse('xml_cartas.xml')
    cartas_root = cartas_tree.getroot()
    mazo_juego = []
    for carta_xml_item in cartas_root.findall('carta'):
        if carta_xml_item.find('activa').text == 'SI':
            valor = carta_xml_item.find('valor').text
            palo = carta_xml_item.find('palo').text
            valor_juego = carta_xml_item.find('valor_juego').text
            carta = (int(valor), palo, float(valor_juego))
            mazo_juego.append(carta)
    return mazo_juego

# Listas de apoyo para darle flavor al juego

nombres_bots = ['Pepe', 'Paco', 'Pedro', 'Ana', 'Maria', 'Julia', 'R2D2', 'C3PO', 'Bot1', 'Bot2', 'Bot3', 'Bot4',
                'Bot5', 'Bot6', 'Bot7', 'SuperSaiyan', 'Fantasma', 'Naruto', 'PakitoChocolatero', 'John Cena',
                'PepsiCola', 'Catwoman', 'Marilyn Manson', 'Freddy Kruger', 'Elon Musk', 'Juanra Bogor.', 'Pol69',
                'Soy Humano', 'Tu vecino', 'Prudencio', 'Angustias', 'Flugencia', 'Eustaquio', 'Pancracio', 'Ambrosio',
                'Lola Mento', 'Pere Gil', 'Tu padre', 'Krilin', 'Toguro', 'Gustav Klimt', 'Frida Khalo',
                'Freddy Mercury', 'Jax Teller', 'Rick y Morty', 'Mandalorian', 'Mandarina', 'SirPlatano', 'Pinochet',
                'Dracula']

lista_saludos = ['Hola', 'Bienvenido', 'Saludos', 'Buena suerte', 'Me alegro de tenerte aqui', 'Ánimo', 'Mucha suerte',
                 'Espero que ganes', 'No me decepciones', 'Que nombre tan bonito', 'Tu puedes', 'La gloria te aguarda',
                 'Que nadie te diga quien eres', 'Has entrenado duro para este momento', 'No somos nada', 'Ese',
                 'Vamosssssss', 'Mucha mierda', 'A por todas', 'A ganar', 'Demuéstrales lo que vales', 'Grande',
                 '¡Cuidado! Ha llegado']



def loading_app():
# Mensaje de bienvenida tras iniciar la aplicación
    loading_app = 0
    for i in range(15):
        loading_app += 0.5
        if loading_app == 7.5:
            print('¡¡Bienvenido al 7yMedio!!'.center(100))
        else:
            print(str(loading_app).center(100))
    input('Presiona "Enter" para continuar'.center(100))


def crear_jugadores(lista_jugadores, dict_jugadores, dict_config):
# Funcion para introducir el numero de jugadores, registrar sus nombres y crear los diccionarios para cada jugador
    num_jugadores = ''
    while not num_jugadores.isdecimal() or int(num_jugadores) not in range(int(dict_config['Num_Min_Players']),
                                                                           int(dict_config['Num_Max_Players'])+1):

        num_jugadores = input('Elige el numero de jugadores para la partida (De 2 a 8 jugadores)')

    num_jugadores = int(num_jugadores)                          # Se introduce el número de jugadores para la partida.

    for num in range(1, num_jugadores+1):                       # Por cada jugador se pide el nombre
        nombre = input(f'Jugador{num}, escribe tu nombre\n')    # y se crea su diccionario.
        jugador_dict = {nombre: {'cartas': [],
                                 'mano': 'jugando',
                                 'partida': 'jugando',
                                 'prioridad': 0,
                                 'puntos_mano': 0,
                                 'apuesta': None,
                                 'puntos_restantes': int(dict_config['Num_Initial_Points']),
                                 'turno': 1,
                                 'tipo': 'humano'}}
        dict_jugadores.update(jugador_dict)                     # Se añade al diccionario de jugadores
        print(f'{random.choice(lista_saludos)} {nombre}\n')     # Se saluda al jugador
    print('>'.ljust(num_jugadores * 20, '-'))

    print('Los jugadores son:')                             # Se imprime una lista con los jugadores a modo informativo
    for jugador in dict_jugadores.keys():
        print(jugador)
        lista_jugadores.append(jugador)
    print('>'.ljust(num_jugadores * 20, '-'))
    return lista_jugadores, dict_jugadores                      # Se devuelve los parametros de entrada modificados



def crear_bots(lista_jugadores, dict_jugadores, dict_config):
    num_jugadores = ''
# Funciona para crear los Bots automaticamente.
    if dict_config['Is_Allowed_Auto_Mode'] is True:             # Para poder usar 'Is_allowed_Auto_Mode'
        select_num_players = ''                                 # Si esta como TRUE significa que esta activa la opcion
        select_num_bots = ''                                    # para seleccionar varios jugadores contra BOTS.

        while not select_num_players.isdecimal() or int(select_num_players) not in \
                range(int(dict_config['Num_Min_Players'])-1, int(dict_config['Num_Max_Players'])):
            select_num_players = input('Elige el numero de jugadores humanos para la partida '
                                       '(De 1 a 7 jugadores Humanos)')  # Se pide numero de jugadores Humanos

        jugadores_restantes = 8 - int(select_num_players)       # Se Calcula cuantos slots quedan para los Bots

        while not select_num_bots.isdecimal() or int(select_num_bots) not in \
                range(int(dict_config['Num_Min_Players'])-1, int(jugadores_restantes)+1):
            select_num_bots = input(f'Elige el numero de jugadores BOT para la partida '
                                    f'(De 1 a {jugadores_restantes} bots)') # Se pide numero de Bots para la partida
        num_jugadores = int(select_num_players) + int(select_num_bots)      # Asignamos el numero total de jugadores

    elif dict_config['Is_Allowed_Auto_Mode'] is False:          # Si la opcion de config, es FALSE, el modo original
        num_jugadores = ''                                      # era 1 jugador vs varios bots
    while not str(num_jugadores).isdecimal() or int(num_jugadores) not in range(int(dict_config['Num_Min_Players']),
                                                                                int(dict_config['Num_Max_Players'])+1):
        num_jugadores = input('Elige el numero de jugadores para la partida (De 2 a 8 jugadores)')
    num_jugadores = int(num_jugadores)

    for num in range(1, num_jugadores+1):
        if num <= int(select_num_players):
            nombre = input(f'Jugador humano, escribe tu nombre\n')
            jugador_dict = {nombre: {'cartas': [],
                                     'mano': 'jugando',
                                     'partida': 'jugando',
                                     'prioridad': 0,
                                     'puntos_mano': 0,
                                     'apuesta': None,
                                     'puntos_restantes': int(dict_config['Num_Initial_Points']),
                                     'turno': 1,
                                     'tipo': 'humano'}}
            dict_jugadores.update(jugador_dict)
            print(f'{random.choice(lista_saludos)} {nombre}')
        if num > int(select_num_players):
            nombre_random = random.randint(0, len(nombres_bots) - 1)
            nombre = nombres_bots.pop(nombre_random)
            nombre = f'{nombre}-bot'
            jugador_dict = {nombre: {'cartas': [],
                                     'mano': 'jugando',
                                     'partida': 'jugando',
                                     'prioridad': 0,
                                     'puntos_mano': 0,
                                     'apuesta': None,
                                     'puntos_restantes': int(dict_config['Num_Initial_Points']),
                                     'turno': 1,
                                     'tipo': 'bot'}}
            dict_jugadores.update(jugador_dict)
            # print(f'{random.choice(lista_saludos)} {nombre}')

    print('Los jugadores son:')
    for jugador in dict_jugadores.keys():
        print(jugador)
        lista_jugadores.append(jugador)
    print('>'.ljust(num_jugadores * 20, '-'))
    return lista_jugadores, dict_jugadores


def decidir_orden(mazo_juego, dict_palos, lista_jugadores, dict_jugadores, orden_jugadores, orden_inicial):
# Funcion para decidir el orden de los jugadores en partida
    mazo = list(mazo_juego)
    for jugador in lista_jugadores:
        carta_rand = random.randint(0, len(mazo) - 1)
        carta = mazo.pop(carta_rand)
        orden_inicial.append([carta[0], dict_palos[carta[1]], jugador])
    orden_inicial.sort(reverse=True)
    for jugador in orden_inicial:
        orden_jugadores.append(jugador[2])
    for jugador in orden_jugadores:
        dict_jugadores[jugador]['prioridad'] = orden_jugadores.index(jugador)
    return orden_jugadores




def repartir_cartas(mazo, orden_jugadores, dict_jugadores):
# Funcion para repartir la carta inicial e imprimir el resumen la informacion de inicio de turno

    for jugador in orden_jugadores:  # Se reparten cartas a la banca y los jugadores que no esten eliminados
        carta_rand = random.randint(0, len(mazo) - 1)           # Se escoge un indice aleatorio de la baraja
        carta = mazo.pop(carta_rand)                            # Se saca de la lista de cartas
        dict_jugadores[jugador]['cartas'].append(carta)         # Se añade a la lista de cartas del jugador
        if dict_jugadores[jugador]['prioridad'] == 0:           # Diferenciamos el print de la banca del del jugador
            print(f'La banca ({jugador}) recibe {carta[0]} de {carta[1]}')
            dict_jugadores[jugador]['puntos_mano'] = carta[2]   # Actualizamos los puntos del jugador/banca
            print(f'{jugador} tiene {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
        else:
            print(f'{jugador} recibe {carta[0]} de {carta[1]}')
            dict_jugadores[jugador]['puntos_mano'] = carta[2]
            print(f'{jugador} tiene {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
    return mazo, orden_jugadores, dict_jugadores                # Se actualizan los elementos fuera de la funcion

def cambio_banca(orden_jugadores, dict_jugadores):
# Funcion que contempla el cambio de banca cuando un jugador saca 7 y Medio
    for jugador in orden_jugadores[1::]:                        # Se hace una comprobacion de los puntos de las manos
        if dict_jugadores[jugador]['puntos_mano'] == 7.5 and not \
                dict_jugadores[orden_jugadores[0]]['puntos_mano'] == 7.5:   # algun jugador tiene 7yMedio y la banca NO
            aux = orden_jugadores.pop(orden_jugadores.index(jugador))       # Se saca al jugador de la lista
            orden_jugadores.append(aux)                                     # Lo añadimos al final del orden de jugadores
                                                            # De esta manera solo hace falta intercambiarlo con la banca
            orden_jugadores[0], orden_jugadores[len(orden_jugadores) - 1] = orden_jugadores[len(orden_jugadores) - 1], orden_jugadores[0]
            print(f'Ahora {jugador} es la Banca')           # Se da la informacion al jugador
            break                                           # Con break nos aseguramos que solo el primer jugador
    # print(orden_jugadores)                                # con 7 y Medio se intercambie con la banca
    for jugador in orden_jugadores:                         # Actualizamos las prioridades de los diccionarios
        dict_jugadores[jugador]['prioridad'] = orden_jugadores.index(jugador)
    # print(dict_jugadores)


'''--------------------------Funciones para dar informacion formateada al jugador si la solicita---------------------'''

def ver_cabecera(orden_jugadores):
    print("ESTADO MESA".center((20 + 20 * len(orden_jugadores)), '-'))

def ver_jugadores(orden_jugadores):
    print('Jugador'.ljust(20), end='')
    for jugador in orden_jugadores:
        print(f'{jugador}'.ljust(20), end='')
    print()
    print(''.center((20 + 20 * len(orden_jugadores)), '-'))

def ver_estado_mano(orden_jugadores, dict_jugadores):
    print('Estado'.ljust(20), end='')
    for jugador in orden_jugadores:
        print(f"{dict_jugadores[jugador]['mano']}".ljust(20), end='')
    print()
    print(''.center((20 + 20 * len(orden_jugadores)), '-'))

def ver_valor_mano(orden_jugadores, dict_jugadores):
    print('Valor Mano'.ljust(20), end='')
    for jugador in orden_jugadores:
        print(f"{dict_jugadores[jugador]['puntos_mano']}".ljust(20), end='')
    print()
    print(''.center((20 + 20 * len(orden_jugadores)), '-'))

def ver_puntos_restantes(orden_jugadores, dict_jugadores):
    print('Puntos totales'.ljust(20), end='')
    for jugador in orden_jugadores:
        print(f"{dict_jugadores[jugador]['puntos_restantes']}".ljust(20), end='')
    print()
    print(''.center((20 + 20 * len(orden_jugadores)), '-'))

def ver_apuestas(orden_jugadores, dict_jugadores):
    print('Apuesta'.ljust(20), end='')
    for jugador in orden_jugadores:
        if dict_jugadores[jugador]['apuesta'] is None:
            print(''.ljust(20), end='')
        else:
            print(f"{dict_jugadores[jugador]['apuesta']}".ljust(20), end='')
    print()

def ver_cartas(orden_jugadores, dict_jugadores):                            # Para imprimir las cartas de la mano de
    print('Cartas'.ljust(20), end='')                                       # manera correcta y en columnas, se ha
    max_cartas_mano = 0                                                     # iterado las listas de cartas para
    for jugador in orden_jugadores:                                         # comprobar cuantas cartas tienen en mano.
        if len(dict_jugadores[jugador]['cartas']) > max_cartas_mano:        # Obteniendo el maximo valor entre los
            max_cartas_mano = len(dict_jugadores[jugador]['cartas'])        # jugadores, podemos indexar las listas
    for carta in range(0, max_cartas_mano):                                 # de cartas para imprimir ese indice por
        for jugador in orden_jugadores:                                     # jugador, comprobando que no nos pasamos
            if carta in range(len(dict_jugadores[jugador]['cartas'])):      # de rango durante la iteracion, ya que
                print(f"{dict_jugadores[jugador]['cartas'][carta][0]} de "  # cada jugador puede tener distinto numero
                      f"{dict_jugadores[jugador]['cartas'][carta][1]}".ljust(20), end='')   # de cartas.
            else:
                print(''.ljust(20), end='')
        print()
        print(''.ljust(20), end='')
    print()
    print(''.center((20 + 20 * len(orden_jugadores)), '-'))

def ver_mesa(orden_jugadores, dict_jugadores):
# Se ha separado la funcion de informacion global, en funciones de informacion mas pequeñas, de esta manera se pueden
# ordenar de la manera deseada, sin problema
    ver_cabecera(orden_jugadores)
    ver_jugadores(orden_jugadores)
    ver_estado_mano(orden_jugadores, dict_jugadores)
    ver_valor_mano(orden_jugadores, dict_jugadores)
    ver_cartas(orden_jugadores, dict_jugadores)
    ver_puntos_restantes(orden_jugadores, dict_jugadores)
    ver_apuestas(orden_jugadores, dict_jugadores)
    print(''.center((20 + 20 * len(orden_jugadores)), '=') + '\n')

def jugador_turno_reset(orden_jugadores, dict_jugadores):
# Funcion para resetear los parametros de los jugadores al final de cada turno
    for jugador in orden_jugadores:
        dict_jugadores[jugador]['cartas'] = []
        dict_jugadores[jugador]['mano'] = 'jugando'
        dict_jugadores[jugador]['puntos_mano'] = 0.0
        dict_jugadores[jugador]['apuesta'] = 0

def algoritmo_apuesta_bot(turno, dict_jugadores, jugador, orden_jugadores):
# Función que determina cuánto va a apostar el jugador BOT, en funcion del dinero que tenga, y de lo avanzada que esté
# la partida, de esta manera segun avanza el juego hará apuestas más arriesgadas pudiendo incluso hacer una mega
# apuesta al último turno si puede ganar con ello.
    if turno in range(1, 6):                                                    # Segun el turno, establecemos un
        rango_apuesta_bot = random.randint(                                     # rango de apuesta de segun los puntos
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 20),      # que le quedan al bot, y luego un rango
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 40))      # en el que puede apostar
        rango_apuesta_general = range(2, 5)
    elif turno in range(6, 11):
        rango_apuesta_bot = random.randint(
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 30),
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 50))
        rango_apuesta_general = range(4, 9)
    elif turno in range(11, 15):
        rango_apuesta_bot = random.randint(
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 40),
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 75))
        rango_apuesta_general = range(6, 13)
    elif turno in range(15, 21):
        rango_apuesta_bot = random.randint(
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 50),
            int(dict_jugadores[jugador]["puntos_restantes"]))
        rango_apuesta_general = range(8, 21)
    elif turno in range(21, 3):
        rango_apuesta_bot = random.randint(
            int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 50),
            int(dict_jugadores[jugador]["puntos_restantes"]))
        rango_apuesta_general = range(10, int(dict_jugadores[jugador]["puntos_restantes"]))
    elif turno == 30:
        if (dict_jugadores[jugador]["puntos_restantes"] * 2 > dict_jugadores[orden_jugadores[0]]["puntos_restantes"]) \
                and len(orden_jugadores) <= 3:
            rango_apuesta_bot = random.randint(int((dict_jugadores[jugador]["puntos_restantes"] / 100) * 95),
                                               int(dict_jugadores[jugador]["puntos_restantes"]))
            rango_apuesta_general = range(10, int(dict_jugadores[jugador]["puntos_restantes"]))
        else:
            rango_apuesta_bot = random.randint(int((dict_jugadores[jugador]["puntos_restantes"]/100)*50),
                                               int(dict_jugadores[jugador]["puntos_restantes"]))
            rango_apuesta_general = range(10, int(dict_jugadores[jugador]["puntos_restantes"]))

    if rango_apuesta_bot in rango_apuesta_general:                          # Si la apuesta del bot entra en el "rango
        dict_jugadores[jugador]["apuesta"] = rango_apuesta_bot              # general" apostará esa cantidad, en caso
    elif rango_apuesta_bot < rango_apuesta_general[0]:                      # contrario, se ajustará a los valores
        dict_jugadores[jugador]["apuesta"] = rango_apuesta_general[0]       # minimos o maximos según sea su apuesta.
    elif rango_apuesta_bot > rango_apuesta_general[-1]:
        dict_jugadores[jugador]["apuesta"] = rango_apuesta_general[-1]
    if dict_jugadores[jugador]["apuesta"] > dict_jugadores[jugador]["puntos_restantes"]:    # Se ajusta a los puntos
        dict_jugadores[jugador]["apuesta"] = dict_jugadores[jugador]["puntos_restantes"]    # restantes si no tiene
                                                                                            # suficientes puntos

def algoritmo_decision_bot(dict_jugadores, jugador, orden_jugadores, mazo):

# Función que determina la decisión del bot a la hora de pedir carta o plantarse

    if dict_jugadores[jugador]['puntos_mano'] <= dict_jugadores[orden_jugadores[0]]['puntos_mano']:
        accion = '1'                                                    # Si el bot tiene menos puntos que la banca
    elif dict_jugadores[jugador]['puntos_mano'] == 7.5:                 # robará carta. Si tiene 7 y medio se plantará.
        accion = '2'
    elif 7.5 > dict_jugadores[jugador]['puntos_mano'] > dict_jugadores[orden_jugadores[0]][
        'puntos_mano']:                                                 # Si los casos antriores no se cumplen, se
        no_se_pasa = 0                                                  # calcula la probabilidad de exito, contando
        for carta in mazo:                                              # las cartas que quedan en el mazo con las que
            if dict_jugadores[jugador]['puntos_mano'] + carta[2] <= 7.5:    # no se pasa, y sacando un porcentaje.
                no_se_pasa += 1
        probabilidad_exito = no_se_pasa / len(mazo)
        if probabilidad_exito > 0.65:                                   # La accion se determinará aleatoriamente en
            accion = '1'                                                # funcion de las probabilidades de éxito.
        elif probabilidad_exito <= 0.65 and probabilidad_exito >= 0.50:
            probabilidad_pedir = random.randint(1, 100)
            if probabilidad_pedir <= probabilidad_exito * 100:
                accion = '1'
            else:
                accion = '2'
        elif probabilidad_exito < 0.5:
            probabilidad_pedir = random.randint(1, 100)
            if probabilidad_pedir <= (probabilidad_exito * 100) / 3:
                accion = '1'
            else:
                accion = '2'
    return accion


def control_ganancias_banca(dict_jugadores, orden_jugadores, mazo):
# El BOT como banca tiene un algoritmo específico, diferente al sugerido. Según este algoritmo jugará conservadoramente
# para no ser eliminada por pasarse, si puede plantarse y obtener ganancias aunque quede algun jugador con más puntos
# en la mano.
    global accion
    global probabilidad_exito
    control_ganancias = 0
    if dict_jugadores[orden_jugadores[0]]['puntos_mano'] == 7.5:
        accion = '2'
    else:
        for jugador in orden_jugadores[1::]:
            if dict_jugadores[jugador]['mano'] == 'eliminado' or dict_jugadores[jugador]['puntos_mano'] <= \
                    dict_jugadores[orden_jugadores[0]]['puntos_mano']:
                control_ganancias += dict_jugadores[jugador]['apuesta']
            elif dict_jugadores[jugador]['puntos_mano'] > dict_jugadores[orden_jugadores[0]]['puntos_mano']:
                if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                    control_ganancias -= dict_jugadores[jugador]['apuesta'] * 2
                elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                    control_ganancias -= dict_jugadores[jugador]['apuesta']
        no_se_pasa = 0
        for carta in mazo:
            if dict_jugadores[orden_jugadores[0]]['puntos_mano'] + carta[2] <= 7.5:
                no_se_pasa += 1
        probabilidad_exito = no_se_pasa / len(mazo)
    return probabilidad_exito, control_ganancias

def accion_banca_bot(probabilidad_exito, control_ganancias, dict_jugadores, orden_jugadores):
    # global probabilidad_exito
    global accion
    if probabilidad_exito == 1:
        accion = '1'
    elif control_ganancias < 0:
        if dict_jugadores[orden_jugadores[0]]['puntos_restantes'] < abs(control_ganancias):
            accion = '1'
        elif probabilidad_exito > 0.65:
            accion = '1'
        elif probabilidad_exito <= 0.65 and probabilidad_exito >= 0.50:
            probabilidad_pedir = random.randint(1, 100)
            if probabilidad_pedir <= probabilidad_exito * 100:
                accion = '1'
            else:
                accion = '2'
        elif probabilidad_exito < 0.5:
            probabilidad_pedir = random.randint(1, 100)
            if probabilidad_pedir <= (probabilidad_exito * 100) / 3:
                accion = '1'
            else:
                accion = '2'

    elif control_ganancias in range(0, 13):
        if probabilidad_exito > 0.80:
            accion = '1'
        elif probabilidad_exito <= 0.80 and probabilidad_exito >= 0.50:
            probabilidad_pedir = random.randint(1, 100)
            if probabilidad_pedir <= probabilidad_exito * 100:
                accion = '1'
            else:
                accion = '2'
        elif probabilidad_exito < 0.5:
            probabilidad_pedir = random.randint(1, 100)
            if probabilidad_pedir <= (probabilidad_exito * 100) / 3:
                accion = '1'
            else:
                accion = '2'
    elif control_ganancias > 12:
        accion = '2'
    return accion

def creditos():
    print('Gracias por jugar a 7yMedio by "AMS1Team01"\n'.center(100))
    print('Creado por'.center(50) + 'AMS1Team01'.center(50))
    print('Diagrama de Chen'.center(50) + 'AMS1Team01'.center(50))
    print('Query Master'.center(50) + 'Jose Rosillo'.center(50))
    print('Program Structure'.center(50) + 'Iwopolski'.center(50))
    print('IA design'.center(50) + 'Pol69'.center(50))
    print('IA Banca'.center(50) + 'Iwopolski'.center(50))
    print('IA Implementation'.center(50) + 'Iwopolski'.center(50))
    print('Creacion tablas querys HTML'.center(50) + 'Jose Rosillo'.center(50))
    print('HTML architecture'.center(50) + 'Pol69'.center(50))
    print('CSS design'.center(50) + 'Pol69'.center(50))
    print('Diagrama de Clases'.center(50) + 'Pol69'.center(50))
    print('GitHub project Leader'.center(50) + 'Iwopolski'.center(50))
    print('Team organization Leader'.center(50) + 'Jose Rosillo'.center(50))
    print('README'.center(50) + 'Jose Rosillo'.center(50))
    print()
    print('External support'.center(100))
    print()
    print('BBDD Designer'.center(50) + 'Rafa Aracil'.center(50))
    print('XML Files'.center(50) + 'Jordi Garcia'.center(50))
    print('External Team Coach'.center(50) + 'Xavi Gomez'.center(50))
    print('AMS1Team01 are:'.center(100))
    print()
    print('Iwopolski'.center(100))
    print('Jose Rosillo'.center(100))
    print('Pol69'.center(100))
    input()