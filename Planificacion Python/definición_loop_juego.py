'''
-Inicialización del programa
-Comprobación de condiciones de programa
-Elección de modo de juego
'''

'''
-------------------Modo jugadores-------------------
- Pedir cuantos jugadores van a jugar
- Pedir usuarios para los jugadores o Crear usuario
- Cargar variables correspondientes al modo jugadores
'''

'''
--------------------Modo Bots-----------------------
- Escoger cuantos bots juegan
- ¿Generar bots o cargarlos de lista de bots?
- ( Opcional - Se podria elegir dificultad de bots, o que los diferentes bots existentes tengan diferente dificultad )
- Cargar variables correspondientes al modo bots
'''

'''
--------------------Loop de juego---------------------
- Inicializar el juego
- Incremento contador de turno
- Verificacion de condiciones para continuar el loop
- SOLO PRIMER TURNO: Se reparte una carta a cada jugador para establecer el orden y la banca 
- Se restablece el mazo
- Se reparten cartas a todos los jugadores, esas cartas se quitan del mazo y pasan a la mano del jugador
- Por orden - accion de apostar   
- Por orden - eleccion de accion, si roba, vueve a elegir y asi hasta pasar.
- Eliminacion de los jugadores que se hayan pasado de 7yMedio
- Si quedan jugadores que no se hayan pasado, juega la banca:
    - Recibe cartas
    - Decide accion, si roba, recibe otra carta hasta que se planta.
- Comprobaciones de puntos
- Resoluciones de apuestas
- Definicion ganador turno
- Comprobacion cambio de banca y comprobacion orden jugadores
- Reinicializacion de manos y baraja
- Eliminacion de jugadores sin puntos
- Comprobacion orden de jugadores



'''

'''--------------------------------Bucle de juego segun pdf detallado en pags. 8,9,10 del pdf-----------------------'''