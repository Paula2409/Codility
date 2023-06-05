def solution(A,K):
    
    if K < len(A):

        A = A[-K:] + A [:K]

    if K > len(A):

        I = K - len(A)

        A = A[(-K + I):] + A[:(-K + I)]

    return A
