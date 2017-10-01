if __name__ == "__main__":
	largest = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			if str(i * j) == str(i * j)[::-1]:
				if (i * j) > largest:
					largest = i * j

	print(largest)
