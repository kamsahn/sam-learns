"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N,
the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""


def sieve_of_eratosthenes(n: int) -> list[int]:
    prime = 2
    i = 2
    
    ans = [j for j in range(prime, n)]
    non_prime = []
    while n / 2 > prime:
        while prime * i < n:
            non_prime.append(prime * i)
            i += 1
        
        ans = [item for item in ans if item not in non_prime]
        
        # reset
        i = 2
        non_prime = []
        prime = min([k for k in ans if k > prime])
    
    return ans
        

if __name__ == "__main__":
    print(sieve_of_eratosthenes(100))

        
    