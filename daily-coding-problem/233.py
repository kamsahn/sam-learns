"""
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""

def fib(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_list(n: int) -> int:
    store = [1, 2]
    if n == 1:
        return store[0]
    while len(store) < n:
        store.append(store[-1] + store[-2])
    return store[-1]


def fib_constant(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(2, n):
            temp = b + a
            a = b
            b = temp
        return b
        
if __name__ == "__main__":
    print("1st:", fib(1))
    print("2nd:", fib(2))
    print("3rd:", fib(3))
    print("4th:", fib(4))
    print("5th:", fib(5))
    print("6th:", fib(6))
    print("7th:", fib(7))
    
    print("1st:", fib_list(1))
    print("2nd:", fib_list(2))
    print("3rd:", fib_list(3))
    print("4th:", fib_list(4))
    print("5th:", fib_list(5))
    print("6th:", fib_list(6))
    print("7th:", fib_list(7))
    
    print("1st:", fib_constant(1))
    print("2nd:", fib_constant(2))
    print("3rd:", fib_constant(3))
    print("4th:", fib_constant(4))
    print("5th:", fib_constant(5))
    print("6th:", fib_constant(6))
    print("7th:", fib_constant(7))
