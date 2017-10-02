def primesret(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [i for i in range(3,n,2) if sieve[i]]


def binsearch(n, arr):
        lessindex = 0
        moreindex = len(arr)-1
        while True:
                if moreindex < lessindex:
                        return False
                g = (lessindex + moreindex) // 2
                if arr[g] < n:
                        lessindex = g + 1
                elif arr[g] > n:
                        moreindex = g - 1
                else:
                        return True

def checklist(checklist, primelist):
	for p1 in checklist:
		for p2 in checklist:
			if p1 == p2:
				continue
			if binsearch(int(str(p1) + str(p2)), primelist) == False or binsearch(int(str(p2) + str(p1)), primelist) == False:
				return False
	return True


if __name__ == "__main__":

	primes = primesret(200000000)
	check = [0, 0]
	pairs = []
	for i in range(2000):
		check[0] = primes[i]
		for j in range(2000):
			if primes[i] >= primes[j]:
				continue
			check[1] = primes[j]
			if checklist(check, primes):
				pairs.append([primes[i], primes[j]])



	fivearr = [0, 0, 0, 0, 0]
	for i in range(len(pairs)):		
		fivearr[0] = pairs[i][0]
		fivearr[1] = pairs[i][1]
		for j in range(i+1, len(pairs)):
			if pairs[j][0] == fivearr[1]:
				fivearr[2] = pairs[j][1]
				if checklist([fivearr[0], fivearr[1], fivearr[2]], primes) == False:
					continue
			else:
				continue
			for k in range(j+1, len(pairs)):
				if pairs[k][0] == fivearr[2]:
					fivearr[3] = pairs[k][1]
					if checklist([fivearr[0], fivearr[1], fivearr[2], fivearr[3]], primes) == False:
						continue
				else:
					continue
				for p in range(k+1, len(pairs)):
					if pairs[p][0] == fivearr[3]:
						fivearr[4] = pairs[p][1]
						#print(fivearr)
						if checklist(fivearr, primes) == True:
							print(sum(fivearr))
						else:
							continue

			
			
