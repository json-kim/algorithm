# 백준 1463번 문제
# 1로 만들기 (동적 계획법)

# 3으로 나누어 떨어지면 3으로 나누고, 2로 나누어 떨어지면 2로 나눈다.
# 그렇지 않을 경우, 1을 뺀다. 최소의 연산으로 1로 만드는 횟수를 찾기
# 처음의 리스트에는 뺄셈만 수행했을 경우의 연산횟수를 입력한다.
n = int(input())

count = [i-1 for i in range(n+1)]
if n>1:
    count[2] = 1
if n>2:
    count[3] = 1
for i in range(2, n):
    count[i+1] = min(count[i+1], count[i]+1)
    if i*2 <= n:
        count[i*2] = min(count[i*2], count[i]+1)
    if i*3 <= n:
        count[i*3] = min(count[i*3], count[i]+1)
        
print(count[n])


