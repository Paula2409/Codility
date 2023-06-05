def solution(A):
  sum_second = 0
  sum_first = 0
  minimal_d = []
    
  for i in range((len(A))-1):
      for j in range(i+1,len(A)):
          sum_second = A[j] + sum_second

      sum_first = A[i] + sum_first
      minimal_difference = abs(sum_first - sum_second)
      minimal_d.append(minimal_difference)
      sum_second = 0
  return min(minimal_d)
