import random

mazo = [(1, 'Oros', 1), (1, 'Copas', 1), (1, 'Espadas', 1), (1, 'Bastos', 1),
        (2, 'Oros', 2), (2, 'Copas', 2), (2, 'Espadas', 2), (2, 'Bastos', 2),
        (3, 'Oros', 3), (3, 'Copas', 3), (3, 'Espadas', 3), (3, 'Bastos', 3),
        (4, 'Oros', 4), (4, 'Copas', 4), (4, 'Espadas', 4), (4, 'Bastos', 4),
        (5, 'Oros', 5), (5, 'Copas', 5), (5, 'Espadas', 5), (5, 'Bastos', 5),
        (6, 'Oros', 6), (6, 'Copas', 6), (6, 'Espadas', 6), (6, 'Bastos', 6),
        (7, 'Oros', 7), (7, 'Copas', 7), (7, 'Espadas', 7), (7, 'Bastos', 7),
        (10, 'Oros', 0.5), (10, 'Copas', 0.5), (10, 'Espadas', 0.5), (10, 'Bastos', 0.5),
        (11, 'Oros', 0.5), (11, 'Copas', 0.5), (11, 'Espadas', 0.5), (11, 'Bastos', 0.5),
        (12, 'Oros', 0.5), (12, 'Copas', 0.5), (12, 'Espadas', 0.5), (12, 'Bastos', 0.5)]

jugador1 = 'Iwo'
jugador2 = 'Jose'
jugador3 = 'Pol'

lista_jugadores = [jugador1, jugador2, jugador3]

def repartir_cartas():
    carta = random.choice(mazo)
    mazo.pop(mazo.index(carta))