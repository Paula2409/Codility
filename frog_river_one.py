def solution(X, A):
    # Initialize list B
    B = []
    # Iterate list B for append values
    for x in range(X+1):
        B.append(0)
    # Initialize variable and first position of the list B
    position = 0
    B[0] = 1
    # Iterate values list A for evaluate if there is a leaf
    for k in range(len(A)):
        position = A[k]
        B[position] = 1    
        if len(set(B)) == 1:
            return k
    # If the frog doesn't get to the other side
    return -1
