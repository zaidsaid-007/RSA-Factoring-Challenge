#!/usr/bin/python3
import sys
from math import isqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def factorize_rsa(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return n, 1

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            num = int(line)
            factor1, factor2 = factorize_rsa(num)
            print(f"{num}={factor1}*{factor2}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
