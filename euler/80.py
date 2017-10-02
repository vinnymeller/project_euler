from decimal import Decimal, getcontext


if __name__ == "__main__":
	getcontext().prec = 104

	sum = 0
	for i in range(101):
		num = str(Decimal(i).sqrt())
		if len(num) > 50:
			parts = num.split(".")
			num = parts[0] + parts[1]
			for i in range(100):
				sum += int(num[i])
	print(sum)
