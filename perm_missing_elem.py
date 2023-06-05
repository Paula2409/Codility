def solution(A):
    # Ordenamos la lista para facilitar busqueda
    A.sort()
    result = 1
    for i in A:
        if i > result:
            return result
        result += 1
    # Si no encontramos el numero, el faltante es la variable result
    return result     


print(solution([1,8,9,4,6,5,10,20,3]))
