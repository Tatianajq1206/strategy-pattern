def pass_graph(aristas: list) -> list:
    #Esta función duplica cada arista en la lista de aristas, invirtiendo el orden del nodo de inicio y fin.
    #Por ejemplo, si se recibe una arista (a, b, peso), la función devuelve tanto esa arista como la arista 
    #invertida (b, a, peso).
    cambio = []
    for i in range(len(aristas)):
        aux = (aristas[i][1], aristas[i][0], aristas[i][2])
        cambio.append(aristas[i])
        cambio.append(aux)
    return cambio

#La siguiente funcion busca la arista con el menor peso, comparando la posicion [2], en una lista de aristas
def peso_menor(comparar):
    if len(comparar) == 0:
        return []
    edge = comparar[0]
    menor = edge[2]
    for i in range(1,len(comparar)):
        if comparar[i][2] < menor:
            edge = comparar[i]
            menor = comparar[i][2]
    return edge

#Esta función busca el camino más corto entre dos nodos en un grafo dado.
#Utiliza un algoritmo de búsqueda recursiva.
def camino_corto(aristas: list, start=int, end=int, path: list = [], original_star=None):

    comparar = []
    camino = []
    for i in range(len(aristas)):
        origen = aristas[i][0]
        destino = aristas[i][1]
        if origen == start and destino not in original_star:
            comparar.append(aristas[i])

    if not comparar:
        return [path]

    edge = peso_menor(comparar)
    next_start = edge[1]
    camino.append(edge)

    update_aristas = [arista for arista in aristas if arista not in comparar]

    new_call = camino_corto(update_aristas, next_start, end, path + [edge], original_star=original_star.union({start}))

    if new_call:
        camino += new_call

    return camino

#Esta función envuelve la función `find_shortest_path`, asegurando que los nodos de inicio y fin
#no sean iguales
def graph_algorithm(aristas: list, start=int, end=int):
    if start == end:
        raise ValueError("El nodo de inicio y el nodo final son iguales.")
    return camino_corto(aristas, start, end, original_star={start})

def main():
    aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
    cambio_grahp = pass_graph(aristas)

    try:
        caminos = graph_algorithm(cambio_grahp, 3, 0)
        print("Caminos encontrados:")
        for i, camino in enumerate(caminos):
            print(f"Camino {i + 1}: {camino}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
