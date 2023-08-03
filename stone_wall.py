def solution(H):
  A = []
  counter = 0

  for i in H:

    while len(A) != 0 and i < A[-1]:
      A.pop()
      counter += 1

    if len(A) == 0 or i > A[-1]:
      A.append(i)


  print(counter)
  counter += len(A)
  print(counter)

solution([8,8,5,7,9,8,7,4,8])
