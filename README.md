# Busqueda-Binaria

Practicando y aprendiendo Python con ejercicios. Nivel `Beginner/Principiante`.




**Explicacion del algoritmo**

~~~
Condicion = La lista debe estar ordenada de forma ascendente
Tecnica = Recursion o recursiva
lista = [1, 3, 5, 10, 12]
Limite inferior -> 0 Limite superior -> 4
punto_medio = (0 + 4) // 2 = 4 // 2 = 2 (indice)
punto_medio = 5 
~~~

*Explicacion linea 36 en adelante*

Al buscar el `punto medio` estamos buscando si el elemento **objetivo** es `mayor` o `menor`, por ende terminamos descartando la otra mitad de la lista. Luego, se toma de partida el `punto medio` para continuar buscando el **objetivo.** 