n = int(input())

def pibo(x):
	if (x == 0):
		return 0
	else:
		if (x < 3):
			return(1)
		else:
			return(pibo(x-1)+ pibo(x-2))
	
print(pibo(n))