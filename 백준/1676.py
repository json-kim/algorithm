# 백준 1676번 문제
# 팩토리얼 0의 개수

# n의 팩토리얼을 구했을 때,
# 뒤에서부터 시작하여 0이아닌 숫자가 나올때까지 존재하는 0의 갯수를 구하기
# 10이 몇번 곱해지느냐를 생각하기

N = int(input())

factorial = [1]*(N+1)
for i in range(2, N+1):
    factorial[i] = i * factorial[i-1]

result = 0
nFac = factorial[N]

while nFac%10 == 0:
    result = result + 1
    nFac = nFac // 10
    
print(result)