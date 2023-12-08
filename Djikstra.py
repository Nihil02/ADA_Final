import math
from random import randint
from heapq import heappop, heappush


def Dijkstra(Grafo, nodoOrigen, nodoDestino):
    if not nodoOrigen in Grafo.keys() or not nodoDestino in Grafo.keys():
        return "El nodo no existe en el grafo"
    if nodoOrigen is nodoDestino:
        return "El nodo destino es el nodo de origen"

    distancias = {nodo: math.inf for nodo in Grafo}
    distancias[nodoOrigen] = 0
    Queue = [(0, nodoOrigen)]
    previos = {nodo: None for nodo in Grafo}

    while Queue:
        distanciaActual, nodoActual = heappop(Queue)

        if distanciaActual != distancias[nodoActual]:
            continue

        aux = {
            k: v for k, v in sorted(Grafo[nodoActual].items(), key=lambda item: item[1])
        }

        for nodoVecino, distancia in aux.items():
            distanciaAux = distancias[nodoActual] + distancia
            if distanciaAux < distancias[nodoVecino]:
                distancias[nodoVecino] = distanciaAux
                previos[nodoVecino] = nodoActual
                heappush(Queue, (distanciaAux, nodoVecino))

    if distancias[nodoDestino] == math.inf:
        return "No hay solución"
    else:
        inclusion = []
        nodoActual = nodoDestino
        while nodoActual is not None:
            inclusion.append(nodoActual)
            nodoActual = previos[nodoActual]
        return {x: distancias[x] for x in distancias if x in inclusion}


g = {
    "A": {"B": 1, "C": 3, "D": 5},
    "B": {"A": 4, "D": 1},
    "C": {"A": 3, "D": 5},
    "D": {"B": 1, "A": 5},
}

vi = "A"
vf = "D"

"""
nodes = ["A", "H", "D", "B", "C"]
n = 3
g_ran = dict()

for i in range(n):
    aux_dict = dict()
    for j in range(n):
        key = chr(ord("@") + j + 1)
        if i == j:
            aux_dict[key] = 0
        else:
            aux_dict[key] = randint(-1, 4)
    aux_dict = {k: v for k, v in aux_dict.items() if v > 0}
    g_ran[chr(ord("@") + i + 1)] = aux_dict

vi = input()
vi = list(vi.upper())[0]
vf = input()
vf = list(vf.upper())[0]

vi = nodes[randint(0, len(nodes)-1)]
vf = nodes[randint(0, len(nodes)-1)]


while(vi == vf):
    vf = nodes[randint(0, len(nodes)-1)]
"""
print(g)
print(vi)
print(vf)
print(Dijkstra(g, vi, vf))
