#Esta función es que organiza la lista de aristas del grafo en donde organiza las tuplas por peso
def sort_graph(aristas: list) -> list:
    '''En esta función es bastante tarda, ya que en el proceso de organizar las tuplas por peso, el codigo es ineficiente, ya que
    utiliza la lista original para comparar el peso, y para ello tiene que recorrer la lista aristas repetidas ocaciones, y al retornar
    sort_graph(left) + [aristas[middle]] + sort_graph(right) --> left=[] + [aristas[middle]] + right = [Lista con las tuplas - la que 
    se usa para comparar], al repetir este proceso, nos dimos cuenta que siempre retorna una de las sublistas como una lista vacia, lo 
    que relentiza el proceso de organizar las tuplas
'''
    if len(aristas) <= 1:
        return aristas
    
    middle = len(aristas) // 2 #Divivede la lista de aristas en dos, y calcula la tuple del medio de la lista inicil

    left = [x for x in aristas if aristas[middle][2] > x[2]] #En la sub lista  izquierda vamos a tener las tuplas que sean 
    #menores que el peso de la arista de middle
    right = [x for x in aristas if aristas[middle][2] < x[2]]#En la sub lista derecha vamos a tener las tuplas que sean 
    #mayores que el peso de la arista de middle

    return sort_graph(left) + [aristas[middle]] + sort_graph(right) #Retorna las sublistas y la tupla de en medio y las une

#Esta funcion utiliza busqueda binaria recursica para encontrar el objetivo dentro de la lista de aristas
def search_objetive(aristas:list, target: int, start = 0, end = 0) -> int:
    ''' En esta parte del codigo se compara el indice de en medio, con el objetivo para comprobar si se encontro en alguno de los casos
    que se dieron como opción, sin embargo, el indice lo calcula con la lista inicial de tuplas, la cual no esta organizada.
    A pesar de ser eficiente, la recusrion en esta funcion no tiene un limite, por otro lado, otro de los problemas, es que si el 
    objetivo no esta en la lista divide la lista hasta que start >= end, lo que hace muy largo este proceso
    '''
    if start == 0 and end == 0:
        end = len(aristas)

    #Si el inicio es mayor o igual al final, retorna -1(ya que no se encontro el objetivo)
    if start >= end:
        return -1

    middle = (start + end) // 2 #Se esta calculando el indice de en medio 
    #Si el indice de en medio es = al objetivo retorna el indice, indicando que se encontro
    if aristas[middle][1] == target:
        return middle
    #Por otro lado, si el indice es mayor al objetivo, busca en la lista izquierda
    elif aristas[middle][1] > target:
        return search_objetive(aristas, target, start, middle)
    #Por otro lado, si el indice es menor al objetivo, busca en la lista derecha
    elif aristas[middle][1] < target:
        return search_objetive(aristas, target, middle + 1, end)

#Esta funciín esta buscando la ruta mas facil entre el nodo objetivo y el nodo de inicio
def bad_graph_algorithm(aristas:list, start_node: int, objetive_node: int) -> list:
    '''Debido a que esta funcion se conecta con la funcion search se tiene el mismo problema, y es que la 
    recursividad es infinita, por otro lado, esta función no esta evaluando todos los casos posibles, si no 
    que evalua solo una ruta, sin comprara las demas y poder eleguir el mejor camino
    Cabe destacar, que todo el proceso se sigue haciendo como la lista inicial de tuplas sin organizar
    otro de los conflictos que se encontraron en el codigo, es que se esta comparando el nodo inicio con
    el nodo objetivo, lo que hace que el codigo lance un error, porque no se esta utilizando uan buena 
    practica de programación
    '''
    #Busca la tupla que tenga el valor del nodo objetivo
    objetive = search_objetive(aristas, objetive_node)

    #Retorna un lista vacia, en el caso de no encontrar el nodo objetivo
    if objetive == -1:
        return []

    #Si  el nodo objetivo fue encontrado, la devuleve a una lista
    if (aristas[objetive][0] == start_node):
        return [aristas[objetive]] #Almacena las tuplas que se encontraron utiles para la mejor ruta
    
    # llama a la funcion bad_graph_algorithm utilizando el primer elemento de la arista como el nuevo nodo objetivo
    # y concecta la arista actual a la lista resultante
    return  bad_graph_algorithm(aristas, start_node, aristas[objetive][0]) + [aristas[objetive]] 


def main():
    ''' En esta funcion se establecen las entradas del programa
    Al jugar un poco con el nodo de inicio y el nodo final, nos damos cuenta que el codigo esta asumiendo que 
    se debe trabajar con un grafo diriguido, lo que hace que no contemple todas las opciones en caso, de querer
    ir del final del nodo, al inicio del nodo
    Tambien se esta llamando a la funcion sort_graph, pero no se esta utilizando en ningun lado, por lo que
    organizar la lista inicial por  pesos no afectaria el resultado

    El codigo apesar de encontrar una posible solucion ante la ruta que podria tomar para llegar del nodo 0 al nodo 3, 
    no contempla posibles exepciones como si, el nodo inicial es igual al nodo destino, otra cosa de la que nos pudimos
    dar cuenta, es que no esta usando el peso de las aristas como herramienta para llegar mas facil y rapido al nodo destino
    '''
    aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
    aristas_ordenadas_por_peso = sort_graph(aristas)

    path = bad_graph_algorithm(aristas, 0, 3)

    print(path)
    


if __name__ == "__main__":
    main()