
-- 1 Mostrar la Carta inicial más repetida por cada jugador(mostrar nombre jugador y carta). 
SELECT usr.username AS 'Nombre Usuario',
	IFNULL((SELECT t.carta_inicial
	FROM
		turnos t,
		participante p,
		jugador j,
		usuario u
	WHERE
		u.idusuario = j.idusuario AND
		p.id_jugador = j.idjugador AND
		p.id_participante = t.idparticipante AND
		u.idusuario = usr.idusuario
	GROUP BY t.carta_inicial, j.idusuario
	ORDER BY COUNT(*) DESC
	LIMIT 1), 'No ha jugado') AS 'Carta inicial más repetida'
FROM usuario usr
ORDER BY usr.idusuario;


-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador)
SELECT prt.idpartida AS Partida, 
	(SELECT u.username
	FROM
		turnos t,
		partida pr,
		participante p,
		jugador j,
		usuario u
	WHERE
		u.idusuario = j.idusuario AND
		p.id_jugador = j.idjugador AND
		t.idparticipante = p.id_participante AND
		pr.idpartida = t.idpartida AND
		pr.idpartida = prt.idpartida
		GROUP BY t.idpartida, j.idusuario
		ORDER BY MAX(t.apuesta) DESC
		LIMIT 1) AS 'Apuesta más alta'
FROM
    partida prt
ORDER BY
	prt.idpartida;
	
    
-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador)
SELECT prt.idpartida AS Partida, 
	(SELECT u.username
	FROM
		turnos t,
		partida pr,
		participante p,
		jugador j,
		usuario u
	WHERE
		u.idusuario = j.idusuario AND
		p.id_jugador = j.idjugador AND
		t.idparticipante = p.id_participante AND
		pr.idpartida = t.idpartida AND
		pr.idpartida = prt.idpartida
		GROUP BY t.idpartida, j.idusuario
		ORDER BY MAX(t.apuesta)
		LIMIT 1) AS 'Apuesta más baja'
	FROM
		partida prt
	ORDER BY
		prt.idpartida;


-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna "porcentaje %"
SELECT u.username AS 'Nombre Usuario', pr.nombre_sala AS 'Nombre Sala', 
	IFNULL((
				SELECT CONCAT(ROUND((SUM(g.ganado) / COUNT(g.ganado)) * 100, 2), '%') AS porcentaje
				FROM (
					SELECT (t.puntos_inicio - t.puntos_final) >= 0 AS ganado
					FROM turnos t
					WHERE t.idpartida = pr.idpartida AND t.idparticipante = p.id_participante
				) g
			), 'Incongruencia') AS Porcentaje
FROM 
	partida pr,
    participante p,
    jugador j,
    usuario u
WHERE
	pr.idpartida = p.id_partida AND
    p.id_jugador = j.idjugador AND
    j.idusuario = u.idusuario;


-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna "porcentaje %"
SELECT CONCAT(ROUND((COUNT(j.idbot)/COUNT(pt.idpartida))*100, 2),  '%') AS 'Porcentaje'
FROM
	participante p,
    partida pt,
    jugador j
WHERE
	p.id_jugador = j.idjugador AND
    pt.ganador_partida = p.id_participante;
    
	
-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.
-- OMITIDA
	
    
-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.
SELECT t.idpartida AS Partida, tc.descripcion AS Palo, count(tipo) AS Rondas
FROM
	turnos t,
    cartas c,
    tipo_carta tc
WHERE
	c.idcartas = t.carta_inicial AND
    tc.idtipo_carta = c.tipo AND
    t.puntos_final > t.puntos_inicio
	GROUP BY  tc.idtipo_carta, t.idpartida
    ORDER BY t.idturnos;


-- 8 Cuantas rondas gana la banca en cada partida.
SELECT idpartida as Partida, count(*) AS 'Rondas Ganadas'
FROM
	turnos
WHERE
	puntos_final > puntos_inicio AND
    es_banca = 1
    GROUP BY idpartida;
    
    
-- 9 Cuántos usuarios han sido la banca en una partida.
SELECT t.idpartida AS Partida, COUNT(DISTINCT j.idjugador) AS Usuarios
FROM 
	usuario u,
    jugador j,
    participante p,
    turnos t
WHERE
	j.idusuario = u.idusuario AND
    p.id_jugador = j.idjugador AND
    t.idparticipante = p.id_participante AND
    es_banca = 1
    GROUP BY t.idpartida;
	
    
-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.
-- OMITIDA


-- 11 Calcular la apuesta media por partida.
SELECT idpartida AS Partida, ROUND(AVG(apuesta)) AS 'Apuesta Media'
FROM
	turnos
    GROUP BY idpartida;


-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.
SELECT u.idusuario AS 'ID Usuario', u.username AS 'Nombre Usuario', t.idpartida AS Partida, IFNULL(t.apuesta, 0) AS 'Última Apuesta'
FROM
	turnos t,
    participante p,
    jugador j,
    usuario u
WHERE
	j.idusuario = u.idusuario AND
    p.id_jugador = j.idjugador AND
    t.idparticipante = p.id_participante
    GROUP BY idpartida, u.idusuario
    ORDER BY idpartida, numero_turno DESC;
    
    
-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.
SELECT t.idpartida AS Partida, COUNT(*) AS Cartas, SUM(valor) AS 'Valor Total'
FROM
	turnos t,
    cartas c
WHERE
	t.carta_inicial = c.idcartas
    GROUP BY t.idpartida
    ORDER BY t.idturnos;


-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.
-- OMITIDA