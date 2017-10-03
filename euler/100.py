from decimal import Decimal, getcontext
import math

ratioarr = [4684660, 27304197]
if __name__ == "__main__":
	sqrtt = Decimal(0.5).sqrt()
	i = math.floor((ratioarr[1]**2)/ratioarr[0])
	while 1 < 1000000000000000:
		blue = math.ceil(Decimal(i) * sqrtt)
		if (blue**2 - blue)/(Decimal(i)**2 - Decimal(i)) == Decimal(0.5):
			if i > 1000000000000:
				print(blue)
				break
			else:
				ratioarr[0], ratioarr[1] = ratioarr[1], i
				i = math.floor((ratioarr[1]**2)/ratioarr[0])
		else:
			i += 1		
