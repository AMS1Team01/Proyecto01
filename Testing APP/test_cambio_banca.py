lista = ['a', 'b', 'c']
dict_lista = {'a': {'puntos': 6, 'prioridad': 0}, 'b': {'puntos': 7.5, 'prioridad': 1}, 'c': {'puntos': 7.5, 'prioridad': 2}}

for jugador in lista:
    if dict_lista[jugador]['puntos'] == 7.5:
        aux = lista.pop(lista.index(jugador))
        lista.append(aux)
        lista[0], lista[len(lista)-1] = lista[len(lista)-1], lista[0]
        break
print(lista)
for jugador in lista:
    dict_lista[jugador]['prioridad'] = lista.index(jugador)
print(dict_lista)

# En esta funcion cambio la prioridad de los jugadores segun su orden en la lista, ya que es lo más practico.
# La prioridad se pone por requisito del ejercicio, pero hace la misma funcion que la lista de orden de jugadores, que
# es más sencilla de manipular.

# Es por eso que hay una segunda iteracion del código, para asignar la prioridad a los valores del diccionario del
# jugador, aunque es un aributo innecesario.

# Si es necesario, se puede modificar los valores en diccionario y ordenar de nuevo segun su prioridad, pero parece poco eficiente.