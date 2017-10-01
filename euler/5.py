if __name__ == "__main__":
	def gcd(a, b):
		while b > 0:
			a, b = b, a % b
		return a

	def lcm(a, b):
		return a * b / gcd(a, b)
   
	lcmlast = 20
	for i in range(19, 1, -1):
		lcmlast = lcm(i, lcmlast)

	print(lcmlast)
		
