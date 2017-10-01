if __name__ == "__main__":
	a, b, c, sum = 1, 1, 0, 0
	while (a + b < 4000000):
		c = a + b
		if c % 2 == 0:
			sum += c
		a, b = b, c
	print(sum)
