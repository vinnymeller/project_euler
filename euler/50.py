import math

#fast primes credit to some dude
def primesret(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def binsearch(n, arr):
	lessindex = 0
	moreindex = len(arr)-1
	while True:
		if moreindex < lessindex:
			return -1
		g = (lessindex + moreindex) // 2
		if arr[g] < n:
			lessindex = g + 1
		elif arr[g] > n:
			moreindex = g - 1
		else:
			return g

if __name__ == "__main__":
	primearr = primesret(1000000)

	is_consecutives = 0
	bigprime = 0
	for i in range(len(primearr)):
		if (i % 100 == 0):
			print(i)
			print(is_consecutives)
			print(bigprime)
		sum = primearr[i]
		consecutive = 1
		j = 0
		while sum < 1000000:
			j += 1
			if i + j > len(primearr)-1:
				continue
			sum += primearr[i + j]
			consecutive += 1
			if binsearch(sum, primearr) != -1:
				if consecutive > is_consecutives:
					is_consecutives = consecutive
					bigprime = sum

	print(is_consecutives)
	print(bigprime)
