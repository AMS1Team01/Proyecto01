import random

OROS, COPAS, ESPADAS, BASTOS = 4, 3, 2, 1
SOTA, CABALLO, REY = 10, 11, 12

mazo_juego = ((1, 'OROS', 1), (1, 'COPAS', 1), (1, 'ESPADAS', 1), (1, 'BASTOS', 1),
        (2, 'OROS', 2), (2, 'COPAS', 2), (2, 'ESPADAS', 2), (2, 'BASTOS', 2),
        (3, 'OROS', 3), (3, 'COPAS', 3), (3, 'ESPADAS', 3), (3, 'BASTOS', 3),
        (4, 'OROS', 4), (4, 'COPAS', 4), (4, 'ESPADAS', 4), (4, 'BASTOS', 4),
        (5, 'OROS', 5), (5, 'COPAS', 5), (5, 'ESPADAS', 5), (5, 'BASTOS', 5),
        (6, 'OROS', 6), (6, 'COPAS', 6), (6, 'ESPADAS', 6), (6, 'BASTOS', 6),
        (7, 'OROS', 7), (7, 'COPAS', 7), (7, 'ESPADAS', 7), (7, 'BASTOS', 7),
        (10, 'OROS', 0.5), (10, 'COPAS', 0.5), (10, 'ESPADAS', 0.5), (10, 'BASTOS', 0.5),
        (11, 'OROS', 0.5), (11, 'COPAS', 0.5), (11, 'ESPADAS', 0.5), (11, 'BASTOS', 0.5),
        (12, 'OROS', 0.5), (12, 'COPAS', 0.5), (12, 'ESPADAS', 0.5), (12, 'BASTOS', 0.5))

# mazo_juego = ((1, 'OROS', 1), (1, 'COPAS', 1), (1, 'ESPADAS', 1), (1, 'BASTOS', 1),
#         (2, 'OROS', 2), (2, 'COPAS', 2), (2, 'ESPADAS', 2), (2, 'BASTOS', 2),
#         (3, 'OROS', 3), (3, 'COPAS', 3), (3, 'ESPADAS', 3), (3, 'BASTOS', 3),
#         (4, 'OROS', 4), (4, 'COPAS', 4), (4, 'ESPADAS', 4), (4, 'BASTOS', 4),
#         (5, 'OROS', 5), (5, 'COPAS', 5), (5, 'ESPADAS', 5), (5, 'BASTOS', 5),
#         (6, 'OROS', 6), (6, 'COPAS', 6), (6, 'ESPADAS', 6), (6, 'BASTOS', 6),
#         (7, 'OROS', 7), (7, 'COPAS', 7), (7, 'ESPADAS', 7), (7, 'BASTOS', 7),
#         (SOTA, 'OROS', 0.5), (SOTA, 'COPAS', 0.5), (SOTA, 'ESPADAS', 0.5), (SOTA, 'BASTOS', 0.5),
#         (CABALLO, 'OROS', 0.5), (CABALLO, 'COPAS', 0.5), (CABALLO, 'ESPADAS', 0.5), (CABALLO, 'BASTOS', 0.5),
#         (REY, 'OROS', 0.5), (REY, 'COPAS', 0.5), (REY, 'ESPADAS', 0.5), (REY, 'BASTOS', 0.5))


mazo = list(mazo_juego)

lista_jugadores = ['Iwo', 'Jose', 'Pol69']
dict_jugadores = {'Iwo': {'cartas': [],
                          'mano': 'jugando',
                          'partida': 'jugando',
                          'prioridad': int,
                          'puntos_mano': float,
                          'apuesta': int,
                          'puntos_restantes': 20,
                          'turno': 1},
                  'Jose': {'cartas': [],
                           'mano': 'jugando',
                           'partida': 'jugando',
                           'prioridad': int,
                           'puntos_mano': float,
                           'apuesta': int,
                           'puntos_restantes': 20,
                           'turno': 1},
                  'Pol69': {'cartas': [],
                            'mano': 'jugando',
                            'partida': 'jugando',
                            'prioridad': int,
                            'puntos_mano':  float,
                            'apuesta': int,
                            'puntos_restantes': 20,
                            'turno': 1}}

orden_inicial = []
orden_jugadores = []

for jugador in lista_jugadores:
    carta_rand = random.randint(0, len(mazo)-1)
    carta = mazo.pop(carta_rand)
    orden_inicial.append([carta, jugador])
orden_inicial.sort(reverse=True)
print(orden_inicial)
for jugador in orden_inicial:
    orden_jugadores.append(jugador[1])
print(orden_jugadores)
for jugador in orden_jugadores:
    dict_jugadores[jugador]['prioridad'] = orden_jugadores.index(jugador)

# Arreglar el siguiente print variará segun numero de jugadores

print(f'Se inicia el juego en el siguiente orden:\n -El primer jugador será {orden_jugadores[1]}\n -El segundo jugador será {orden_jugadores[2]}\n -La Banca es {orden_jugadores[0]}\n')

mazo = list(mazo_juego)



