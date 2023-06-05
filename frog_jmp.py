def solution(x,y,d):
    count = (y - x) // d
    # Chequeo si llegue:
    if x+count*d >= y:
      print(count)
    else:
      print(count+1)


solution(10,85,30)
