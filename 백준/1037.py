# 백준 1037번 문제
# 약수

# 진짜 약수를 오름차순 정렬했을 때, 가장 작은 수와 가장 큰수의 곱이 찾는 수이다.
import sys

n = int(sys.stdin.readline())
factor = list(map(int, sys.stdin.readline().strip().split()))

result = max(factor) * min(factor)

print(result)