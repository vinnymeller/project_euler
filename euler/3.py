import math

if __name__ == "__main__":
	solution = 0
	num = 600851475143
	maxx = math.ceil(math.sqrt(num))
	primearr = [2]
	for i in range(3, maxx, 2):
		if solution != 0:
			break
		isprime = True
		for numm in primearr:
			if i % numm == 0:
				isprime = False
				break
		if isprime:
			primearr.append(i)
			while num % i == 0:
				num = num / i
				if num == 1:
					solution = i			
	print(solution)
	
