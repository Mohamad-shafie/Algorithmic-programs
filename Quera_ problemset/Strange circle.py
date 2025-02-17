# Question Link: https://quera.org/problemset/3540
import math

N_and_K = list(map(int, input().split(" ")))
n, k = N_and_K[0], N_and_K[1]

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print(int(lcm(n, k)/k))