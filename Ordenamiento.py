def burbuja(datos):
    size = len(datos)-1 #Mira toda la lista -1 p el ultimo dato no tiene con que comprarlo
    for i in range (0, size): #Bucle para evaluar cuantas veces se tiene que recorer la lista
        print(f"# De pasadas {i + 1}")
        for j in range (0, size): # Bucle para comparar los valores e intercambiarlos 
            print (f"Comparaciones {datos[j]} > {datos[j+1]}")
            if datos [j] > datos[j+1]:
                print(f"Que numeros intercambia para organizar la lista: {datos[j]} y {datos[j+1]} ")
                aux = datos[j] #Almacenamos el dato que se esta intercambiando para no perderlo
                datos[j] = datos[j+1] # Remplazamos el dato que se comprar por el que se esta intercambiando 
                datos [j+1] = aux
    return datos



def seleccion(datos):
    size = len(datos)-1

    for i in range (0,size):
        min_index = i #Mantiene la posicion de valor minimo 
        min_value = datos[min_index] #Almacena el valor que hay en datos en la posicion min_index
        print(f"Pasadas {i+1}")

        for j in range (i, size): # comenzamos a comprar desde el indice en el que estamos
            print(f"comprar {min_value}> {datos[j+1]}")
            if min_value > datos [j+1]:
                min_value = datos [j+1]
                min_index = j+1
        
        if min_index != 1:
            aux = datos[i]
            datos[i]= datos[min_index]
            datos [min_index] = aux
    return datos


def insercion(datos):
    size = len(datos)

    for i in range (1,size):
        #print (f"Pasadas {i-1}") ## PREGUNTAR PQ
        insert_value = datos[i] #Toma el siguiente valor a ser insertado
        insert_index = i #Indice donde se inserta el valor

        while insert_index > 0 and datos[insert_index -1 ] > insert_value:
            #Se mueve al frente hasta encontrar un lugar adecuado o hasta el principio de la lista
            datos[insert_index] = datos[insert_index-1]
            insert_index -=1
        
        datos[insert_index] = insert_value #Insertamos el valor en su lugar correcto
    return datos


def shell(datos):
    size = len(datos)
    # Si el arreglo es impar usando (//) se puede hacer el inervalo entero para que se pueda manejar 
    intervalo = size // 2  

    while intervalo > 0 :
        print(f" __________Intervalo: {intervalo}__________")
        for i in range (intervalo, size):
            #print (f"Pasadas {i-1}") ## PREGUNTAR PQ
            # i esta iterando en funcion del intervalo
            insert_value = datos[i] #Toma el siguiente valor a ser insertado
            insert_index = i #Indice donde se inserta el valor

            print(f"comparación: {datos[insert_index - intervalo ]} > {insert_value}")
            while insert_index >= intervalo and datos[insert_index - intervalo ] > insert_value:
                #Se mueve al frente hasta encontrar un lugar adecuado o hasta el principio de la lista
                datos[insert_index] = datos[insert_index - intervalo]
                insert_index -= intervalo
            
            datos[insert_index] = insert_value #Insertamos el valor en su lugar correcto
        #Actualiza el intervalo
        intervalo //= 2
        return datos


def mergesort (datos):
    if len(datos) == 1: #Caso base para mirar si se puede seguir dividiendo el arreglo
        return [datos[0]]
    
    #Divide el arreglo en dos mitades 
    mitad = len(datos)//2
    izquierda = datos[:mitad]
    derecha = datos[:mitad]

    #Solucionar las dos mitadess de forma recursiva 
    sol_izquierda = mergesort(izquierda)
    sol_derecha = mergesort(derecha)

    return Merge (sol_izquierda, sol_derecha)

    def Merge (izquierda, derecha):
        resultado = []
        while len(izquierda) > 0 and len(derecha) > 0:
            if izquierda[0] <= derecha[0]:
                resultado.append(derecha.pop(0)) #CORREGUIR SI ALGO
            else:
                resultado.append(izquierda.pop(0))

        while len(izquierda) > 0:
            resultado.append(izquierda.pop(0))
        
        while len(derecha) > 0:
            resultado.append(derecha.pop(0))
        
        return resultado


"""def Rapido(datos, low, high):
    if low < high:
        pi = Particion(datos, low, high)

        Rapido(datos, low, pi - 1)
        Rapido(datos, pi + 1, high)
    def Particion(datos, low, high)
        pivot = datos[high] # pivotea el de la derecha
        i = low - 1          # indice izquiera del pivot    
        
        for j in range(low, high):
            if datos[j] <= pivote
            i += 1           # movemos el índice a la derecha
            datos[i], datos[j] = datos[j], datos[i]. # intercambiamos los elementos

        datos[i+1], datos[high] = datos[high], datos[i+1]
        return i+1
"""


lista=[70,90,0,80,60,85]
print(f"Este es el metodo de Burguja {burbuja(lista)} \n")
print(f"Este es el metodo de Selección {seleccion(lista)}\n")
print(f"Este es el metodo de Insercion {insercion(lista)}\n")
print(f"Este es el metodo de shell {shell(lista)}\n")
print(f"Este es el metodo Merge Sort {mergesort(lista)}\n")
#print(f"Este es el metodo Quick Sort {Rapido(Particion)}\n")






