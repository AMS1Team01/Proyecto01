lista_jugadores = ['a','b','c','d']

dict_jugadores = {'a': {'puntos_restantes': 7, 'mano': 'jugando', 'apuesta': 0, 'puntos_mano': 6},
              'b': {'puntos_restantes': 8, 'mano': 'jugando', 'apuesta': 6, 'puntos_mano': 8},
              'c': {'puntos_restantes': 10, 'mano': 'eliminado', 'apuesta': 2, 'puntos_mano': 7},
              'd': {'puntos_restantes': 7, 'mano': 'jugando', 'apuesta':3, 'puntos_mano': 5}}

for jugador in lista_jugadores[1::]:
    if (dict_jugadores[lista_jugadores[0]]['puntos_mano'] >= dict_jugadores[jugador]['puntos_mano'] and dict_jugadores[lista_jugadores[0]]['mano'] != 'eliminado') or dict_jugadores[jugador]['mano'] == 'eliminado':   # En la implantacion al bucle añadimos "and banca_gana_automaticamente is False" para no cobrar doble
        dict_jugadores[lista_jugadores[0]]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]
        dict_jugadores[jugador]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]

    elif (dict_jugadores[lista_jugadores[0]]['puntos_mano'] < dict_jugadores[jugador]['puntos_mano'] or dict_jugadores[lista_jugadores[0]]['mano'] == 'eliminado') and dict_jugadores[jugador]['mano'] != 'eliminado':

        if dict_jugadores[jugador]['puntos_mano'] == 7.5:
            if (dict_jugadores[jugador]["apuesta"] * 2) > dict_jugadores[lista_jugadores[0]]["puntos_restantes"]:
                resto_puntos_banca = dict_jugadores[lista_jugadores[0]]["puntos_restantes"]
                dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= resto_puntos_banca
                dict_jugadores[jugador]["puntos_restantes"] += resto_puntos_banca
            else:
                dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= (dict_jugadores[jugador]["apuesta"] * 2)
                dict_jugadores[jugador]["puntos_restantes"] += (dict_jugadores[jugador]["apuesta"] * 2)
        elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
            if dict_jugadores[jugador]["apuesta"] > dict_jugadores[lista_jugadores[0]]["puntos_restantes"]:
                resto_puntos_banca = dict_jugadores[lista_jugadores[0]]["puntos_restantes"]
                dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= resto_puntos_banca
                dict_jugadores[jugador]["puntos_restantes"] += resto_puntos_banca
            else:
                dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]
                dict_jugadores[jugador]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]