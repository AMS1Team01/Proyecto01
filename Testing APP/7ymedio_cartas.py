
mazo = []

num_cartas = {'AS': 1, 'DOS': 2, 'TRES': 3, 'CUATRO': 4, 'CINCO': 5, 'SEIS': 6, 'SIETE': 7,
              'SOTA': 10, 'CABALLO': 11, 'REY': 12}
palo_cartas = ('OROS', 'COPAS', 'ESPADAS', 'BASTOS')

valor_cartas = {'AS': 1, 'DOS': 2, 'TRES': 3, 'CUATRO': 4, 'CINCO': 5, 'SEIS': 6, 'SIETE': 7,
              'SOTA': 0.5, 'CABALLO': 0.5, 'REY': 0.5}

OROS, COPAS, ESPADAS, BASTOS = 4, 3, 2, 1

for num in num_cartas:
    for palo in palo_cartas:
        mazo.append((num_cartas[num], palo, valor_cartas[num]))
print(mazo)


