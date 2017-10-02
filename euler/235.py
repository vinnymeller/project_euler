from decimal import Decimal, getcontext


def uk(r, k):
	return (Decimal(900)-Decimal(3)*Decimal(k))*(r**(Decimal(k)-Decimal(1)))

if __name__ == "__main__":

	getcontext().prec = 100
	sum = Decimal(0)
	rval = Decimal(0)
	rvalmin = Decimal(-99)
	rvalmax = Decimal(100)
	for runs in range(100):
		sum = Decimal(0)
		rval = (rvalmax + rvalmin)/Decimal(2)
		for i in range(1, 5001):
			sum += uk(rval, i)
		if sum < Decimal(-600000000000):
			rvalmax = rval
		if sum > Decimal(-600000000000):
			rvalmin = rval	

	print(rval)
