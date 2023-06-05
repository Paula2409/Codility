def solution(N):
	N = str(bin(N)).replace("0b","")
	list_max = []
	
	count = 0
	for i in N:
		if i == "0":
			count += 1
		if i == "1":
			list_max.append(count)
			count = 0

			
	if max(list_max) > 0:
		return max(list_max)
	else:
		return 0
