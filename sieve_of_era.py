import math

def prime_generator(n):
	# n is the number of digit we want the primes to be
	lowerbound = int(math.pow(10, n-1)+1)   #101
	upperbound = int(math.pow(10, n))       #1000
	primelist = sieve_of_era(lowerbound, upperbound)
	print primelist

def sieve_of_era(low, upp):
    prime = [True] * upp
    for i in xrange(3, int(upp**0.5)+1, 2): #ignore even numbers
    	if prime[i]:
    		prime[i*i::2*i] = [False]*((upp-i*i-1)/(2*i)+1) #deng cha shu lie

    toReturn = []
    # toReturn.append(2)
    for i in range(low, upp, 2):
        if prime[i] == True:
        	toReturn.append(i)
    
    return toReturn


def main():
	prime_generator(3)

if __name__ == '__main__':
	main()