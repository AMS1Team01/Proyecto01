

import random
import funciones

app = True
modo_juego = False
game = False

dict_config = funciones.get_gonfig()
mazo_juego = funciones.crear_mazo()


while app is True:
    funciones.loading_app()

    modo_juego = True
    while modo_juego is True:
        elegir_modo = input('\n' + 'Por favor, elige modo de juego:'.center(100) + '\n' +
                            '\n' + '1) Un jugador contra Bots'.center(100) + '\n' +
                            '2) Multijugador'.center(90) + '\n' +
                            '3) Salir'.center(82))
        if elegir_modo == '1':
            print('Modo Jugadores Versus Bots\n')
            game = True                                         # Flag para entrar y mantener la ejecución de la partida
            modo_juego = False
        elif elegir_modo == '2':
            print('Modo para varios jugadores.\n')
            game = True                                         # Flag para entrar y mantener la ejecución de la partida
            modo_juego = False
        elif elegir_modo == '3':
            funciones.creditos()
            app = False
            modo_juego = False
        else:
            print('Opción incorrecta.\n')
    lista_jugadores = []
    dict_jugadores = {}
    orden_inicial = []
    orden_jugadores = []
    if elegir_modo == '1':
        funciones.crear_bots(lista_jugadores, dict_jugadores, dict_config)
    elif elegir_modo == '2':
        funciones.crear_jugadores(lista_jugadores, dict_jugadores, dict_config)
    funciones.decidir_orden(mazo_juego, funciones.dict_palos, lista_jugadores, dict_jugadores, orden_jugadores, orden_inicial)
    print(f'{orden_jugadores[0]} empieza como la Banca\nEl resto de jugadores juegan en el siguiente orden:')
    for jugador in orden_jugadores[1::]:
        print(f'{jugador}')
    mazo = list(mazo_juego)
    banca_gana_automaticamente = False  # Flag para saltar el loop de la banca si todos los jugadores han sido eliminados
    turno = 0
    while game is True:


        turno += 1
        input(f'Ronda {turno}\n'
              f'\npresiona "enter" para continuar')

        # loop jugadores

        # Se reparten las cartas
        funciones.repartir_cartas(mazo, orden_jugadores, dict_jugadores)

        # Por cada jugador:
        # Se piden apuestas
        if turno == 1:
            print('En el primer turno todos los jugadores apuestan la cantitad pre-fijada de 4 puntos\n')
            for jugador in orden_jugadores[1::]:
                dict_jugadores[jugador]["apuesta"] = 4
        for jugador in orden_jugadores[1::]:
            if turno != 1:  # Resto de turnos eleccion
                while dict_jugadores[jugador]["apuesta"] == 0 or dict_jugadores[jugador]["apuesta"] is None or not \
                        str(dict_jugadores[jugador][
                                "apuesta"]).isdecimal():  # Comprobamos que el input sea correcto
                    if dict_jugadores[jugador]["tipo"] == 'bot':
                        funciones.algoritmo_apuesta_bot(turno, dict_jugadores, jugador, orden_jugadores)
                        print(f'{jugador} ha apostado {dict_jugadores[jugador]["apuesta"]} puntos.'
                              f'Carta inicial: {dict_jugadores[jugador]["cartas"][0][0]} de '
                              f'{dict_jugadores[jugador]["cartas"][0][1]}. '
                              f'Valor mano {dict_jugadores[jugador]["cartas"][0][2]} puntos\n')

                    elif dict_jugadores[jugador]["tipo"] == 'humano':
                        dict_jugadores[jugador]["apuesta"] = input(f'{jugador},¿Cuánto vas a apostar? '
                                                                   f'Carta inicial: {dict_jugadores[jugador]["cartas"][0][0]} '
                                                                   f'de {dict_jugadores[jugador]["cartas"][0][1]} '
                                                                   f'({dict_jugadores[jugador]["cartas"][0][2]} puntos)\n')
                        while not dict_jugadores[jugador]["apuesta"].isdecimal() or \
                                int(dict_jugadores[jugador]["apuesta"]) > dict_jugadores[jugador]["puntos_restantes"]:
                            dict_jugadores[jugador]["apuesta"] = input(
                                f'Apuesta incorrecta. No puede ser superior a tus puntos restantes'
                                f'({dict_jugadores[jugador]["puntos_restantes"]})\n'
                                f'{jugador},¿Cuánto vas a apostar? '
                                f'Carta inicial: {dict_jugadores[jugador]["cartas"][0][0]} de '
                                f'{dict_jugadores[jugador]["cartas"][0][1]} '
                                f'({dict_jugadores[jugador]["cartas"][0][2]} puntos)\n')
                        dict_jugadores[jugador]["apuesta"] = int(
                            dict_jugadores[jugador]["apuesta"])  # Convertimos el input a int
                        print(f'apuesta de {jugador}: {dict_jugadores[jugador]["apuesta"]}\n')

            # Se pide accion

            accion = ''
            while accion not in ['1', '2', '3']:
                if dict_jugadores[jugador]["tipo"] == 'bot':
                    input(f'Juega {jugador}.\nPresiona "Enter" ver la accion del bot.')
                    # accion = ''
                    accion = funciones.algoritmo_decision_bot(dict_jugadores, jugador, orden_jugadores, mazo)

                elif dict_jugadores[jugador]["tipo"] == 'humano':
                    accion = input(f'{jugador}, Escoge acción:\n'
                                   '1) Robar carta\n'
                                   '2) Pasar\n'
                                   '3) Ver Mesa\n')
                if accion == '1':
                    accion = ''
                    carta_rand = random.randint(0, len(mazo) - 1)
                    carta = mazo.pop(carta_rand)
                    dict_jugadores[jugador]['cartas'].append(carta)
                    dict_jugadores[jugador]['puntos_mano'] += carta[2]
                    print(f'{jugador} roba {carta[0]} de {carta[1]}\n'
                          f'\nCartas en la mano:')

                    for carta in dict_jugadores[jugador]['cartas']:
                        print(f'{carta[0]} de {carta[1]}')
                    if dict_jugadores[jugador]["puntos_mano"] == 7.5:
                        print('Tienes 7yMedio!!\n')
                    elif dict_jugadores[jugador]["puntos_mano"] > 7.5:
                        dict_jugadores[jugador]['mano'] = 'eliminado'
                        print(
                            f'¡Que pena! {jugador} se ha pasado con {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
                        break
                    else:
                        print(f'\n{jugador} tiene {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
                elif accion == '2':
                    print(f'{jugador} se ha plantado con {dict_jugadores[jugador]["puntos_mano"]} puntos.\n')
                    break
                elif accion == '3':
                    funciones.ver_mesa(orden_jugadores, dict_jugadores)
                    accion = ''
                else:
                    print('opcion incorrecta\n')

        funciones.ver_mesa(orden_jugadores, dict_jugadores)
        # loop Banca

        # Comprobamos si queda ALGÚN jugador en juego. Si no es asi la banca no juega y cobra.

        banca_gana_automaticamente = True  # Establecemos el flag en TRUE para que camie a FALSE en el momento que salga un solo jugador que sigue en partida
        for jugador in orden_jugadores[1::]:  # Loop para comprobar el estado de los jugadores
            if dict_jugadores[jugador]['partida'] == 'eliminado':  # Si el jugador no esta en juego, no cambia nada
                continue
            elif dict_jugadores[jugador]['mano'] == 'jugando':
                banca_gana_automaticamente = False  # Si el jugador está en juego, se camba el flag y la banca jugará este turno

        if banca_gana_automaticamente is True:
            print('Todos los Jugadores se han pasado, la Banca gana automaticamente')
            for jugador in orden_jugadores[1::]:
                dict_jugadores[orden_jugadores[0]]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]
                dict_jugadores[jugador]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]


        # Si quedan jugadores la banca juga:

        elif banca_gana_automaticamente is False:
            print(f'Es el turno de la banca({orden_jugadores[0]})\n'
                  f'\nJugadores que siguen en juego:')
            for jugador in orden_jugadores[1::]:  # Loop para comprobar el estado de los jugadores
                if dict_jugadores[jugador][
                    'partida'] == 'eliminado':  # Si el jugador no esta en juego, no cambia nada
                    continue
                elif dict_jugadores[jugador][
                    'mano'] == 'jugando':  # Si un jugador estra en juego damos la informacion.
                    print(f'-{jugador} sigue en juego con {dict_jugadores[jugador]["puntos_mano"]} puntos.')

            # La banca escoge accion

            accion = ''
            while accion not in ['1', '2', '3']:
                if dict_jugadores[orden_jugadores[0]]["tipo"] == 'humano':
                    accion = input(f'{orden_jugadores[0]}, Escoge acción:\n'
                                   '1) Robar carta\n'
                                   '2) Pasar\n'
                                   '3) Ver Mesa\n')
                elif dict_jugadores[orden_jugadores[0]]["tipo"] == 'bot':
                    input(f'Juega la Banca ({orden_jugadores[0]}).\nPresiona "Enter" ver la accion del bot')
                    probabilidad_exito, control_ganancias = funciones.control_ganancias_banca(dict_jugadores, orden_jugadores, mazo)
                    accion = funciones.accion_banca_bot(probabilidad_exito, control_ganancias, dict_jugadores, orden_jugadores)



                if accion == '1':
                    accion = ''
                    carta_rand = random.randint(0, len(mazo) - 1)
                    carta = mazo.pop(carta_rand)
                    dict_jugadores[orden_jugadores[0]]['cartas'].append(carta)
                    dict_jugadores[orden_jugadores[0]]['puntos_mano'] += carta[2]
                    print(f'La Banca({orden_jugadores[0]}) roba {carta[0]} de {carta[1]}\n'
                          f'\nCartas en la mano:\n')

                    for carta in dict_jugadores[orden_jugadores[0]]['cartas']:
                        print(f'{carta[0]} de {carta[1]}')
                    print(
                        f'\nLa banca ({orden_jugadores[0]}) tiene {dict_jugadores[orden_jugadores[0]]["puntos_mano"]} puntos.')

                    if dict_jugadores[orden_jugadores[0]]["puntos_mano"] == 7.5:
                        banca_gana_automaticamente = True
                    elif dict_jugadores[orden_jugadores[0]]["puntos_mano"] > 7.5:
                        dict_jugadores[orden_jugadores[0]]['mano'] = 'eliminado'
                        print(
                            f'la banca ({orden_jugadores[0]}) se ha pasado con {dict_jugadores[orden_jugadores[0]]["puntos_mano"]} puntos.')
                        break
                elif accion == '2':
                    print(
                        f'La banca ({orden_jugadores[0]}) se ha plantado con {dict_jugadores[orden_jugadores[0]]["puntos_mano"]} puntos.')
                    break
                elif accion == '3':
                    funciones.ver_mesa(orden_jugadores, dict_jugadores)
                    accion = ''
                else:
                    print('opcion incorrecta\n')

        funciones.ver_mesa(orden_jugadores, dict_jugadores)
        # Comprobaciones ------------------------------------------
        for jugador in orden_jugadores[1::]:
            if (dict_jugadores[orden_jugadores[0]]['puntos_mano'] >= dict_jugadores[jugador]['puntos_mano'] or (
                    dict_jugadores[jugador]['mano'] == 'eliminado' and banca_gana_automaticamente is False)) and \
                    dict_jugadores[orden_jugadores[0]]['mano'] != 'eliminado':

                dict_jugadores[orden_jugadores[0]]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]
                dict_jugadores[jugador]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]

        # Luego se realiza otro bucle para los pagos de la banca a los jugadores, contando ahora la banca con todos los
        # puntos que podria tener.

        for jugador in orden_jugadores[1::]:
            if (dict_jugadores[orden_jugadores[0]]['puntos_mano'] < dict_jugadores[jugador]['puntos_mano'] or
                dict_jugadores[orden_jugadores[0]]['mano'] == 'eliminado') and dict_jugadores[jugador][
                'mano'] != 'eliminado':

                if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                    if (dict_jugadores[jugador]["apuesta"] * 2) > dict_jugadores[orden_jugadores[0]][
                        "puntos_restantes"]:
                        resto_puntos_banca = dict_jugadores[orden_jugadores[0]]["puntos_restantes"]
                        dict_jugadores[orden_jugadores[0]]["puntos_restantes"] -= resto_puntos_banca
                        dict_jugadores[jugador]["puntos_restantes"] += resto_puntos_banca
                    else:
                        dict_jugadores[orden_jugadores[0]]["puntos_restantes"] -= (
                                dict_jugadores[jugador]["apuesta"] * 2)
                        dict_jugadores[jugador]["puntos_restantes"] += (dict_jugadores[jugador]["apuesta"] * 2)

                elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                    if dict_jugadores[jugador]["apuesta"] > dict_jugadores[orden_jugadores[0]]["puntos_restantes"]:
                        resto_puntos_banca = dict_jugadores[orden_jugadores[0]]["puntos_restantes"]
                        dict_jugadores[orden_jugadores[0]]["puntos_restantes"] -= resto_puntos_banca
                        dict_jugadores[jugador]["puntos_restantes"] += resto_puntos_banca
                    else:
                        dict_jugadores[orden_jugadores[0]]["puntos_restantes"] -= dict_jugadores[jugador]["apuesta"]
                        dict_jugadores[jugador]["puntos_restantes"] += dict_jugadores[jugador]["apuesta"]

        # Luego efectuamos los prints según el caso que se haya dado en la partida

        if dict_jugadores[orden_jugadores[0]]['mano'] == 'eliminado':
            for jugador in orden_jugadores[1::]:
                if dict_jugadores[jugador]['mano'] == 'jugando':
                    if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                        print(f'{jugador} ha sacado 7 y Medio, gana {dict_jugadores[jugador]["apuesta"] * 2} puntos de '
                              f'la banca')
                    elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                        print(f'{jugador} gana {dict_jugadores[jugador]["apuesta"]} puntos de la banca')
                elif dict_jugadores[jugador]['mano'] == 'eliminado':
                    print(f'{jugador} se habia pasado, pero como la banca también se ha pasado no pierde puntos.')
        elif dict_jugadores[orden_jugadores[0]]['mano'] == 'jugando':
            if dict_jugadores[orden_jugadores[0]]["puntos_mano"] == 7.5:
                print(f'¡La banca ({orden_jugadores[0]}) ha ganado a todos con 7 y Medio!')
                for jugador in orden_jugadores[1::]:
                    print(f'{jugador} pierde {dict_jugadores[jugador]["apuesta"]} puntos.')
            elif dict_jugadores[orden_jugadores[0]]["puntos_mano"] != 7.5:
                for jugador in orden_jugadores[1::]:
                    if dict_jugadores[jugador]['mano'] == 'eliminado':
                        print(f'{jugador} pierde {dict_jugadores[jugador]["apuesta"]} puntos.')
                    elif dict_jugadores[jugador]['mano'] != 'eliminado':
                        if dict_jugadores[orden_jugadores[0]]['puntos_mano'] >= dict_jugadores[jugador]['puntos_mano']:
                            print(f'{jugador} pierde {dict_jugadores[jugador]["apuesta"]} puntos.')
                        elif dict_jugadores[orden_jugadores[0]]['puntos_mano'] < dict_jugadores[jugador][
                            'puntos_mano']:
                            if dict_jugadores[jugador]['puntos_mano'] == 7.5:
                                print(
                                    f'{jugador} ha sacado 7 y Medio, gana {dict_jugadores[jugador]["apuesta"] * 2} '
                                    f'puntos de la banca')
                            elif dict_jugadores[jugador]['puntos_mano'] != 7.5:
                                print(f'{jugador} gana {dict_jugadores[jugador]["apuesta"]} puntos de la banca')

        print(f'La banca ahora tiene {dict_jugadores[orden_jugadores[0]]["puntos_restantes"]} puntos')

        for jugador in orden_jugadores:
            if dict_jugadores[jugador]['puntos_restantes'] <= 0:
                dict_jugadores[jugador]['partida'] = 'eliminado'
                if dict_jugadores[jugador]['prioridad'] == 0:
                    print(f'La banca ({jugador}) ha sido eliminada')
                else:
                    print(f'El jugador {jugador} ha sido eliminado')
            if dict_jugadores[jugador]['partida'] == 'eliminado':
                orden_jugadores.remove(jugador)
                dict_jugadores.pop(jugador)
        if len(orden_jugadores) == 1:
            print(f'¡Enhorabuena {orden_jugadores[0]}! Has eliminado a los demás jugadores ¡Eres el ganador!')
            game = False
            modo_juego = True
        if turno == int(dict_config['Num_Max_Rounds']):
            print(f'\nHa terminado la partida. Los jugadores se quedan con las siguietes puntuaciones:\n')
            lista_ganadores = []
            for jugador in orden_jugadores:
                resultado = (dict_jugadores[jugador]["puntos_restantes"], jugador)
                print(f'{jugador} tiene {dict_jugadores[jugador]["puntos_restantes"]} puntos')
                lista_ganadores.append(resultado)

            lista_ganadores.sort(reverse=True)
            print()
            print('PODIO'.center(50,'-'))
            for jugador in lista_ganadores:
                if jugador == lista_ganadores[0]:
                    print(f'Primer puesto:\t{jugador[1]} con {jugador[0]} puntos'.ljust(50))
                elif jugador == lista_ganadores[1]:
                    print(f'Segundo puesto:\t{jugador[1]} con {jugador[0]} puntos'.ljust(50))
                elif jugador == lista_ganadores[2]:
                    print(f'Tercer puesto:\t{jugador[1]} con {jugador[0]} puntos'.ljust(50))
            if len(lista_ganadores) > 3:
                print('Resto de supervivientes'.center(50,'-'))
                puesto = 4
                for jugador in lista_ganadores[3::]:
                    print(f'Puesto {puesto}: \t{jugador[1]} con {jugador[0]} puntos'.ljust(50))
                    puesto += 1
            game = False
            modo_juego = True


        if turno < 30:

            funciones.cambio_banca(orden_jugadores, dict_jugadores)
            for jugador in orden_jugadores:
                funciones.jugador_turno_reset(orden_jugadores, dict_jugadores)
            mazo = list(mazo_juego)

        if turno >= 30:
            input()
            print('\n\n\n')
            funciones.creditos()










