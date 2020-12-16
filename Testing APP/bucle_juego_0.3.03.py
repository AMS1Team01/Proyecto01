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

mazo = list(mazo_juego)

lista_jugadores = ['Iwo', 'Jose', 'Pol69']
dict_jugadores = {'Iwo': {'cartas': [],
                          'mano': 'jugando',
                          'partida': 'jugando',
                          'prioridad': 0,
                          'puntos_mano': float,
                          'apuesta': int,
                          'puntos_restantes': 20,
                          'turno': 1},
                  'Jose': {'cartas': [],
                           'mano': 'jugando',
                           'partida': 'jugando',
                           'prioridad': 1,
                           'puntos_mano': float,
                           'apuesta': int,
                           'puntos_restantes': 20,
                           'turno': 1},
                  'Pol69': {'cartas': [],
                            'mano': 'jugando',
                            'partida': 'jugando',
                            'prioridad': 2,
                            'puntos_mano': float,
                            'apuesta': int,
                            'puntos_restantes': 20,
                            'turno': 1}}

orden_jugadores = ['Iwo', 'Jose', 'Pol69']
game = True  # Flag para mantener la ejecución del juego
banca_gana_automaticamente = False  # Flag para saltar el loop de la banca si todos los jugadores han sido eliminados
turno = 0
while game is True:
    if turno >= 30:
        game = False
    turno += 1
    input(f'Ronda {turno}\n'
          f'\npresiona "enter" para continuar')

    # loop jugadores

    # Se reparten las cartas

    for jugador in lista_jugadores:  # Se reparten cartas a la banca y los jugadores que no esten eliminados
        if dict_jugadores[jugador]['partida'] == 'eliminado':
            continue
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

    # Por cada jugador:

    # Se piden apuestas
    if turno == 1:
        print('En el primer turno todos los jugadores apuestan la cantitad pre-fijada de 4 puntos\n')
    for jugador in lista_jugadores[1::]:
        if dict_jugadores[jugador]['partida'] == 'eliminado':
            continue
        if turno == 1:  # El primer turno la apuesta es fija (20% de total)
            dict_jugadores[jugador]["apuesta"] = 4
        elif turno != 1:  # Resto de turnos eleccion ( FALTA FIJAR LOS LIMITES DE LAS APUESTAS )
            while dict_jugadores[jugador]["apuesta"] == 0 or not dict_jugadores[jugador][
                "apuesta"].isdecimal():  # Comprobamos que el input sea correcto
                dict_jugadores[jugador]["apuesta"] = input(f'{jugador},¿Cuánto vas a apostar? '
                                                           f'Carta inicial: {dict_jugadores[jugador]["cartas"][0][0]} de {dict_jugadores[jugador]["cartas"][0][1]} '
                                                           f'({dict_jugadores[jugador]["cartas"][0][2]} puntos)\n')
                while int(dict_jugadores[jugador]["apuesta"]) > dict_jugadores[jugador]["puntos_restantes"]:
                    dict_jugadores[jugador]["apuesta"] = input(
                        f'Apuesta incorrecta. No puede ser superior a tus puntos restantes, entonces...\n'
                        f'{jugador},¿Cuánto vas a apostar? '
                        f'Carta inicial: {dict_jugadores[jugador]["cartas"][0][0]} de {dict_jugadores[jugador]["cartas"][0][1]} '
                        f'({dict_jugadores[jugador]["cartas"][0][2]} puntos)\n')
            dict_jugadores[jugador]["apuesta"] = int(dict_jugadores[jugador]["apuesta"])  # Convertimos el input a int
            print(f'apuesta = {dict_jugadores[jugador]["apuesta"]}\n')

        # Se pide accion

        accion = ''
        while accion != '1' or accion != '2':
            accion = input(f'{jugador}, Escoge acción:\n'
                           '1) Robar carta\n'
                           '2) Pasar\n')
            if accion == '1':
                carta_rand = random.randint(0, len(mazo) - 1)
                carta = mazo.pop(carta_rand)
                dict_jugadores[jugador]['cartas'].append(carta)
                dict_jugadores[jugador]['puntos_mano'] += carta[2]
                print(f'{jugador} roba {carta[0]} de {carta[1]}\n'
                      f'\nCartas en la mano:')

                for carta in dict_jugadores[jugador]['cartas']:
                    print(f'{carta[0]} de {carta[1]}')
                if dict_jugadores[jugador]["puntos_mano"] == 7.5:
                    print('Tienes 7yMedio!!')
                elif dict_jugadores[jugador]["puntos_mano"] > 7.5:
                    dict_jugadores[jugador]['mano'] = 'eliminado'
                    print(f'¡Que pena! {jugador} se ha pasado con {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
                    break
                else:
                    print(f'\n{jugador} tiene {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
            elif accion == '2':
                print(f'{jugador} se ha plantado con {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
                break
            else:
                print('opcion incorrecta\n')
    # loop Banca

    # Comprobamos si queda ALGÚN jugador en juego. Si no es asi la banca no juega y cobra.

    banca_gana_automaticamente = True  # Establecemos el flag en TRUE para que camie a FALSE en el momento que salga un solo jugador que sigue en partida
    for jugador in lista_jugadores[1::]:  # Loop para comprobar el estado de los jugadores
        if dict_jugadores[jugador]['partida'] == 'eliminado':  # Si el jugador no esta en juego, no cambia nada
            continue
        elif dict_jugadores[jugador]['mano'] == 'jugando':
            banca_gana_automaticamente = False  # Si el jugador está en juego, se camba el flag y la banca jugará este turno

    if banca_gana_automaticamente is True:
        print('Todos los Jugadores se han pasado, la Banca gana automaticamente')
        for jugador in lista_jugadores[1::]:
            dict_jugadores[lista_jugadores[0]]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]
            dict_jugadores[jugador]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]


    # Si quedan jugadores la banca juga:

    elif banca_gana_automaticamente is False:
        print(f'Es el turno de la banca({lista_jugadores[0]})\n'
              f'\nJugadores que siguen en juego:')
        for jugador in lista_jugadores[1::]:  # Loop para comprobar el estado de los jugadores
            if dict_jugadores[jugador]['partida'] == 'eliminado':  # Si el jugador no esta en juego, no cambia nada
                continue
            elif dict_jugadores[jugador]['mano'] == 'jugando':  # Si un jugador estra en juego damos la informacion.
                print(f'-{jugador} sigue en juego con {dict_jugadores[jugador]["puntos_mano"]} puntos.')

        # La banca escoge accion

        accion = ''
        while accion != '1' or accion != '2':
            accion = input(f'{lista_jugadores[0]}, Escoge acción:\n'
                           '1) Robar carta\n'
                           '2) Pasar\n')
            if accion == '1':
                carta_rand = random.randint(0, len(mazo) - 1)
                carta = mazo.pop(carta_rand)
                dict_jugadores[lista_jugadores[0]]['cartas'].append(carta)
                dict_jugadores[lista_jugadores[0]]['puntos_mano'] += carta[2]
                print(f'La Banca({lista_jugadores[0]}) roba {carta[0]} de {carta[1]}\n'
                      f'\nCartas en la mano:\n')

                for carta in dict_jugadores[lista_jugadores[0]]['cartas']:
                    print(f'{carta[0]} de {carta[1]}')
                print(f'\n({lista_jugadores[0]}) tiene {dict_jugadores[lista_jugadores[0]]["puntos_mano"]} puntos.')

                if dict_jugadores[lista_jugadores[0]]["puntos_mano"] == 7.5:
                    banca_gana_automaticamente = True
                elif dict_jugadores[lista_jugadores[0]]["puntos_mano"] > 7.5:
                    dict_jugadores[lista_jugadores[0]]['mano'] = 'eliminado'
                    print(
                        f'la banca ({lista_jugadores[0]}) se ha pasado con {dict_jugadores[lista_jugadores[0]]["puntos_mano"]} puntos.')
                    break
            elif accion == '2':
                print(
                    f'La banca ({lista_jugadores[0]}) se ha plantado con {dict_jugadores[lista_jugadores[0]]["puntos_mano"]} puntos.')
                break
            else:
                print('opcion incorrecta\n')

# En esta version dividimos las comprobaciones, para que primero paguen los juagadores a la banca por razones de posteriores pagos a jugadores

    for jugador in lista_jugadores[1::]:
        if (dict_jugadores[lista_jugadores[0]]['puntos_mano'] >= dict_jugadores[jugador]['puntos_mano'] and dict_jugadores[lista_jugadores[0]]['mano'] != 'eliminado') or (dict_jugadores[jugador]['mano'] == 'eliminado' and banca_gana_automaticamente is False):
            dict_jugadores[lista_jugadores[0]]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]
            dict_jugadores[jugador]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]



# Luego se realiza otro bucle para los pagos de la banca a los jugadores, contando ahora la banca con todos los puntos que podria tener.

    for jugador in lista_jugadores[1::]:
        if (dict_jugadores[lista_jugadores[0]]['puntos_mano'] < dict_jugadores[jugador]['puntos_mano'] or dict_jugadores[lista_jugadores[0]]['mano'] == 'eliminado') and dict_jugadores[jugador]['mano'] != 'eliminado':

            if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                if (dict_jugadores[jugador]["apuesta"] * 2) > dict_jugadores[lista_jugadores[0]]["puntos_restantes"]:
                    resto_puntos_banca = dict_jugadores[lista_jugadores[0]]["puntos_restantes"]
                    dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= resto_puntos_banca
                    dict_jugadores[jugador]["puntos_restantes"] += resto_puntos_banca
                else:
                    dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= (
                                dict_jugadores[jugador]["apuesta"] * 2)
                    dict_jugadores[jugador]["puntos_restantes"] += (dict_jugadores[jugador]["apuesta"] * 2)

            elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                if dict_jugadores[jugador]["apuesta"] > dict_jugadores[lista_jugadores[0]]["puntos_restantes"]:
                    resto_puntos_banca = dict_jugadores[lista_jugadores[0]]["puntos_restantes"]
                    dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= resto_puntos_banca
                    dict_jugadores[jugador]["puntos_restantes"] += resto_puntos_banca
                else:
                    dict_jugadores[lista_jugadores[0]]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]
                    dict_jugadores[jugador]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]

# Luego efectuamos los prints según el caso que se haya dado en la partida

    if dict_jugadores[lista_jugadores[0]]['mano'] == 'eliminado':
        for jugador in lista_jugadores[1::]:
            if dict_jugadores[jugador]['mano'] == 'jugando':
                if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                    print(f'{jugador} ha sacado 7 y Medio, gana {dict_jugadores[jugador]["apuesta"] * 2} puntos de la banca')
                elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                    print(f'{jugador} gana {dict_jugadores[jugador]["apuesta"]} puntos de la banca')
            elif dict_jugadores[jugador]['mano'] == 'eliminado':
                print(f'{jugador} se habia pasado, pero como la banca también se ha pasado no pierde puntos.')
    elif dict_jugadores[lista_jugadores[0]]['mano'] == 'jugando':
        if dict_jugadores[lista_jugadores[0]]["puntos_mano"] == 7.5:
            print(f'¡La banca ({lista_jugadores[0]}) ha ganado a todos con 7 y Medio!')
            for jugador in lista_jugadores[1::]:
                print(f'{jugador} pierde {dict_jugadores[jugador]["apuesta"]} puntos.')
        elif dict_jugadores[lista_jugadores[0]]["puntos_mano"] != 7.5:
            for jugador in lista_jugadores[1::]:
                if dict_jugadores[jugador]['mano'] == 'eliminado':
                    print(f'{jugador} pierde {dict_jugadores[jugador]["apuesta"]} puntos.')
                elif dict_jugadores[jugador]['mano'] != 'eliminado':
                    if dict_jugadores[lista_jugadores[0]]['puntos_mano'] >= dict_jugadores[jugador]['puntos_mano']:
                        print(f'{jugador} pierde {dict_jugadores[jugador]["apuesta"]} puntos.')
                    elif dict_jugadores[lista_jugadores[0]]['puntos_mano'] < dict_jugadores[jugador]['puntos_mano']:
                        if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                            print(
                                f'{jugador} ha sacado 7 y Medio, gana {dict_jugadores[jugador]["apuesta"] * 2} puntos de la banca')
                        elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                            print(f'{jugador} gana {dict_jugadores[jugador]["apuesta"]} puntos de la banca')

    print(f'La banca ahora tiene {dict_jugadores[lista_jugadores[0]]["puntos_restantes"]} puntos')

    for jugador in lista_jugadores:
        if dict_jugadores[jugador]['puntos_restantes'] <= 0:
            dict_jugadores[jugador]['partida'] = 'eliminado'
            if dict_jugadores[jugador]['prioridad'] == 0:
                print(f'La banca ({jugador}) ha sido eliminada')
                # funcionalidad cambio de prioridades
            else:
                print(f'El jugador {jugador} ha sido eliminado')

    '''



    '''

    # Comprobaciones estado y comparacion puntos para resolver apuestas.

    # print(f'La banca tiene {dict_jugadores[lista_jugadores[0]]["puntos_restantes"]} puntos ')
    # Aqui codigo para cambiar el orden si algun jugador ha sacado 7ymedio

    # Se resetean los jugadores al final del turno

    for jugador in lista_jugadores:
        dict_jugadores[jugador]['cartas'] = []
        dict_jugadores[jugador]['mano'] = 'jugando'
        dict_jugadores[jugador]['puntos_mano'] = 0.0
        dict_jugadores[jugador]['apuesta'] = 0
    mazo = list(mazo_juego)

'''
    En esta version del bucle.
        1) Se ha separado la comprobacion de puntos y pagos en 2 bucles, para que primero la banca se cobre las 
            apuestas y tenga todo el capital disponible para los pagos a los jugdores.
        
        
       
'''




