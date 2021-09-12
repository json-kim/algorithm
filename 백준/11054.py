# 백준 11054번 문제
# 가장 긴 바이토닉 부분 수열 (동적 계획법)

# 11053번 문제의 변형 문제이다.
# 수열의 n번째 숫자에서 증가하는 부분수열의 최대길이와, 감소하는 부분수열의 최대길이를 저장하고,
# 두 합의 최댓값을 찾으면 된다.
# 단 두 합의 경우 중심이 되는 자기자신이 2번해서 포함되기 때문에(증가하는 수열, 감소하는 수열 각각) -1을 해준게 최종 결과이다.

n = int(input())
A = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n

# 증가하는 부분수열 계산
for i in range(n):
    for j in range(i):
        if A[j] < A[i] and increase[j] >= increase[i]:
            increase[i] = increase[j] + 1

# 감소하는 부분수열 계산
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if A[j] < A[i] and decrease[j] >= decrease[i]:
            decrease[i] = decrease[j] + 1

def getMax(a, b):
    max = 0
    
    for i in range(len(a)):
        if max < a[i] + b[i]:
            max = a[i] + b[i]
    
    return max

print(getMax(increase, decrease)-1)