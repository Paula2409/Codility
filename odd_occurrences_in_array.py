from collections import Counter
unpaired = set()
def solution(A):
    c = Counter(A)
    for key,value in c.items():
        if value % 2 != 0:
            unpaired.add(key)
    for j in unpaired:

        print(j,end=" ")

solution([1,3,5,7,7,7,3,1,9,11,11,9,7,1])
