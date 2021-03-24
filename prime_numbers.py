# Implementing methods from CTTI

# check if n is a prime number
# S1 check to see if sqrt(n) can be divided by any number up to it
def checkPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))):  #[1]
        if n%i == 0:
            return False
    return True
# [1] For n = a*b, if a<sqrt(n), then b>sqrt(n)
# e.g. n = 100, sqrt(n) = 10, if we checked a=5, then we don't need to check a=20.
# also note int(a) gives you the integer of the float number, doesn't do rounding.
# same behavior for both positives and negatives.
# compared to a//b, 2//3 = 1//3 = 0, -2//3=-1//3=-1

#S2 check to see if sqrt(n) can be divisble by a prime number 
# because all non-prime numbers can be divided by a prime number
def checkPrime2(n):
    if n<2:
        return False
    for prime in getPrime(int(math.sqrt(n))):
        if n%prime == 0:
            print(f'{n} is divisible by {prime}.')
            return False
    return True


# The Sieve of Eratosthene: get a list of primes up to n
import math
def getPrime(n):
    flags = [True]*(n+1)  # there are n+1 numbers from 0 to n
    flags[0] = flags[1] = False
    prime = 2
    while prime <= int(math.sqrt(n)):
        for i in range(prime*prime, n+1, prime): #[1]
            flags[i] = False
        for j in range(prime+1, n+1): #[2]
            if flags[j]:
                prime = j
                break
    return [num for num, flag in enumerate(flags) if flag] 

# [1] cross out all numbers in range(n+1) that are multiples of the current prime number
# starting from prime*prime because k*prime for k < prime has already been checked
# ending with n+1 so that n can be checked, also because when prime*prime==n, range(n,n+1) would make sure n is returned
# with every prime steps to check for multiples
# [2] move to the next prime number with flag being true
# starting from the next number to the current prime

if __name__ == "__main__":
    checkPrime(10)
    checkPrime2(10)
    getPrime(10)
    checkPrime2(77711)

