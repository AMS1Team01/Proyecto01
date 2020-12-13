import random

# Definir variables de inicio

sota, caballo, rey = 10, 11, 12

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

mazo_figuras = [(1, 'Oros', 1), (1, 'Copas', 1), (1, 'Espadas', 1), (1, 'Bastos', 1),
        (2, 'Oros', 2), (2, 'Copas', 2), (2, 'Espadas', 2), (2, 'Bastos', 2),
        (3, 'Oros', 3), (3, 'Copas', 3), (3, 'Espadas', 3), (3, 'Bastos', 3),
        (4, 'Oros', 4), (4, 'Copas', 4), (4, 'Espadas', 4), (4, 'Bastos', 4),
        (5, 'Oros', 5), (5, 'Copas', 5), (5, 'Espadas', 5), (5, 'Bastos', 5),
        (6, 'Oros', 6), (6, 'Copas', 6), (6, 'Espadas', 6), (6, 'Bastos', 6),
        (7, 'Oros', 7), (7, 'Copas', 7), (7, 'Espadas', 7), (7, 'Bastos', 7),
        ('sota', 'Oros', 0.5), ('sota', 'Copas', 0.5), ('sota', 'Espadas', 0.5), ('sota', 'Bastos', 0.5),
        ('caballo', 'Oros', 0.5), ('caballo', 'Copas', 0.5), ('caballo', 'Espadas', 0.5), ('caballo', 'Bastos', 0.5),
        ('rey', 'Oros', 0.5), ('rey', 'Copas', 0.5), ('rey', 'Espadas', 0.5), ('rey', 'Bastos', 0.5)]

jugador1 = 'Iwo'
jugador2 = 'Jose'
jugador3 = 'Pol'
jugador4 = None
jugador5 = None
jugador6 = None
jugador7 = None
jugador8 = None
oros, copas, espadas, bastos = 'prioridad4', 'prioridad3', 'prioridad2', 'prioridad1'

# iniciar loop del juego



# Escoger modo



# introducir numero jugadores



# pedir nombres jugadores



# escoger orden jugadores


orden_inicial = []
orden_jugadores = []
lista_jugadores = [jugador1, jugador2, jugador3,]
for jugador in lista_jugadores:
    carta = random.choice(mazo)
    mazo.pop(mazo.index(carta))
    orden_inicial.append([carta, jugador])
orden_inicial.sort(reverse=True)
print(orden_inicial)
for posicion in orden_inicial:
    orden_jugadores.append(posicion[1])
print(orden_jugadores)

for jugador in range(1,len(orden_jugadores)):



