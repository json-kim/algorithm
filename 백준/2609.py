# 백준 2609번 문제
# 최대공약수와 최소공배수

# 주어진 두 수의 최대공약수와 최소공배수를 구하는 문제
import sys
A, B = map(int, sys.stdin.readline().strip().split())

smaller = min(A, B)
bigger = max(A, B)

mostFactor = 1
leastMultiple = A*B

for i in range(smaller, 1, -1):
    if A % i == 0 and B % i == 0:
        mostFactor = i
        break
    
for i in range(1, smaller):
    if (bigger*i) % smaller == 0:
        leastMultiple = bigger*i
        break
    
print(mostFactor)
print(leastMultiple)