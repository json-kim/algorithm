# 백준 1934번 문제
# 최소 공배수

# 유클리드 호제법 사용

def getLCM(A, B):
    a, b = A, B
    
    while b != 0:
        a = a % b
        a, b = b, a
        
    gcd = a
    lcm = A * B // gcd 
    return lcm

import sys

T = int(sys.stdin.readline())
case = []

for _ in range(T):
    case.append(list(map(int, sys.stdin.readline().split())))

for c in case:
    print(getLCM(c[0], c[1]))
