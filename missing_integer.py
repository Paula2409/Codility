"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]."""

def solution(A):

    A = sorted(list(set(A)))
    if max(A) < 0 or (1 not in A):
        print(1)

    # total = (len(A)*(len(A)+1))//2
    # print(total)

    # sum_a = sum(A)
    # print(sum_a)

    # if total == sum_a:
    #     print(len(A)+1)
    # else:
    #     print(max(A)-(sum_a-total))

    for i in range(len(A)-1):
        if A[i] > 0 and A[i+1]-A[i] > 1: #Chequear si hay diferencia mayor que 1 entre los numeros
            print(A[i]+1)
    return A[len(A)-1]+1
solution([1, 3, 6, 5, 1,4])