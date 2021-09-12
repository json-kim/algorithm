# 백준 11399번 문제
# ATM

n = int(input())
p = list(map(int, input().split()))
resultTime = 0
waitTime = 0

p.sort()

for t in p[:n]:
    waitTime = waitTime + t
    resultTime = resultTime + waitTime
    
print(resultTime)