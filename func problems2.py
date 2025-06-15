#  1. Sum of Prime Numbers up to N Using Functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            total += i
    return total

print("Sum of primes up to 20:", sum_of_primes(20))  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

# 2. Sum of Odd Numbers up to N Using Function
def sum_of_odds(limit):
    total = 0
    for i in range(1, limit + 1, 2):
        total += i
    return total

print("Sum of odd numbers up to 10:", sum_of_odds(10))  # 1 + 3 + 5 + 7 + 9 = 25

