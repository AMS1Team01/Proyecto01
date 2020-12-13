# import random
# puntos = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
# jugadores = ['banca', 'jose', 'pol69']
#
#
# jose = random.choice(puntos)
# pol69 = random.choice(puntos)
# jugadores = [jose, pol69]
# for jugador in jugadores:
#     if jugador > 7.5:
#         jugador = [jugador, 'eliminado']
#     else:
#         jugador = [jugador, 'jugando']
# print(jose)
# print(pol69)
#
# print(jugadores[1])
#
# if 'jugando' not in jugadores[1]:
#     print(f'banca gana porque todos se han pasado')
#
# banca = random.choice(puntos)

if 'jugando' in jugadores[1]:
    for jugador in jugadores:
        if banca != 'jugando':
            if 'jugando' in jugador:
        elif banca >= jugador:
            if banca == 7.5:
            elif banca != 7.5:
        elif banca < jugador:
            if jugador == 7.5:
            elif jugador != 7.5:


if banca['mano'] == 'jugando':                          # Se comprueba si la banca esta en juego
    if banca_gana_automaticamente is True:              # Se comprueba si la banca gana a todos con 7ymedio
        for jugador in lista_jugadores[1::]:            # Si gana a todos recoge apuestas de todos los jugadores (NO SABEMOS SI BANCA COBRA DOBLE POR 7YMEDIO)
            if jugador <= 0:                            # Si el jugador tiene 0 o menos puntos es eliminado
                jugador["partida"] = 'eliminado'

    elif banca_gana_automaticamente is False:                                 # Si no gana automaticamente hay que comprobar las puntuaciones.
        for jugador in lista_jugadores[1::]:
            if jugador['mano'] == 'eliminado':              # Si el jugador se habia pasado la banca ya gana.
            elif jugador['mano'] == 'jugando':
                if banca["puntos_mano"] >= jugador["puntos_mano"]:
                elif banca["puntos_mano"] < jugador["puntos_mano"]:
                    if jugador["puntos_mano"] == 7.5:
                    elif jugador["puntos_mano"] != 7.5:
            if jugador["puntos_restantes"] <= 0:                        # Si el jugador tiene 0 o menos puntos es eliminado
                jugador["partida"] = 'eliminado'
            if banca["puntos_restantes"] <= 0:             # Si la banca tiene 0 o menos puntos es eliminado
                banca["partida"] = 'eliminado'

elif banca['mano'] == 'eliminado':                         # Si la banca se pasa
    for jugador in lista_jugadores[1::]:
        if jugador['mano'] == 'jugando':
            if jugador["puntos_mano"] == 7.5:
            elif jugador["puntos_mano"] != 7.5:
        dict_jugadores[jugador]["apuesta"] = 0



