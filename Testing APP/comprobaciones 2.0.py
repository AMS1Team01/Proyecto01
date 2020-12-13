
'''
si todos los jugadores se han pasado banca no juega y gana
    bucle cobra todas las apuestas
si banca se pasa
    bucle comprobar si jugador juega
        si jugador juega la banca le paga
si no se han pasado juega
    si saca 7.5 gana a todos
        bucle cobra todas las apuestas
    si no saca 7.5 comparamos
        si jugador se ha pasado
            paga a la banca
        si jugador no se ha pasado
            si banca gana
                paga a la banca
            si banca no gana
                si jugador 7.5
                    paga doble al jugador
                si jugador no 7.5
                    paga al jugador

bucle jugadores
    si jugador tiene 0 puntos queda eliminado


'''



'''
si todos los jugadores estan eliminado banca gana
    bucle cobra las apuestas de los jugadores
si los jugadores no estan eliminados -> turno banca
    Bucle carta banca
    si puntos_mano de banca > 7.5
        bucle comprobar si jugador esta eliminado
            si jugador no está eliminado
                banca paga apuesta a jugador
                break
                reset de las variables
    si puntos_mano de banca = 7.5 banca gana
        bucle cobra las apuestas de los jugadores
    si puntos_mano de banca not 7.5 
        si jugador esta eliminado
            paga a la banca
        si jugador no esta eliminado
            si puntos_mano de banca > puntos_mano jugador
                apuesta del jugador paga a la banca
            si puntos_mano de banca < puntos_mano jugador
                si puntos_mano de jugador = 7.5
                    jugador gana apuesta*2
                si puntos_mano de jugador < 7.5 
                    jugador gana apuesta
   


'''