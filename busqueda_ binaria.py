import random
import time

# Busqueda inocente, ingenua o naive search

def  busqueda_inocente(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1 


mi_lista = [1, 3, 5, 10, 12]
print(busqueda_inocente(mi_lista, 10))


# Condicion = La lista debe estar ordenada de forma ascendente
# Tecnica = Recursion o recursiva
# lista = [1, 3, 5, 10, 12]
# Limite inferior -> 0 Limite superior -> 4
# punto_medio = (0 + 4) // 2 = 4 // 2 = 2 (indice)
# punto_medio = 5

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # Inicio de la lista.
    if limite_superior is None:
        limite_superior = len(lista)-1 # Final de la lista.
        
    if limite_superior < limite_inferior:
        return -1
    
    
    punto_medio = (limite_inferior + limite_superior) // 2  # Divide entre 2 y trunca el resultado a un entero o INT    

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)
    
    
if __name__=='__main__':
    
    # Crear una lista ordenada con 10000 numeros aleatorios
    tamaño = 10000
    conjunto_inicial = set()
    
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        
    lista_ordenada = sorted(list(conjunto_inicial))
    
    # Medir el tiempo de busqueda inocente
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_inocente(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")
    
    
    # Medir el tiempo de busqueda binaria. 
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")