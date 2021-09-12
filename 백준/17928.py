# 백준 17928번 문제
# 오큰수

# 크기가 n인 수열 A의 각 원소에 대해 오큰수 구하기
# 오큰수: 오른쪽에 있으면서 해당 원소보다 큰 수중에 가장 왼쪽에 있는 수
# 없을 경우 -1
# 각 원소의 오큰수를 출력
# 스택에 값이 아니라 인덱스를 저장한게 포인트라고 생각한다.

n = int(input())
A = list(map(int, input().split()))

stack = []
stack.append(0)
NGE = [-1] * n

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)