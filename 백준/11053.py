# 백준 11053번 문제
# 가장 긴 증가하는 부분 수열 (동적 계획법)

# 주어집 입력값들에서 가장 긴 증가하는 부분수열의 길이를 구한다.
# n번째 길이에서 해당 숫자를 포함하는 부분수열의 최대 길이를 저장한다.(마지막 숫자는 자기자신)
# 조건을 판단하는 방법은 다음과 같다.
# 1~n-1번째 숫자들을 돌며 해당 숫자가 자신보다 작고 최대길이가 자신의 길이보다 크면, 해당 숫자의 최대길이+1을 저장한다.

n = int(input())
A = list(map(int, input().split()))

length = [1] * n

for i in range(n):
    for j in range(i):
        if A[j]<A[i] and length[j]>=length[i]:
            length[i] = length[j] + 1
            
print(max(length))