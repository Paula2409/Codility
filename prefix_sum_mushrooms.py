def prefix_sums(A):
    n = len(A) # largo array A
    P = [0] * (n + 1) # Crea un array con tantos elementos tenga el array A mas 1

    for k in range(1, (n+1)):
        P[k] = P[k - 1] + A[k - 1] # Agrega al array P la suma de los numeros en el array A

    return P

def count_total(P, x, y):
    return P[y+1] - P[x]

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result

pre = prefix_sums([2,3,7,5,1,3,9])
print(pre)

# count_ = count_total(pre, 1, 4)
# print(count_)

mushroom = mushrooms([2,3,7,5,1,3,9],4,6)
print(mushroom)



