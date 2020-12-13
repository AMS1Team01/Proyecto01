import random
# archivo con las funciones necesarias para el funcionamiento del 7YMedio.
mazo = []

num_cartas = {'AS': 1, 'DOS': 2, 'TRES': 3, 'CUATRO': 4, 'CINCO': 5, 'SEIS': 6, 'SIETE': 7,
              'SOTA': 10, 'CABALLO': 11, 'REY': 12}
palo_cartas = ('OROS', 'COPAS', 'ESPADAS', 'BASTOS')

valor_cartas = {'AS': 1, 'DOS': 2, 'TRES': 3, 'CUATRO': 4, 'CINCO': 5, 'SEIS': 6, 'SIETE': 7,
                'SOTA': 0.5, 'CABALLO': 0.5, 'REY': 0.5}

OROS, COPAS, ESPADAS, BASTOS = 4, 3, 2, 1

def crear_mazo():
# Funcion para crear el mazo del juego

    for num in num_cartas:
        for palo in palo_cartas:
            mazo.append((num_cartas[num], palo, valor_cartas[num]))
    return mazo


num_jugadores = ''

def crear_jugadores(num_jugadores, lista_jugadores, dict_jugadores):
# Funcion para introducir el numero de jugadores, registrar sus nombres y crear los diccionarios para cada jugador

    while not num_jugadores.isdecimal() or int(num_jugadores) not in range(2, 9):
        num_jugadores = input('Elige el numero de jugadores para la partida (De 2 a 8 jugadores)')
    num_jugadores = int(num_jugadores)

    for num in range(1, num_jugadores+1):
        nombre = input(f'Jugador{num}, escribe tu nombre\n')
        jugador_dict = {nombre: {'cartas': [], 'mano': 'jugando', 'partida': 'jugando', 'prioridad': 0, 'puntos_mano': 0, 'apuesta': 0, 'puntos_restantes': 20, 'turno': 1}}
        dict_jugadores.update(jugador_dict)
    print('Los jugadores son:')
    for jugador in dict_jugadores.keys():
        print(jugador)
        lista_jugadores.append(jugador)
    return lista_jugadores, dict_jugadores


def decidir_orden(mazo, lista_jugadores, dict_jugadores, orden_jugadores, orden_inicial):
# Funcion para decidir el orden de los jugadores en partida

    for jugador in lista_jugadores:
        carta_rand = random.randint(0, len(mazo) - 1)
        carta = mazo.pop(carta_rand)
        orden_inicial.append([carta, jugador])
    orden_inicial.sort(reverse=True)
    print(orden_inicial)
    for jugador in orden_inicial:
        orden_jugadores.append(jugador[1])
    print(orden_jugadores)
    for jugador in orden_jugadores:
        dict_jugadores[jugador]['prioridad'] = orden_jugadores.index(jugador)
    return orden_jugadores, orden_inicial
# Aqui falta un print con los resultados del orden.

def repartir_cartas(mazo, orden_jugadores, dict_jugadores):
# Funcion para repartir la carta inicial e imprimir el resumen

    for jugador in orden_jugadores:  # Se reparten cartas a la banca y los jugadores que no esten eliminados
        carta_rand = random.randint(0, len(mazo) - 1)
        carta = mazo.pop(carta_rand)
        dict_jugadores[jugador]['cartas'].append(carta)
        if dict_jugadores[jugador]['prioridad'] == 0:  # Diferenciamos el print de la banca del del jugador
            print(f'La banca ({jugador}) recibe {carta[0]} de {carta[1]}')
            dict_jugadores[jugador]['puntos_mano'] = carta[2]
            print(f'{jugador} tiene {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
        else:
            print(f'{jugador} recibe {carta[0]} de {carta[1]}')
            dict_jugadores[jugador]['puntos_mano'] = carta[2]
            print(f'{jugador} tiene {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
    return mazo, orden_jugadores, dict_jugadores