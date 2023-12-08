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
                heappush(Queue, (distanciaAux, nodoVecino))

            if nodoVecino is nodoDestino:
                return {
                    k: v
                    for k, v in sorted(distancias.items(), key=lambda item: item[1])
                    if v is not math.inf
                }
    return "No hay solución"


g = {
    "A": {"B": 4, "C": 3, "D": 5},
    "B": {"A": 4, "D": 8},
    "C": {"A": 3, "D": 5},
    "D": {"B": 8, "A": 5},
}

g = {
    "A": {"F": 1, "D":5},
    "F": {"H": 1, "D": 15},
    "H":{},
    "D":{"B": 1, "C": 6},
    "B":{},
    "C":{}

}

nodes = ["F", "H", "D", "B", "C"]
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

print(g)
#vi = input()
#vi = list(vi.upper())[0]
#vf = input()
#vf = list(vf.upper())[0]

vi = nodes[randint(0, len(nodes)-1)]
vf = nodes[randint(0, len(nodes)-1)]

while(vi == vf):
    vf = nodes[randint(0, len(nodes)-1)]

print(vi)
print(vf)
"""
"""
print(Dijkstra(g, vi, vf))
