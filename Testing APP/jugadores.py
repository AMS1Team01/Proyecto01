num_jugadores = ''
lista_jugadores = []
dict_jugadores = {}

while not num_jugadores.isdecimal():
    num_jugadores = input('Elige el numeo de jugadores para la partida')
num_jugadores = int(num_jugadores)

for jugador in range(num_jugadores):
    nombre = input('Escribe tu nombre')
    #nombre = f'jugador{jugador}'
    jugador_dict = {nombre: {'cartas': [], 'mano': 'jugando', 'partida': 'jugando', 'prioridad': 0, 'puntos_mano': 0, 'apuesta': 0, 'puntos_restantes': 20, 'turno': 1}}
    dict_jugadores.update(jugador_dict)

print(dict_jugadores)

for jugador in dict_jugadores.keys():
    print(jugador)
    lista_jugadores.append(jugador)
print(lista_jugadores)
