"""

Se le dan N contadores, inicialmente establecidos en 0, y tiene dos posibles operaciones en ellos:

aumentar(X) − el contador X se incrementa en 1,
contador máximo : todos los contadores se establecen en el valor máximo de cualquier contador.
Se da una matriz no vacía A de M enteros. Esta matriz representa operaciones consecutivas:

si A[K] = X, tal que 1 ≤ X ≤ N, entonces la operación K es aumentar(X),
si A[K] = N + 1, entonces la operación K es el contador máximo.
Por ejemplo, dado el entero N = 5 y la matriz A tal que:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
los valores de los contadores después de cada operación consecutiva serán:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
El objetivo es calcular el valor de cada contador después de todas las operaciones.

Escribe una función:

def solución(N, A)

que, dado un número entero N y una matriz A no vacía que consta de M números enteros, devuelve una secuencia de números enteros que representan los valores de los contadores.

La matriz de resultados debe devolverse como una matriz de enteros.

Por ejemplo, dado:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
la función debería devolver [3, 2, 2, 4, 2], como se explicó anteriormente.

Escriba un algoritmo eficiente para las siguientes suposiciones:

N y M son números enteros dentro del rango [ 1 .. 100,000 ];
cada elemento de la matriz A es un número entero dentro del rango [ 1 .. N + 1 ]."""


def solution(N,A):
    counters = []

    for i in range(N):
        counters.append(0)

    for value in A:
        if 1 <= value <= N:
            counters[value-1] += 1
        elif value == (N + 1):
            max_counter = max(counters)
            counters = []
            x = 0
            while x <= N:
                counters.append(max_counter)
                x += 1

    print(counters)

solution(5, [3,4,4,6,1,4,4])