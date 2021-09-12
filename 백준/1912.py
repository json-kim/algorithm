# 백준 1912번 문제
# 연속합 (동적 계획법)

# 수열에서 연속된 숫자들의 합의 최댓값을 구하는 문제
# 길이가 n인 수열의 최댓값은 길이가 n-1인 수열에서 n번째 숫자를 추가했을 때를 고려하여 구한다.
# 이 때 구하는 값은 n번째 숫자를 포함한 연속된 수열의 최댓값을 구하여 저장한다.
# 그리고 연속된 수열이어야 하기 때문에 n-1을 포함한 연속 수열의 최댓값을 비교해보면 된다.

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

maxSum = [0] * n
maxSum[0] = arr[0]

for i in range(1, n):
    if maxSum[i-1] < 0:
        maxSum[i] = arr[i]
    else:
        maxSum[i] = maxSum[i-1] + arr[i]

print(max(maxSum))
